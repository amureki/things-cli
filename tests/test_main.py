from unittest import mock

from click.testing import CliRunner


class TestCLI:
    def test_send_email_message_ok(self):
        with mock.patch('things_cli.smtp.send_email_message') as mock_send_message:
            from things_cli.main import add

            runner = CliRunner()
            task_title = 'Buy milk'
            result = runner.invoke(add, [task_title, 'Low-fat, please'])
            mock_send_message.assert_called_once()
            assert result.exit_code == 0
            assert result.output == 'Task "{}" added to inbox!\n'.format(task_title)
