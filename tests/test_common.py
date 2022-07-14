from unittest import TestCase, mock

import common
from storage.transaction import Transaction


class CommonTest(TestCase):
    def setUp(self) -> None:
        self.transaction = Transaction()
        self.transaction.operations = {"aa": "20"}

    def test_begin(self):
        """Assert that begin a transaction returns a new instance."""
        t1 = common.begin(self.transaction)
        self.assertEqual(str(t1), "{}")

    def test_begin_w_none_transaction(self):
        """Assert that begin a transaction returns a new instance."""
        transaction = None
        t1 = common.begin(transaction)
        self.assertEqual(str(t1), "{}")

    @mock.patch("common.commited_transactions", {"ee": "20"})
    def test_commit(
        self,
    ):
        """Assert that commmit a transaction adds the new values

        to global transaction."""
        common.commit(self.transaction)
        self.assertEqual(common.commited_transactions["aa"], "20")

    def test_commit_w_empty_transaction(self):
        """Assert that commmit with no transaction prints

        show_no_transaction."""
        transaction = None
        with mock.patch("client.cli.show_no_transaction") as show_msg:
            common.commit(transaction)
            show_msg.assert_called_once()

    @mock.patch("common.commited_transactions", {"ee": "20"})
    def test_commit_transaction_w_none_values(self):
        """Assert that commmit a transaction remove None values."""
        self.transaction.operations["ee"] = None
        common.commit(self.transaction)
        assert common.commited_transactions == {"aa": "20"}

    def test_rollback(self):
        """Assert that rollback a transaction

        drops the current transaction."""
        common.rollback(self.transaction)
        self.assertEqual(str(self.transaction), "{}")

    def test_rollback_w_empty_transaction(self):
        """Assert that rollback with no transaction prints

        show_no_transaction."""
        transaction = None
        with mock.patch("client.cli.show_no_transaction") as show_msg:
            common.rollback(transaction)
            show_msg.assert_called_once()

    @mock.patch("common.cli.ask_string", side_effect=["aa"])
    def test_get_value(self, prompt_mock):
        """Assert that the method prints the right value."""
        with mock.patch("client.cli.show_msg") as show_msg:
            common.get_value(self.transaction)
            show_msg.assert_called_once_with("20")
            assert prompt_mock.call_count == 1

    def test_get_value_w_empty_transaction(self):
        """Assert that calling with empty transaction

        prints no transaction message.
        """
        transaction = None
        with mock.patch("client.cli.show_no_transaction") as show_msg:
            common.get_value(transaction)
            show_msg.assert_called_once()

    @mock.patch("common.commited_transactions", {"aa": "20"})
    def test_show_current_status_of_storage(self):
        """Assert that prints twice."""
        with mock.patch("client.cli.show_msg") as show_msg:
            common.show_current_status_of_storage(self.transaction)
            assert show_msg.call_count == 2

    def test_show_current_status_of_storage_w_empty_transaction(self):
        """Assert that calling with empty transaction prints no

        transaction message.
        """
        transaction = None
        with mock.patch("client.cli.show_no_transaction") as show_msg:
            common.show_current_status_of_storage(transaction)
            show_msg.assert_called_once()

    @mock.patch("common.commited_transactions", {"aa": "20"})
    @mock.patch("common.cli.ask_string", side_effect=["20"])
    def test_count_values_on_storage(self, ask_string_mock):
        """Assert that prints the right quantity."""
        with mock.patch("client.cli.show_msg") as show_msg:
            common.count_values_on_storage(self.transaction)
            show_msg.assert_called_once_with(1)
            ask_string_mock.assert_called()

    def test_count_values_on_storage_w_empty_transaction(self):
        """Assert that calling with empty transaction prints no

        transaction message.
        """
        transaction = None
        with mock.patch("client.cli.show_no_transaction") as show_msg:
            common.count_values_on_storage(transaction)
            show_msg.assert_called_once()

    @mock.patch("common.cli.set_prompt", side_effect=["ee", "20"])
    def test_set_key_value(self, set_prompt_mock):
        """Assert that sets the righ key-value pair."""
        common.set(self.transaction)
        assert len(self.transaction.operations.keys()) == 2
        set_prompt_mock.assert_called()

    def test_set_key_value_w_empty_transaction(self):
        """Assert that sets the righ key-value pair."""
        transaction = None
        with mock.patch("client.cli.show_no_transaction") as show_msg:
            common.set(transaction)
            show_msg.assert_called_once()

    @mock.patch("common.cli.ask_string", side_effect=["aa"])
    def test_unset(self, ask_string_mock):
        """Assert that set a value to None."""
        common.unset(self.transaction)
        self.assertIsNone(self.transaction.operations["aa"])
        ask_string_mock.assert_called_once()

    def test_unset_w_empty_transaction(self):
        """Assert that calling with empty transaction prints no

        transaction message.
        """
        transaction = None
        with mock.patch("client.cli.show_no_transaction") as show_msg:
            common.unset(transaction)
            show_msg.assert_called_once()

    def test_help(self):
        """Assert that prints the menu."""
        transaction = None
        with mock.patch("client.cli.menu") as show_msg:
            common.help(transaction)
            show_msg.assert_called_once()
