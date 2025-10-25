import pytest

@pytest.mark.skip(reason="Feature not yet implemented")
def test_feature_future():
    assert False

@pytest.mark.xfail(reason="Known bug in Chrome headless mode")
def test_known_bug():
    assert 1 == 2
