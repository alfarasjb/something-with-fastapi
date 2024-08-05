FROM python:3.12.3-bookworm AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app


RUN python -m venv /app/.venv
COPY requirements.txt ./
RUN /app/.venv/bin/pip install -r requirements.txt
FROM python:3.12.3-slim-bookworm
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv/
COPY . .
# Ensure the virtual environment's bin directory is in the PATH
# Need this to run uvicorn
ENV PATH="/app/.venv/bin:$PATH"

# Expose port
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]