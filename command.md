# run docker-compose build
docker-compose up --build

# go into docker terminal
docker exec -it django /bin/sh

# remove all the containers and images
docker stop $(docker ps -aq); docker rm $(docker ps -aq); docker rmi $(docker images -aq)