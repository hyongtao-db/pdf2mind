FROM python:3.12-slim

WORKDIR /app

# copy the code of pdf2mind to the container
COPY . .

RUN pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple --no-cache-dir -r requirements.txt
RUN apt update && \
    apt install -y graphviz && \
    apt clean && rm -rf /var/lib/apt/lists/*

ENV ARK_API_KEY=""
ENV OPENAI_API_KEY=""
ENV DASHSCOPE_API_KEY=""

ENTRYPOINT ["python", "pdf2mind.py"]
