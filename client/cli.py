import logging

from rich import print
from rich.prompt import Prompt

logger = logging.getLogger(__name__)


def menu() -> None:
    """Display the menu to the user."""
    print(":snake:Welcome to the Simple Storage System!:snake:\n")
    print("You can use the following commands:\n")
    print("\tBEGIN\t\t:small_orange_diamond: start a new transaction")
    print("\t\tSET\t\tSet a key-value pair.")
    print("\t\tUNSET\t\tUnset a key")
    print("\t\tGET\t\tGet the value associated with a key.")
    print("\t\tNUMEQUALTO\tReturns the number of keys that are")
    print("\t\t\t\tassociated with the given value.")
    print("\tCOMMIT\t\t:small_orange_diamond: commit the current transaction.")
    print("\tROLLBACK\t:small_orange_diamond: rollback the current")
    print("\t\t\t   transaction.")
    print("\tHELP\t\t:small_orange_diamond: show this help message")
    print("\tEND\t\t:small_orange_diamond: end the program")


def prompt() -> str:
    """Asks for a command."""
    command = Prompt.ask("Enter the command: ", default="HELP")
    command = command.strip().lower()
    return command


def show_msg(msg: str) -> None:
    """Shows a message."""
    print(msg)


def invalid_command() -> None:
    """Shows error msg."""
    msg = "error"
    show_msg(msg)


def show_no_transaction() -> None:
    """Shows NO TRANSACTION msg."""
    msg = "NO TRANSACTION"
    show_msg(msg)


def set_prompt() -> tuple[str, str]:
    """Asks for key and value to the user."""
    key, value = None, None
    while not key and not value:
        key = Prompt.ask("Enter a key")
        value = Prompt.ask("Enter a value")

    return key, value


def ask_string(msg: str) -> str:
    """Asks string to the user."""
    key = None
    while not key:
        key = Prompt.ask(f"Enter a {msg}")
    return key
