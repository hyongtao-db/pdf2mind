FROM python:3.12-slim

WORKDIR /app

# copy the code of pdf2mind to the container
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV ARK_API_KEY=""
ENV OPENAI_API_KEY=""
ENV DASHSCOPE_API_KEY=""

ENTRYPOINT ["python", "pdf2mind.py"]
