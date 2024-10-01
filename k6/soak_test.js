import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 5,              // 5 virtual users
  duration: '10m',     // Run the test for 10 minutes (soak test)
};

export default function () {
  const res = http.get('http://fastapi:8000/api/orchestrate');

  check(res, {
    'is status 200': (r) => r.status === 200,
  });

  sleep(2); // Pause for 2 seconds between requests
}
