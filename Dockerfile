FROM python:slim

WORKDIR /opt_meth

RUN python -m pip install --no-cache-dir --upgrade pip

COPY requirements.txt /opt_meth
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /opt_meth

CMD ["python", "-m", "main"]
