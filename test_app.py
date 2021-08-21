import cowsay
import pytest

def test_cowtext_includes_input():
    output = cowsay.get_output_string('cow', 'Hello World')

    assert 'Hello World' in output
