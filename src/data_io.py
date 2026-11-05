"""Small, non-mutating helpers for loading and profiling project CSVs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_raw_csv(filename: str, *, data_dir: Path | None = None, **kwargs: Any) -> pd.DataFrame:
    """Load one CSV from the local raw-data directory without changing it."""
    name = Path(filename)
    if name.name != filename or name.suffix.lower() != ".csv":
        raise ValueError("filename must be a plain CSV filename, not a path")

    path = (data_dir or RAW_DATA_DIR) / filename
    if not path.is_file():
        raise FileNotFoundError(
            f"Required local dataset not found: {path}. See README.md for source and placement."
        )
    return pd.read_csv(path, **kwargs)


def missing_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """Return a column-level missing-value summary, including zero-missing columns."""
    missing = frame.isna().sum()
    return pd.DataFrame(
        {
            "dtype": frame.dtypes.astype(str),
            "missing_n": missing,
            "missing_pct": (missing / max(len(frame), 1) * 100).round(2),
            "distinct_n": frame.nunique(dropna=True),
        }
    ).rename_axis("column").reset_index()


def duplicate_summary(frame: pd.DataFrame, *, key: str | list[str] | None = None) -> dict[str, int]:
    """Count duplicate rows and, optionally, duplicate values of a candidate key."""
    result = {"duplicate_rows": int(frame.duplicated().sum())}
    if key is not None:
        result["duplicate_key_rows"] = int(frame.duplicated(subset=key).sum())
        result["unique_key_n"] = int(frame.drop_duplicates(subset=key).shape[0])
    return result


def category_counts(frame: pd.DataFrame, column: str) -> pd.DataFrame:
    """Return category counts and percentages with missing values retained."""
    counts = frame[column].value_counts(dropna=False)
    return pd.DataFrame(
        {
            column: counts.index.astype("string"),
            "count": counts.to_numpy(),
            "percent": (counts.to_numpy() / max(len(frame), 1) * 100).round(2),
        }
    )
