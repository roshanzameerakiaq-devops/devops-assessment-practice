import json
import unittest
from unittest.mock import Mock

from app import TaskManagerHandler


class TestTaskManager(unittest.TestCase):

    def test_health_response(self):
        handler = object.__new__(TaskManagerHandler)
        handler.path = "/health"
        handler.send_response = Mock()
        handler.send_header = Mock()
        handler.end_headers = Mock()
        handler.wfile = Mock()

        handler.do_GET()

        handler.send_response.assert_called_once_with(200)

        body = handler.wfile.write.call_args[0][0]
        response = json.loads(body.decode())

        self.assertEqual(response, {"status": "healthy"})


if __name__ == "__main__":
    unittest.main()
