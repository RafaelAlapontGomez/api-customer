import logging.config
from fastapi import FastAPI

from app.v1.router.customer_router import router as customer_router

app = FastAPI()

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project. 
                                      # This will get the root logger since no logger in the configuration has this name.

logger.info("logging from the root logger")
app.include_router(customer_router)