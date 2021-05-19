## ELK stack deployment using Docker Compose

- This deployment has something special. Instead of using x-pack security model, I am using OpenDistro based security plugin.



### in case you need to create blank keystore for elasticsearch -

```
docker run --rm -v -v C:/temp/docker-compose/config:/usr/share/elasticsearch/config/ docker.elastic.co/elasticsearch/elasticsearch:7.10.2 elasticsearch-keystore create


docker run --rm -it -v C:/temp/docker-compose/config:/usr/share/elasticsearch/config/ docker.elastic.co/elasticsearch/elasticsearch:7.10.2 elasticsearch-keystore add azure.client.default.key


docker run --rm -it -v C:/temp/docker-compose/config:/usr/share/elasticsearch/config/ docker.elastic.co/elasticsearch/elasticsearch:7.10.2 elasticsearch-keystore add azure.client.default.account

```
