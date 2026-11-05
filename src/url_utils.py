"""URL and hostname normalization helpers shared by analysis notebooks."""

from __future__ import annotations

from urllib.parse import urlsplit

import pandas as pd


_MISSING = {"", "nan", "none", "null", "<na>"}


def _as_text(value: object) -> str | None:
    if pd.isna(value):
        return None
    text = str(value).strip()
    if text.lower() in _MISSING:
        return None
    return text


def normalize_url_key(value: object) -> str | None:
    """Normalize a URL for candidate matching by removing scheme and fragment.

    The host and path are lowercased to mirror the source dataset's URL-key
    normalization. A single trailing slash is removed. Query strings are kept.
    This is a matching aid, not a claim that two URLs have identical behavior.
    """
    text = _as_text(value)
    if text is None:
        return None
    candidate = text if "://" in text or text.startswith("//") else f"//{text}"
    parsed = urlsplit(candidate)
    host = parsed.netloc.lower().rstrip(".")
    path = parsed.path.lower()
    if path != "/":
        path = path.rstrip("/")
    query = parsed.query.lower()
    key = f"{host}{path}"
    if query:
        key = f"{key}?{query}"
    return key or None


def hostname_from_url(value: object) -> str | None:
    """Extract a lowercase hostname from URL- or host-shaped input."""
    text = _as_text(value)
    if text is None:
        return None
    candidate = text if "://" in text or text.startswith("//") else f"//{text}"
    try:
        host = urlsplit(candidate).hostname
    except ValueError:
        return None
    if not host:
        return None
    return host.lower().rstrip(".")


def tld_from_url(value: object) -> str | None:
    """Return the final hostname label; use a supplied TLD column when available."""
    host = hostname_from_url(value)
    if not host or "." not in host:
        return None
    return host.rsplit(".", 1)[-1]


def url_structure_complexity(frame: pd.DataFrame) -> pd.Series:
    """Count distinct URL-structure signals present (range 0–9).

    The score is a compact derived measure, not a validated security score.
    It counts whether each structure is present, rather than summing counts
    that mechanically grow with URL length. The analysis still stratifies by
    URL length as required by Q1.
    """
    signals = {
        "subdomain": frame["subdom_cnt"].fillna(0).gt(0),
        "path": frame["path_len"].fillna(0).gt(0),
        "query": frame["query_len"].fillna(0).gt(0),
        "ip_host": frame["is_ip"].fillna(0).gt(0),
        "special_characters": frame["special_cnt"].fillna(0).gt(0),
        "equals": frame["eq_cnt"].fillna(0).gt(0),
        "question_mark": frame["qm_cnt"].fillna(0).gt(0),
        "ampersand": frame["amp_cnt"].fillna(0).gt(0),
        "multiple_dots": frame["dot_cnt"].fillna(0).gt(1),
    }
    return pd.DataFrame(signals, index=frame.index).sum(axis=1).astype("int64")
