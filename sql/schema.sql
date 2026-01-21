CREATE TABLE IF NOT EXISTS systems (
    system_id INTEGER PRIMARY KEY AUTOINCREMENT,
    distro TEXT NOT NULL,
    kernel_version TEXT NOT NULL,
    architecture TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS updates (
    update_id INTEGER PRIMARY KEY AUTOINCREMENT,
    system_id INTEGER NOT NULL,
    package_count INTEGER NOT NULL,
    has_kernel_update INTEGER NOT NULL,
    risk_label INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(system_id) REFERENCES systems(system_id)
);

CREATE TABLE IF NOT EXISTS update_packages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    update_id INTEGER NOT NULL,
    package_name TEXT NOT NULL,
    old_version TEXT,
    new_version TEXT,
    FOREIGN KEY(update_id) REFERENCES updates(update_id)
);
