FROM python:3.12
COPY . .
RUN pip3 install -r requirements.txt
CMD python webserver.py
# docker buildx build -t mess:0.5 . 
# docker image ls
# docker run --name mess05 -p 8001:8000 -d mess:0.5
# docker ps | grep mess
# docker logs mess05
# docker exec -it mess05 bash # curl localhost:8000
# http://localhost:8001/