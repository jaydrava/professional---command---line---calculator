import subprocess
import sys


def test_main_runs_without_error():
    # Run the module as a script via Python command line
    result = subprocess.run([sys.executable, '-m', 'app.calculator'],
                            capture_output=True, text=True, input='exit\n')
    assert result.returncode == 0
    assert "Welcome to the Command Line Calculator" in result.stdout
