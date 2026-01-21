from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.utils.logger import get_logger

log = get_logger(__name__)


def train_risk_model(df):
    # Not enough data → explainable fallback
    if len(df) < 2:
        log.warning(
            "Not enough update records to train ML model. "
            "At least 2 updates are required."
        )
        log.info("Skipping ML training (demo mode)")
        return None

    X = df[["package_count", "has_kernel_update"]]
    y = df["risk_label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    log.info("Model evaluation:")
    print(classification_report(y_test, preds))

    return model
