# section3_project

## 개요
- [Metabase를 사용한 대시보드](http://rotbeer.duckdns.org)
  - 현재 문제가 있어 사용하지 않음
- [Flask를 사용한 API](http://rotbeer.duckdns.org/api)

## 사용 방법
1. csv_to_postgresql.py를 사용해 marketing_campaign.csv를 postgresql DB에 저장
2. db_to_ml_pickle.ipynb를 사용해 DB에서 데이터를 가져와 머신러닝을 모델을 만들고 피클 파일을 만듬
3. 피클 파일을 my_flask 디렉토리에 옮기고 도커 이미지를 만듬
    ```
    docker build -t repo/name:tag <DIR>
    ```
4. 도커 이미지 실행
    ```
    docker run -d -p 8000:8000 --name myflask --env-file env.list <IMAGE>
    ```
    - env.list는 환경변수를 설정해 주는 파일로 다음과 같은 형식을 따른다.
        ```
        metabase_url=http://127.0.0.1:3000/public/dashboard/something # 필요함
        VAR1=value1
        VAR2=value2
        ```
5. 대시보드를 사용하려면 metabase와 postgresql이 필요하다
    - Metabase Docker Image : https://hub.docker.com/r/metabase/metabase
    - Postgresql Docker Image: https://hub.docker.com/_/postgres
    - 둘 다 도커로 실행하거나 flask와 같은서버에서 실행할 필요 X
    - Metabase는 url로 공유 가능한 서비스

## Metabase 대시보드를 현재 사용하지 않는 이유
  - Metabase 컨테이너는 cpu와 ram을 많이 사용함
  - AWS Lightsail에서 ram 512MB 인스턴스는 실행조차 불가능, OOM(Out Of Memory)
  - ram 1GB 인스턴스는 실행은 가능하나 리소스를 많이 사용하고 10~20분 후 인스턴스가 멈춤
  - 대시보드를 사용하려면 높은 스펙의 인스턴스를 사용하거나, 리소스를 많이 사용할 수 있는 환경(PC)에서 실행하거나, Metabase가 아닌 다른 대시보드를 사용해야 함

## 사용한 기술
  - ~~Metabase~~
    - 리소스 부족
  - ~~Postgresql~~
    - Metabase 대시보드에서 사용할 DB로 사용했었음
    - RDS를 사용하지 않은 이유: 소규모 프로젝트에서는 RDS보다 도커 컨테이너로 사용하는게 적절하다고 생각
  - Flask
    - Python 웹 프레임워크, 웹페이지와 API 처리
  - Gunicorn
    - Python WSGI HTTP Server for UNIX, Flask 혹은 Django와 많이 사용하는 WSGI
    - Flask도 'Werkzeug'라는 WSGI가 있지만 production에서는 적합하지 않음
  - Nginx
    - 웹 서버, 리버스 프록시 등 강력한 기능을 가진 웹 서버 소프트웨어
    - Nginx 간단한 사용예제
      ```
      sudo apt update
      sudo apt install nginx
      sudo vim /etc/nginx/site-available/myexample

        server {
                listen 80;

                location / {
                        include proxy_params;
                        proxy_pass http://localhost:8000/;
                }
        }
      
      cd /etc/nginx/site-enable
      sudo rm default
      sudo ln -s /etc/nginx/site-available/myexam
      sudo nginx -s reload
      ```
  - AWS Lightsail
    - 사용하기 쉽고 저렴한 VPC
  - DuckDNS
    - free dynamic DNS hosted on AWS: https://www.duckdns.org/
    - google이나 github로 로그인하면 클릭 몇번으로 사용가능

## 찾아봐야 할 것
  - Flask와 gunicorn을 하나의 Docker Image로 만들고, 서버에서 Nginx와 Docker Engine을 사용해서 실행했는데
    - Nginx, Gunicorn, Flask 각각의 성능을 최대로 사용할 수 있는것인지?

## AWS Lightsail의 인스턴스에 ssh 사용하여 접근할 때
  - MobaXterm 이나 putty를 사용하는 글을 많이 봤지만 이유를 모르겠음
  - 대부분의 운영체제는 ssh를 기본적으로 지원함
  - 윈도우즈 파워쉘에서도 다음과 같은 방법으로 사용 가능함
    ```
    ssh USER@HOST -i <.pem file>
    ```
  - WINDOWS TERMINAL을 사용한다면 파워쉘에서 깔끔한 UI로 사용할 수 있음