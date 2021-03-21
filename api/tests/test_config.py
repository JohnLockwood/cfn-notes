from pytest import fixture
from app.core.config import Config


@fixture
def config():
    return Config()


def test_get_value_returns_value_if_key_is_good(config):
    value = config.get_value(Config.KEY_USER)
    assert value is not None
    assert value == 'api_user'


def test_get_value_returns_none_if_key_invalid(config):
    # Key invalid because of bad key
    value = config.get_value('bogus/key/is/bogus')
    assert value is None

    # Key is good, but mess up the object
    config.environment = "bogus/environment"
    value = config.get_value('db/name')
    assert value is None


def test_get_connection_string(config):
    value = config.get_connection_string()
    assert "None" not in value
    assert 'postgresql+psycopg2://' in value
    assert "api_user" in value


def test_get_connection_string_overriding_host(config):
    value = config.get_connection_string(host='foo')
    assert "None" not in value
    assert "foo" in value
