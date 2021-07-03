# ELK-DEP-OPTIONS

This repository contains various deployment options to build a elasticsearch cluster for use. 

- Using Docker Compose
- Using Docker Only
- Using Kubernetes
- OpenDistro Elastic
- 

Apart from this repository contains examples of Elasticsearch deployment using OpenDistro Security plugin instead of X-Pack. 


Befor running any elasticsearch cluster on Kubernetes/Docker, make sure node has maximum number of memory map areas a process may have defined.

```
sysctl -w vm.max_map_count=262144

```





## USING ELASTICSEARCH APIs

### Create a Simple Index with record

```

POST index-name/person/1 
{
    "name" : "Arun",
    "lastname" : "Ku",
    "job_description" : "DevOps"
}

# get GET 

curl -X GET "localhost:9200/mindex-name/person/1?pretty"





# Create document IDs automatically

POST my-index-000001/_doc/
{
  "@timestamp": "2099-11-15T13:12:00",
  "message": "GET /search HTTP/1.1 200 1070000",
  "user": {
    "id": "kimchy"
  }
}
```

### OIDC 

```
curl https://login.microsoftonline.com/<TENANT_ID>/v2.0/.well-known/openid-configuration | jq
https://gist.github.com/paulgrav/31909667f96614a645b1ceec5b9b06b0
```
