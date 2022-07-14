from unittest import TestCase, mock

import client.cli as cli


class ClientTest(TestCase):
    @mock.patch("client.cli.print")
    def test_menu(self, rich_print_mock):
        """Assert that prints the menu."""
        cli.menu()
        rich_print_mock.assert_called()

    @mock.patch("client.cli.Prompt")
    def test_prompt(self, rich_mock):
        """Assert that the command is formatted the right way."""
        begin_cmd = " BEGIN "
        rich_mock.ask.return_value = begin_cmd
        command = cli.prompt()
        self.assertEqual(command, begin_cmd.strip().lower())

    @mock.patch("client.cli.print")
    def test_show_msg(self, rich_print_mock):
        """Assert that print is called once."""
        msg = "Send help"
        cli.show_msg(msg)
        rich_print_mock.assert_called_once()

    @mock.patch("client.cli.print")
    def test_invalid_command(self, rich_print_mock):
        """Assert that print is called once."""
        cli.invalid_command()
        rich_print_mock.assert_called_once()

    @mock.patch("client.cli.print")
    def test_show_no_transaction(self, rich_print_mock):
        """Assert that print is called once."""
        cli.show_no_transaction()
        rich_print_mock.assert_called_once()

    @mock.patch("client.cli.Prompt")
    def test_set_prompt(self, rich_mock):
        """Assert that prompt retuns the key-value pair."""
        input = "test"
        rich_mock.ask.return_value = input
        key, value = cli.set_prompt()
        self.assertEqual(key, input)
        self.assertEqual(value, input)

    @mock.patch("client.cli.Prompt")
    def test_ask_string(self, rich_mock):
        """Assert that ask_string retuns the right key."""
        input = "test"
        rich_mock.ask.return_value = input
        key = cli.ask_string("key")
        self.assertEqual(key, input)
