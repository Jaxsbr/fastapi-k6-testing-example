# FastAPI + k6 Performance Testing Example

## Overview

This repository provides an example project that demonstrates how to:

1. Set up a simple **FastAPI** application that simulates random response times.
2. Perform **performance tests** and **soak tests** using **k6**.
3. Orchestrate both the FastAPI service and k6 tests using **Docker Compose**.

The goal of this project is to help developers learn how to:
- Build and deploy a Python-based **FastAPI** service.
- Use **k6** to conduct performance and load testing on an API.
- Leverage **Docker Compose** to easily spin up services and automate testing.

## Project Structure

```bash
├── Dockerfile               # Dockerfile to build the FastAPI service
├── app.py                   # FastAPI application code with random response times
├── docker-compose.yml        # Docker Compose file to manage FastAPI and k6 services
├── performance_test.js       # k6 script for basic performance testing
└── soak_test.js              # k6 script for soak testing
```

## Run
```yaml
# start
docker-compose up --build

# stop
docker-compose down
```

### Example Output

```
k6-soak-test         |      ✗ is status 200
k6-soak-test         |       ↳  98% — ✓ 362 / ✗ 5
k6-soak-test         |
k6-soak-test         |      checks.........................: 98.63% ✓ 362      ✗ 5
k6-soak-test         |      data_received..................: 64 kB  105 B/s
k6-soak-test         |      data_sent......................: 32 kB  52 B/s
k6-soak-test         |      http_req_blocked...............: avg=20µs     min=0s       med=12.58µs max=1.15ms   p(90)=17.03µs  p(95)=21.76µs
k6-soak-test         |      http_req_connecting............: avg=3.97µs   min=0s       med=0s      max=602.37µs p(90)=0s       p(95)=0s
k6-soak-test         |      http_req_duration..............: avg=6.23s    min=0s       med=5.63s   max=55.59s   p(90)=8.25s    p(95)=9.18s
k6-soak-test         |        { expected_response:true }...: avg=6.31s    min=556.88ms med=5.68s   max=55.59s   p(90)=8.27s    p(95)=9.18s
k6-soak-test         |      http_req_failed................: 1.36%  ✓ 5        ✗ 362
k6-soak-test         |      http_req_receiving.............: avg=196.58µs min=0s       med=176µs   max=3.85ms   p(90)=257.89µs p(95)=304.05µs
k6-soak-test         |      http_req_sending...............: avg=51.46µs  min=0s       med=49.16µs max=222.5µs  p(90)=69.57µs  p(95)=86.54µs
k6-soak-test         |      http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s
k6-soak-test         |      http_req_waiting...............: avg=6.23s    min=0s       med=5.63s   max=55.59s   p(90)=8.25s    p(95)=9.18s
k6-soak-test         |      http_reqs......................: 367    0.603533/s
k6-soak-test         |      iteration_duration.............: avg=8.23s    min=2s       med=7.64s   max=57.59s   p(90)=10.25s   p(95)=11.19s
k6-soak-test         |      iterations.....................: 367    0.603533/s
k6-soak-test         |      vus............................: 1      min=1      max=5
k6-soak-test         |      vus_max........................: 5      min=5      max=5
k6-soak-test         |
k6-soak-test         |
k6-soak-test         | running (10m08.1s), 0/5 VUs, 367 complete and 0 interrupted iterations
k6-soak-test         | default ✓ [ 100% ] 5 VUs  10m0s
k6-soak-test exited with code 0
```

## Difference Between Performance and Soak Testing
Performance Testing: Focuses on measuring the system's speed, responsiveness, and stability under peak or variable load over a short period (seconds to minutes). It identifies performance bottlenecks and scalability issues.

Soak Testing: Evaluates the system's long-term stability under constant, moderate load over an extended period (hours to days). It helps detect memory leaks, resource exhaustion, or performance degradation over time.
