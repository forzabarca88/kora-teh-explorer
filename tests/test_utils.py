import pytest
from src.utils import validate_content_size


def test_validate_content_size():
    # Test with content within the limit
    valid_content = "a" * (100 * 1024)  # 100 KB
    try:
        validate_content_size(valid_content)
    except ValueError:
        pytest.fail("validate_content_size raised ValueError unexpectedly for valid content.")
    
    # Test with content exceeding the limit
    invalid_content = "a" * (100 * 1024 + 1)  # 100 KB + 1 byte
    with pytest.raises(ValueError):
        validate_content_size(invalid_content)
