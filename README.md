This repo contains tests for Chatsky integration with three types of language tasks:

- slot extraction
- intent detection
- answer retrieval

The `models_service` directory contains a FastAPI service with three endpoints
for each of them:

- `/slot` endpoint extracts strings from a message using regex;
- `/intent` endpoint determines if a message displays any predefined intent;
- `/retrieve` endpoint returns an answer to a question if it is similar to an existing question.

The `intent`, `retrieval` and `slot` directories contain Chatsky pipelines that use the
endpoints and tests for the pipelines:

- `test.sh` checks that pipeline produces expected responses within the 0.4s window;
- `time_test.sh` prints the time it takes for pipeline to start working.

Run tests for the slot pipeline with:

```bash
docker compose up -d --build --remove-orphans && docker compose run slot bash ./test.sh
```

```bash
docker compose up -d --build --remove-orphans && docker compose run slot bash ./time_test.sh
```

Run tests for the intent pipeline with:

```bash
docker compose up -d --build --remove-orphans && docker compose run intent bash ./test.sh
```

```bash
docker compose up -d --build --remove-orphans && docker compose run intent bash ./time_test.sh
```

Run tests for the retrieval pipeline with:

```bash
docker compose up -d --build --remove-orphans && docker compose run retriaval bash ./test.sh
```

```bash
docker compose up -d --build --remove-orphans && docker compose run retriaval bash ./time_test.sh
```
