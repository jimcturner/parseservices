# Unit tests for module src/parse_services.py
# Run this from within the /tests subfolder otherwise the imports from /src will fail

import unittest
import sys

# Fix to allow unittest to search for modules/paths in the parent folder
sys.path.append("..")
from src.parse_services import get_port_and_protocol


class TestParseServices(unittest.TestCase):
    def test_parse_ntp_returns_udp_and_tcp_123(self):
        self.assertEqual("[{'udp': '123'}, {'tcp': '123'}]", str(get_port_and_protocol("ntp")))

    def test_parse_non_string_raises_exception(self):
        self.assertRaises(Exception, get_port_and_protocol, 1)


if __name__ == '__main__':
    unittest.main()
