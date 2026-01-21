import sqlite3
import platform
from pathlib import Path
from src.utils.logger import get_logger

log = get_logger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = PROJECT_ROOT / "data" / "update_engine.db"
SCHEMA_PATH = PROJECT_ROOT / "sql" / "schema.sql"
PACMAN_LOG = Path("/var/log/pacman.log")


def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA_PATH.read_text())
    return conn


def parse_pacman_updates():
    if not PACMAN_LOG.exists():
        return []

    lines = PACMAN_LOG.read_text().splitlines()
    packages = []

    for line in lines[-500:]:
        if " upgraded " in line:
            try:
                part = line.split(" upgraded ")[1]
                name, vers = part.split(" (")
                old, new = vers.strip(")").split(" -> ")
                packages.append((name.strip(), old.strip(), new.strip()))
            except ValueError:
                continue

    return packages


def main():
    log.info("Initializing database")
    conn = init_db()
    cur = conn.cursor()

    log.info("Storing system information")
    cur.execute(
        """
        INSERT INTO systems (distro, kernel_version, architecture)
        VALUES (?, ?, ?)
        """,
        ("arch", platform.release(), platform.machine()),
    )
    system_id = cur.lastrowid

    log.info("Parsing pacman logs")
    packages = parse_pacman_updates()
    has_kernel = int(any(pkg[0].startswith("linux") for pkg in packages))

    log.info("Storing update metadata")
    cur.execute(
        """
        INSERT INTO updates (system_id, package_count, has_kernel_update)
        VALUES (?, ?, ?)
        """,
        (system_id, len(packages), has_kernel),
    )
    update_id = cur.lastrowid

    for pkg in packages:
        cur.execute(
            """
            INSERT INTO update_packages
            (update_id, package_name, old_version, new_version)
            VALUES (?, ?, ?, ?)
            """,
            (update_id, *pkg),
        )

    conn.commit()
    conn.close()

    log.info(f"Update stored with {len(packages)} packages")


if __name__ == "__main__":
    main()
