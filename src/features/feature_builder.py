import sqlite3
import pandas as pd
from pathlib import Path
from src.utils.logger import get_logger

log = get_logger(__name__)
DB_PATH = Path("data/update_engine.db")


def build_features():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(
        """
        SELECT
            package_count,
            has_kernel_update
        FROM updates
        """,
        conn,
    )

    conn.close()

    log.info("Building risk labels")

    df["risk_label"] = (
        (df["package_count"] > 20)
        | (df["has_kernel_update"] == 1)
    ).astype(int)

    return df
