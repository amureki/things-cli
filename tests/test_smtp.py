from unittest import mock

from things_cli.smtp import send_email_message


class TestSMTP:
    def test_send_email_message_ok(self):
        with mock.patch('things_cli.smtp.connect_to_server') as mock_connect:
            mock_connect.return_value = mock.MagicMock()
            email_sent = send_email_message('test', 'body')
            mock_connect.assert_called_once()
            assert email_sent
