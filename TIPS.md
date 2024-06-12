## docker builds

docker-compose up -d --build

docker-compose build --progress=plain --no-cache

docker-compose up -d

docker build -t oshite_app .
docker run -p 8000:5000 -p 5679:5679 oshite_app

## docker removes

docker-compose down

docker-compose down --volumes

docker-compose down --rmi all --volumes --remove-orphans
