# Performance Test API image

Docker image for an Upstream API to hit for performance tests.

## Build and Run locally

Build:
```sh
docker build -t perf-upstream-api .
```

Run:
```sh
docker run -d -p 8082:8000 --rm --name perf-upstream-api perf-upstream-api
```

Stop:
```sh
docker stop perf-upstream-api
```

Push:
```sh
docker image tag perf-upstream-api fombicovmw/perf-upstream-api:{version}
docker image push fombicovmw/perf-upstream-api:{version}
```

## Usage

- http://{address}:8000/random - returns 1024 random characters
- http://{address}:8000/random?length=n - returns n random characters
