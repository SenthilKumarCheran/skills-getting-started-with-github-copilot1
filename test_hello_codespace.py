import builtins
import pytest
import builtins
from io import StringIO
from contextlib import redirect_stdout
import hello_codespace

def run_script_with_inputs(monkeypatch, inputs):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
    output = StringIO()
    with redirect_stdout(output):
        hello_codespace.main()
    return output.getvalue()

def test_greet_with_country(monkeypatch):
    inputs = ["Dana", "456 Elm St", "Utopia"]
    output = run_script_with_inputs(monkeypatch, inputs)
    assert "Hello, Codespace!" in output
    assert "Nice to meet you, Dana!" in output
    assert "Welcome from Utopia, Dana!" in output

def test_greet_no_country(monkeypatch):
    inputs = ["Eve", "789 Oak Ave", ""]
    output = run_script_with_inputs(monkeypatch, inputs)
    assert "Hello, Codespace!" in output
    assert "Nice to meet you, Eve!" in output
    assert "Welcome, Eve!" in output

def test_greet_empty_name(monkeypatch):
    inputs = ["", "No Address"]
    output = run_script_with_inputs(monkeypatch, inputs)
    assert "Hello, Codespace!" in output
    assert "Nice to meet you, !" in output

def test_no_address(monkeypatch):
    inputs = ["Alex", ""]
    output = run_script_with_inputs(monkeypatch, inputs)
    assert "Hello, Codespace!" in output
    assert "Nice to meet you, Alex!" in output
    assert "Address not provided." in output

def test_address_with_spaces(monkeypatch):
    inputs = ["Sam", "   "]
    output = run_script_with_inputs(monkeypatch, inputs)
    assert "Hello, Codespace!" in output
    assert "Nice to meet you, Sam!" in output
    assert "Address not provided." in output

def test_country_with_spaces(monkeypatch):
    inputs = ["Chris", "123 Main St", "   "]
    output = run_script_with_inputs(monkeypatch, inputs)
    assert "Hello, Codespace!" in output
    assert "Nice to meet you, Chris!" in output
    assert "Welcome, Chris!" in output

def test_all_empty(monkeypatch):
    inputs = ["", ""]
    output = run_script_with_inputs(monkeypatch, inputs)
    assert "Hello, Codespace!" in output
    assert "Nice to meet you, !" in output
    assert "Address not provided." in output
from io import StringIO
from contextlib import redirect_stdout
import hello_codespace

def run_script_with_inputs(monkeypatch, inputs):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
    output = StringIO()
    with redirect_stdout(output):
        hello_codespace.main()
    return output.getvalue()

def test_greet_with_country(monkeypatch):
    inputs = ["Dana", "456 Elm St", "Utopia"]
    output = run_script_with_inputs(monkeypatch, inputs)
    assert "Hello, Codespace!" in output
    assert "Nice to meet you, Dana!" in output
    assert "Welcome from Utopia, Dana!" in output

def test_greet_no_country(monkeypatch):
    inputs = ["Eve", "789 Oak Ave", ""]
    output = run_script_with_inputs(monkeypatch, inputs)
    assert "Hello, Codespace!" in output
    assert "Nice to meet you, Eve!" in output
    assert "Welcome, Eve!" in output

def test_greet_empty_name(monkeypatch):
    inputs = ["", "No Address"]
    output = run_script_with_inputs(monkeypatch, inputs)
    assert "Hello, Codespace!" in output
    assert "Nice to meet you, !" in output
