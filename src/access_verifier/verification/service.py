"""
Checks if the given IP is valid or not
"""

from src.access_verifier.access_manager.access_cache import AccessCache

def verify_access(ip: str) -> bool:
    """  
    Checks if the given IP is valid or not.
    :param ip: ip address
    :return: True or False
    """
    access_cache = AccessCache()
    return access_cache.is_trusted_ip(ip)
