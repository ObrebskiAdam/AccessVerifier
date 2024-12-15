"""
Module: access_cache

This module provides the AccessCache class, which is responsible for managing
trusted IP addresses using either a local file or a Redis server. The class
supports loading trusted IPs from a JSON file or a Redis set, and checking
if a given IP address is trusted.

Classes:
    AccessCache: Manages trusted IP addresses using a local file or a Redis server.
"""

import os
import json
from typing import Set
from cachetools import TTLCache
import redis

class AccessCache:
    """
       A class to manage trusted IP addresses using either a local file or a Redis server.

       Attributes:
           use_redis (bool): Flag to determine whether to use Redis for storing trusted IPs.
           redis_client (redis.StrictRedis): Redis client instance.
           ttl_cache (TTLCache): In-memory cache with TTL (Time To Live) for trusted IPs.
           trusted_ips (set): Set of trusted IP addresses.

       Methods:
           __init__(self, use_redis=False):
               Initializes the AccessCache instance.

           load_trusted_ips_from_file(self, file_path):
               Loads trusted IP addresses from a JSON file.

           load_trusted_ips_from_redis(self):
               Loads trusted IP addresses from a Redis set.

           load_trusted_ips(self):
               Loads trusted IP addresses from the appropriate source (file or Redis).

           is_trusted_ip(self, ip_address):
               Checks if the given IP address is trusted.
       """
    def __init__(self, use_redis=False):
        self.use_redis = use_redis

        # Configure Redis if use_redis is True
        if self.use_redis:
            self.redis_client = redis.StrictRedis(host='localhost', port=6379,
                                                  db=0, decode_responses=True)
            self.cache_key = 'trusted_ips'
        else:
            self.cache = TTLCache(maxsize=1000, ttl=86400)  # 24 hours TTL

        self.load_trusted_ips()

    def load_trusted_ips_from_file(self) -> Set[str]:
        """
        Load trusted IPs from a local file (for development purposes).
        """
        config_path = os.path.join(os.path.dirname(__file__), '../../config/trusted_ips.json')
        with open(config_path, 'r', encoding="UTF-8") as f:
            return set(json.load(f))

    def load_trusted_ips_from_redis(self) -> Set[str]:
        """
        Load trusted IPs from Redis (for production).
        """
        trusted_ips = self.redis_client.smembers(self.cache_key)
        return set(trusted_ips)


    def load_trusted_ips(self):
        """
        Load trusted IPs from the appropriate source based on the environment.
        """
        if self.use_redis:
            self.trusted_ips = self.load_trusted_ips_from_redis()
        else:
            self.trusted_ips = self.load_trusted_ips_from_file()
            self.cache['trusted_ips'] = self.trusted_ips


    def is_trusted_ip(self, ip: str) -> bool:
        """
        Check if the given IP is trusted.

        :param ip: IP address to check
        :return: True if the IP is trusted, otherwise False
        """
        if self.use_redis:
            trusted_ips = self.load_trusted_ips_from_redis()
        else:
            trusted_ips = self.cache.get('trusted_ips')
        return ip in trusted_ips
