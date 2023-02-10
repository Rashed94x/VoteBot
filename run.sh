DOCKER_TAG=votebot
docker build -t $DOCKER_TAG .
docker run -d --name $DOCKER_TAG $DOCKER_TAG