import logging

logger = logging.getLogger(__name__)


class Transaction:
    def __init__(self):
        self.operations = {}

    def set_key_value(self, key: str, value: str) -> None:
        """Sets a new key-value pair."""
        logger.debug("Setting key: %s, value: %s", key, value)
        self.operations[key] = value

    def delete_key(self, key: str) -> None:
        """Sets a value to None."""
        if key in self.operations:
            self.operations[key] = None

    def get_value(self, key: str) -> str:
        """Returns a value from a key."""
        try:
            value = self.operations[key]
        except KeyError:
            value = "NULL"
        return value

    def get_number_of_keys_equal_to(self, value: str) -> int:
        """Displays the number of keys that are associated

        with the given value.
        """
        count = sum(1 for v in self.operations.values() if v == value)
        return count

    def rollback(self) -> None:
        """Rollback a transaction."""
        if not self.operations:
            raise Exception("No transaction to rollback")
        logger.debug("Rolling back transaction")
        self.operations = {}

    def __str__(self) -> str:
        return str(self.operations)

    def __repr__(self) -> str:
        return str(self.operations)
