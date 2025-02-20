import pytest
import pydantic

from src.example_model import Config


def test_config_positive():
    config = Config.from_yaml("tests/config_positive.yaml")
    assert config.owner.name == "John Doe"
    assert config.owner.age == 30
    assert config.car.name == "BMW"


def test_config_negative():
    """Test invalid config"""
    with pytest.raises(pydantic.ValidationError) as exec_info:
        config = Config.from_yaml("tests/config_negative.yaml")
    assert str(exec_info.value).startswith("2 validation errors for Config")
    