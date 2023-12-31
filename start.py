from time import time
import uvicorn
import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
from sqlalchemy.sql import text

from app.db.session import SessionLocal

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute(text('SELECT 1'))
    except Exception as e:
        logger.error(e)
        raise e
    finally:
        logger.info("db close (start)")
        db.close()


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, log_level="debug")


# from app import settings

# if __name__ == "__main__":
#     uvicorn.run("app.main:app", port=8001)
