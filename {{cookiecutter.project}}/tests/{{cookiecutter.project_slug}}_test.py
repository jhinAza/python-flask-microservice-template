{% if cookiecutter.test_suite == "unittest" %}
import unittest

class TestTrue(unittest.TestCase):

    def test_true(self):
        self.assertTrue(True)
{% elif cookiecutter.test_suite == "pytest" %}
import pytest

class TestTrue():

    def test_true(self):
        assert True
{% endif %}

