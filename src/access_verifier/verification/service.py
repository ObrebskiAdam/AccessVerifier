"""
Checks if the given IP is valid or not
"""
# Sample IPS
TRUSTED_IPS = {"192.168.1.1", "192.168.1.2", "203.0.113.5"}


def verify_access(ip: str) -> bool:
    """  
    Checks if the given IP is valid or not.
    :param ip: ip address
    :return: True or False
    """
    if ip not in TRUSTED_IPS:
        return False

    return True
