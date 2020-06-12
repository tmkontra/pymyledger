import logging

from .pymyledger import PyMyLedger


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Logging configured")
    logging.debug("Starting application")
    PyMyLedger()

if __name__ == "__main__":
    main()
