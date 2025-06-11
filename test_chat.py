import pytest
from chatbot import get_response

def test_greeting():
    assert get_response("Hi") == "Hello! How can I help you?"

def test_farewell():
    assert get_response("bye") == "Goodbye! Have a nice day!"

def test_unknown():
    assert get_response("random text") == "Sorry, I don't understand that."
