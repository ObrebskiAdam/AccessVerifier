# Stage 1: Base image
FROM python:3.13-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/app" \
    VENV_PATH="/app/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Stage 2: Builder
FROM python-base as builder

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    curl \
    build-essential

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry install

COPY . .
RUN poetry run pytest

# Stage 3: Runtime
FROM python-base as runtime

WORKDIR $PYSETUP_PATH

# Copy only necessary files from builder
COPY --from=builder $PYSETUP_PATH/.venv $PYSETUP_PATH/.venv
COPY --from=builder $PYSETUP_PATH/src ./src

EXPOSE 8000

CMD ["uvicorn", "src.access_verifier.main:app", "--host", "0.0.0.0", "--port", "8000"]