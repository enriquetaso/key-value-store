from client import cli
from storage.transaction import Transaction

commited_transactions = {}


def begin(transaction: Transaction | None) -> Transaction:
    """Returns a new Transaction instance."""
    return Transaction()


def commit(transaction: Transaction | None) -> None:
    """Updates the commited_transactions with

    new ones and remove None values.
    """
    if not transaction:
        cli.show_no_transaction()
        return
    global commited_transactions
    commited_transactions.update(transaction.operations)
    commited_transactions = {
        k: v for k, v in commited_transactions.items() if v is not None
    }


def rollback(transaction: Transaction | None) -> None:
    """Rollback a transaction or show no transaction msg."""
    if not transaction:
        cli.show_no_transaction()
        return
    transaction.rollback()


def get_value(transaction: Transaction | None) -> Transaction | None:
    """Retrieves a value for a given key."""
    # I assume that in this part of the exercise you want to display
    # the message "No transaction" when the transaction has not
    # taken place.
    if not transaction:
        cli.show_no_transaction()
        return
    key = cli.ask_string("Enter a key")
    value = transaction.get_value(key)
    cli.show_msg(value)
    return transaction


def show_current_status_of_storage(
    transaction: Transaction | None,
) -> Transaction | None:
    """Shows the status of transactions."""
    if not transaction:
        cli.show_no_transaction()
        return
    cli.show_msg(transaction)
    cli.show_msg(commited_transactions)
    return transaction


def count_values_on_storage(
    transaction: Transaction | None,
) -> Transaction | None:
    """Returns the number of keys that are associated with the

    given value.
    """
    if not transaction:
        cli.show_no_transaction()
        return
    key = cli.ask_string("Enter a value")
    value = transaction.get_number_of_keys_equal_to(key)
    cli.show_msg(value)
    return transaction


def set(transaction: Transaction | None) -> Transaction | None:
    """Associates a key with a value and stores it

    or prints a no transaction msg.
    """
    if not transaction:
        cli.show_no_transaction()
        return
    key, value = cli.set_prompt()
    transaction.set_key_value(key, value)
    return transaction


def unset(transaction: Transaction | None) -> Transaction | None:
    """Calls delete on a key or prints a no transaction msg."""
    if not transaction:
        cli.show_no_transaction()
        return
    key = cli.ask_string("Enter a key")
    transaction.delete_key(key)
    return transaction


def help(transaction: Transaction | None) -> Transaction | None:
    """Shows the menu."""
    cli.menu()
    return transaction


OPTIONS = {
    "begin": begin,
    "commit": commit,
    "rollback": rollback,
    "get": get_value,
    "show": show_current_status_of_storage,
    "numequalto": count_values_on_storage,
    "set": set,
    "unset": unset,
}
