import logging
import datetime
from pathlib import Path

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

    try:
        curr_path_splitted = str(Path.cwd()).split('/')
        if curr_path_splitted[len(curr_path_splitted) - 1] == 'src':
            root_name = '../log/'
        else:
            root_name = 'log/'
        logging.basicConfig(filename = root_name + 
                str(datetime.datetime.now()).replace(' ', '_').replace(':', '')[:17] + origin + '.log', 
                level=level, 
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    except:
        raise KeyError("Invalid logger level")
    return logging.getLogger(__name__)
