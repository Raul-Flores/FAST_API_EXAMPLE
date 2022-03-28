FROM python:3.8
WORKDIR /app
COPY requirements.txt requirements.txt
EXPOSE 8000
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY main-sql.py database.py schemas.py .
CMD ["uvicorn", "main-sql:app", "--host", "0.0.0.0", "--port", "8000"]
