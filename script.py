import logging
import sys
import traceback

from rich.logging import RichHandler

from client import cli, constants
from common import OPTIONS

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
)

logger = logging.getLogger(__name__)


def start_app() -> None:
    """Start the key-value application."""
    transaction = None
    while True:
        logger.debug("Transactions: %s", transaction)
        command = cli.prompt()
        logger.debug("Command: %s", command)
        if command in constants.END_COMMAND:
            break
        if command in constants.HELP_COMMAND:
            cli.menu()
        try:
            transaction = OPTIONS[command](transaction)
        except KeyError:
            cli.invalid_command()


def main() -> None:
    try:
        cli.menu()
        start_app()
    except KeyboardInterrupt:
        cli.show_msg("Shutdown requested... exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()
