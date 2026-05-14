from app.logger import get_logger
from app.scanner import get_rsync_version
from app.report import generate_report
from app.utils import load_targets

logger = get_logger()

def main():
    logger.info("Starting vulnerability simulation workflow")

    targets = load_targets("data/sample_targets.txt")

    version = get_rsync_version()

    logger.info(f"Detected rsync version: {version}")
    logger.info(f"Loaded {len(targets)} targets")

    generate_report(version, targets)

    logger.info("Workflow completed")

if __name__ == "__main__":
    main()
