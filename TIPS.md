## docker builds

docker-compose up -d --build

docker-compose build --progress=plain --no-cache

## docker removes

docker-compose down

docker-compose down --volumes

docker-compose down --rmi all --volumes --remove-orphans