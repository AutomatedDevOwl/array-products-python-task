import sys
import time
import pytest


class TestCaseWebHost():

    @pytest.fixture
    def example_fixture(self):
        return 'test_fixture'

    def wait_before_closing_browser(self):
        time.sleep(5)

    def setup_method(self, method):
        sys.stdout.write('\n' + 'setting up test..\n')

    def teardown_method(self, method):
        sys.stdout.write('\n' + 'tearing down test..')
