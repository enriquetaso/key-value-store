from unittest import TestCase, mock

from script import main, start_app


class ScriptTest(TestCase):
    @mock.patch("script.cli.prompt", return_value="END")
    def test_start_app_end(self, prompt_mock):
        """Assert that start_app ends with END command."""
        start_app()
        prompt_mock.assert_called_once()

    @mock.patch("script.cli.prompt", side_effect=["help", "end"])
    def test_start_app_help(self, prompt_mock):
        """Assert that start_app ask twice with HELP command."""
        start_app()
        assert prompt_mock.call_count == 2

    @mock.patch("script.cli.prompt", side_effect=["begin", "END"])
    def test_start_app_begin_command(self, prompt_mock):
        """Assert that start_app ask twice with BEGIN command."""
        start_app()
        assert prompt_mock.call_count == 2

    @mock.patch("script.cli.invalid_command")
    @mock.patch("script.cli.prompt", side_effect=["INVALID", "END"])
    def test_start_app_invalid(self, prompt_mock, invalid_command_mock):
        """Assert that start_app calls invalid_command

        with invalid command propomted."""
        start_app()
        assert prompt_mock.call_count == 2
        invalid_command_mock.assert_called_once()


class ScriptMainTest(TestCase):
    @mock.patch("script.cli.menu")
    @mock.patch("script.start_app", side_effect=Exception)
    @mock.patch("sys.exit")
    def test_main_exception(self, exit_mock, start_app_mock, menu_mock):
        """Assert that main calls sys.exit on Exception."""
        main()
        exit_mock.assert_called_once()
        start_app_mock.assert_called_once()
        menu_mock.assert_called_once()

    @mock.patch("script.cli.menu")
    @mock.patch("script.start_app", side_effect=KeyboardInterrupt)
    @mock.patch("sys.exit")
    def test_main_keyboardinterrupt(self, exit_mock, start_app_mock,
                                    menu_mock):
        """Assert that main calls sys.exit on KeyboardInterrupt."""
        main()
        exit_mock.assert_called_once()
        start_app_mock.assert_called_once()
        menu_mock.assert_called_once()
