if [[ "$1" == "" ]]; then
  echo "usage: $0 [twitch channel]"
  exit 1
fi

docker run -p 8765:8765 -e CHANNEL=$1 -v $PWD/sample:/opt/app/sample ghcr.io/atrioc-devs/muddled-mock:latest

