FROM joyzoursky/python-chromedriver:3.9

WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt

COPY . /src

CMD ["pytest", "test_clicks.py"]