# Access Cache Manager  
  
This project provides a module for managing trusted IP addresses using either a local file or a Redis server. The module includes a class `AccessCache` that supports loading trusted IPs from a JSON file or a Redis set, and checking if a given IP address is trusted.  
  
## Features  
  
- Load trusted IP addresses from a JSON file.  
- Load trusted IP addresses from a Redis set.  
- Check if an IP address is trusted.  
- In-memory caching with TTL (Time To Live) for performance optimization.  
  
## Installation  
  
To install the dependencies for this project, you need to have [Poetry](https://python-poetry.org/) installed. You can install the dependencies using the following command:  
  
```bash  
poetry install  
```
## Testing
 
To run the tests, use the following command:

```bash  
poetry run pytest  
```
## How to run project
```bash  
poetry run uvicorn src.access_verifier.main:app 
```
## Directory Structure
```
project_root/  
├── config/  
│   └── trusted_ips.json  
├── src/  
│   ├── access_verifier/  
│   │   ├── verification/  
│   │   │   ├── api.py  
│   │   │   └── __init__.py  
│   │   ├── access_manager/  
│   │   │   ├── access_cache.py  
│   │   │   └── __init__.py  
│   │   └── __init__.py  
├── tests/  
│   ├── test_access_cache.py  
├── pyproject.toml  
└── README.md 
```
