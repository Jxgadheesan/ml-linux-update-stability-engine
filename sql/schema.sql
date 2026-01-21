CREATE TABLE IF NOT EXISTS systems (
    system_id INTEGER PRIMARY KEY AUTOINCREMENT,
    distro TEXT NOT NULL,
    distro_version TEXT,
    kernel_version TEXT NOT NULL,
    architecture TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS updates (
    update_id INTEGER PRIMARY KEY AUTOINCREMENT,
    system_id INTEGER NOT NULL,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    package_count INTEGER NOT NULL,
    update_type TEXT NOT NULL,
    FOREIGN KEY (system_id) REFERENCES systems(system_id)
);

CREATE TABLE IF NOT EXISTS update_packages (
    update_package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    update_id INTEGER NOT NULL,
    package_name TEXT NOT NULL,
    old_version TEXT,
    new_version TEXT NOT NULL,
    is_core INTEGER DEFAULT 0,
    FOREIGN KEY (update_id) REFERENCES updates(update_id)
);

CREATE TABLE IF NOT EXISTS failures (
    failure_id INTEGER PRIMARY KEY AUTOINCREMENT,
    update_id INTEGER NOT NULL,
    failure_type TEXT,
    severity INTEGER,
    description TEXT,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (update_id) REFERENCES updates(update_id)
);

CREATE TABLE IF NOT EXISTS recovery_actions (
    recovery_id INTEGER PRIMARY KEY AUTOINCREMENT,
    update_id INTEGER NOT NULL,
    action TEXT,
    success INTEGER,
    FOREIGN KEY (update_id) REFERENCES updates(update_id)
);
