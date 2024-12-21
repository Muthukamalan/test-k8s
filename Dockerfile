FROM python:3.9-slim-buster AS build
RUN apt-get update -y && apt install -y --no-install-recommends git build-essential  && pip install --no-cache-dir -U pip
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENV GRADIO_SERVER_PORT=7860
EXPOSE 7860
CMD [ "python","app.py" ]



# OSError: Cannot find empty port in range: 7860-7860. You can specify a different port by setting the GRADIO_SERVER_PORT environment variable or passing the `server_port` parameter to `launch()`.

