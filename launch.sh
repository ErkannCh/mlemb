docker build -t lc-fastapi-app .
docker rm -f lc-fastapi-container
docker run -d -p 9000:9000 --name lc-fastapi-container lc-fastapi-app