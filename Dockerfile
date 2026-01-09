FROM python

RUN mkdir -p python-testapp

WORKDIR /python-testapp

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /python-testapp

EXPOSE 5000

CMD ["sh", "-c", "python init_db.py && python run.py"]
