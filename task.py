import logging
import logging.config

logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    format='%(name)s => %(levelname)s => %(message)s'
)


class CustomHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)


class TestFilter(logging.Filter):
    def filter(self, record):
        return not (record.msg.lower().startswith('test'))


logging.config.fileConfig('logging_config.ini')
logger = logging.getLogger('sampleLogger')

logger.debug('Debug message')gu
