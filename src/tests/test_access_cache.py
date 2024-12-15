import pytest
from src.access_verifier.access_manager.access_cache import AccessCache

# Sample data for testing
sample_ips = {"192.168.1.1", "192.168.1.2", "203.0.113.5"}


@pytest.fixture
def access_cache():
    return AccessCache(use_redis=False)


def test_load_trusted_ips_from_file(access_cache, mocker):
    mocker.patch('src.access_verifier.access_manager.access_cache.AccessCache.load_trusted_ips_from_file',
                 return_value=sample_ips)
    access_cache.load_trusted_ips()
    assert access_cache.trusted_ips == sample_ips


def test_is_trusted_ip(access_cache, mocker):
    mocker.patch('src.access_verifier.access_manager.access_cache.AccessCache.load_trusted_ips_from_file',
                 return_value=sample_ips)
    access_cache.load_trusted_ips()
    assert access_cache.is_trusted_ip("192.168.1.1") is True
    assert access_cache.is_trusted_ip("192.168.1.3") is False


def test_load_trusted_ips_from_redis(mocker):
    mock_redis_client = mocker.Mock()
    mock_redis_client.smembers.return_value = sample_ips

    mocker.patch('redis.StrictRedis', return_value=mock_redis_client)
    access_cache = AccessCache(use_redis=True)
    access_cache.load_trusted_ips()

    assert access_cache.trusted_ips == sample_ips


def test_is_trusted_ip_with_redis(mocker):
    mock_redis_client = mocker.Mock()
    mock_redis_client.smembers.return_value = sample_ips

    mocker.patch('redis.StrictRedis', return_value=mock_redis_client)
    access_cache = AccessCache(use_redis=True)
    access_cache.load_trusted_ips()

    assert access_cache.is_trusted_ip("192.168.1.1") is True
    assert access_cache.is_trusted_ip("192.168.1.3") is False