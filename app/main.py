import logging

from .pymyledger import PyMyLedger

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Logging configured")
    logging.debug("Starting application")
    PyMyLedger()
