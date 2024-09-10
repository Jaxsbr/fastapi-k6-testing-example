import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 10,          // 10 virtual users
  duration: '30s',  // Test runs for 30 seconds
};

export default function () {
  const res = http.get('http://fastapi:8000/api/orchestrate');

  check(res, {
    'is status 200': (r) => r.status === 200,
    'response time < 2s': (r) => r.timings.duration < 2000,
  });

  sleep(1); // Pause for 1 second between requests
}
