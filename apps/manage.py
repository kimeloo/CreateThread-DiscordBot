import logging
logger = logging.getLogger("app_mgr")

def import_thread():
    from thread import main as thread
    thread.run()

def run():
    modules = [import_thread]
    for func in modules:
        try:
            func()
        except ImportError as e:
            logger.error('Module Not Available : {}'.format(e.args[0]))


if __name__ == '__main__':
    run()