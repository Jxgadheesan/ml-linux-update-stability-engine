from src.features.feature_builder import build_features
from src.models.risk_model import train_risk_model
from src.utils.logger import get_logger

log = get_logger(__name__)


def main():
    log.info("Building features")
    df = build_features()

    log.info("Training ML model")
    train_risk_model(df)


if __name__ == "__main__":
    main()
