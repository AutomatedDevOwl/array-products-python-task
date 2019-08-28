import sys
import pytest
from .test_case_array_products import TestCaseWebHost


class TestWebHost(TestCaseWebHost):

    def test_site88(self, example_fixture):

        # Print example pytest fixture.
        sys.stdout.write('hello world')

