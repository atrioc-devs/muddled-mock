IMG=ghcr.io/atrioc-devs/muddled-mock:latest
docker build . -t $IMG
if [[ "$1" == "publish" ]]; then
  docker push $IMG
fi

