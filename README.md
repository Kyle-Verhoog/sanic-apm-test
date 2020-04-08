# sanic-apm-test - to test sanic and datadog integration

To install/run:

```bash
$ cp .env.template .env  # Fill in your Datadog API key
$ docker-compose up -d
```

- Invoke the endpoint `http://localhost:8080/query` to start logging traces.
