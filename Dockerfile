FROM python:3.11.2 AS builder
COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.11.2-slim
WORKDIR /code

COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local:$PATH

CMD [ "python", "-u", "./run.py" ]