from unittest import TestCase

import pytest

from storage.transaction import Transaction


class StorageTest(TestCase):
    def setUp(self) -> None:
        self.transaction = Transaction()
        self.transaction.operations = {"aa": "00"}

    def test_get_value(self):
        """Assert that get_value returns the right value."""
        key = "aa"
        value = self.transaction.get_value(key)
        assert value == "00"

    def test_get_wrong_value(self):
        """Assert that passing a invalid key returns NULL."""
        key = "wrong"
        value = self.transaction.get_value(key)
        assert value == "NULL"

    def test_set_key_value(self):
        """Assert that the method set the righ key-value pair."""
        key_value = "Test"
        self.transaction.set_key_value(key_value, key_value)
        assert self.transaction.operations[key_value] == key_value

    def test_delete_key(self):
        """Assert that the key is set to None."""
        self.transaction.delete_key("aa")
        self.assertIsNone(self.transaction.operations["aa"])

    def test_get_number_of_keys_equal_to(self):
        """Assert that the method returns the quantity of matches."""
        result = self.transaction.get_number_of_keys_equal_to("00")
        assert result == 1

    def test_rollback(self):
        """Assert that operations are empty after rollback."""
        self.transaction.rollback()
        self.assertDictEqual(self.transaction.operations, {})

    def test_rollback_no_transaction(self):
        """Assert that rollback raises exception if no transaction exits."""
        with pytest.raises(Exception):
            t2 = Transaction()
            t2.rollback()

    def test_str(self):
        """Assert that print returns the value of operations"""
        self.assertEqual(str(self.transaction), "{'aa': '00'}")

    def test__repr__(self):
        """Assert that repr returns the value of operations"""
        self.assertEqual(repr(self.transaction), "{'aa': '00'}")
