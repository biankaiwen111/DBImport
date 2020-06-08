import logging
import datetime

def initiateLogger(origin, level):
    '''Initiate a logger with given logging level and logging origin

    Args:
        origin: from which source this logger is from (for determining logging file name)
        level: the level of the logger, options are [INFO, DEBUG, WARNING, ERROR, CRITICAL]
    Raises:
        KeyError: The level parameter is not valid
    Returns:
        the logger object

    '''
    if level == 'INFO':
        loggerLevel = logging.INFO
    elif level == 'DEBUG':
        loggerLevel = logging.DEBUG
    elif level == 'WARNING':
        loggerLevel = logging.WARNING
    elif level == 'ERROR':
        loggerLevel = logging.ERROR
    elif level == 'CRITICAL':
        loggerLevel = logging.CRITICAL
    else:
        raise KeyError('Invalid logging level')

    logging.basicConfig(filename = '../log/' + 
                str(datetime.datetime.now()).replace(' ', '_').replace(':', '')[:17] + origin + '.log', 
                level=loggerLevel, 
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)