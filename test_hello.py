# test_hello.py
import subprocess

def test_hello_world():
    result = subprocess.run(["python", "hello.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, World!"
