FROM python:3.11

WORKDIR Users/Dilmurod/Desktop/TodoApp
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
