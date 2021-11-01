# Performance Test API image

Docker image for an Upstream API to hit for performance tests.

## Usage

- http://{address}:8000/random - returns 1024 random characters, base64-encoded
- http://{address}:8000/random?length=n - returns n random characters, base64-encoded
