FROM gitlab.sdu.dk:5050/odw-e2020/docker:python-latest
RUN pip install Flask
RUN pip install flask_mysqldb
COPY . .
CMD python3 backend.py