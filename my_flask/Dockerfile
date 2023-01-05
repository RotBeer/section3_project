FROM python:3.8-slim

COPY . /my_flask

RUN pip install flask
RUN pip install gunicorn
RUN pip install -U scikit-learn
RUN pip install category_encoders

WORKDIR /

CMD ["gunicorn", "my_flask:create_app()", "--bind=0.0.0.0"]