# Python-Mongodb
Para iniciar el docker, ejecutar:
~~~{.diff}
docker run --hostname=688f62608249 --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=GOSU_VERSION=1.16 --env=JSYAML_VERSION=3.13.1 --env=MONGO_PACKAGE=mongodb-org --env=MONGO_REPO=repo.mongodb.org --env=MONGO_MAJOR=7.0 --env=MONGO_VERSION=7.0.5 --env=HOME=/data/db --volume=/data/configdb --volume=/data/db -p 27017:27017 --restart=no --label='org.opencontainers.image.ref.name=ubuntu' --label='org.opencontainers.image.version=22.04' --runtime=runc -d mongo
~~~
