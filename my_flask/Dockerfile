FROM python:3.8-slim

COPY . /my_flask

RUN pip install flask
RUN pip install gunicorn
RUN pip install -U scikit-learn
RUN pip install category_encoders

WORKDIR /

CMD ["gunicorn", "--workers=1", "my_flask:create_app()", "-b", "0.0.0.0:8000"]