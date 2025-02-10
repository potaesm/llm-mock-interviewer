import sys

import pytest

if __name__ == "__main__":
    # Run pytest on the tests directory
    exit_code = pytest.main(["-v", "./tests/test_models.py"])

    sys.exit(exit_code)
