# sentry-exception-group-issue

## First-time Setup

If you do not have Poetry installed, [install it first](https://python-poetry.org/docs/#installation).

Then run `poetry install`.

## Reproduction Steps

1. Set the value of `SENTRY_DSN` in your shell's environment, e.g. `export SENTRY_DSN=...`
2. Run `poetry run uvicorn app:app`
3. Visit http://localhost:8000/docs in your browser
4. Select "Try it out" and then "Execute" under one of the endpoints to call it and trigger an exception
