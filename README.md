# ELK-DEP-OPTIONS

This repository contains various deployment options to build a elasticsearch cluster for use. 

- Docker Only
- Docker Compose + No Auth [BASIC LICENSE]
- Docker Compose + AD Auth [BASIC LICENSE]
- Docker Compose + OpenID Connect Auth [BASIC LICENSE]
- Standard Kubernetes + Snapshot Plugin + No Auth [BASIC LICENSE]
- Standard Kubernetes using ECK + Snapshot Plugin + Basic Auth [BASIC LICENSE]
- Standard Kubernetes + Snapshot Plugin + OpenDistro Security Plugin + Basic Auth [BASIC LICENSE]
- Standard Kubernetes + Snapshot Plugin + OpenDistro Security Plugin + AD Auth [BASIC LICENSE]
- Standard Kubernetes + Snapshot Plugin + OpenDistro Security Plugin + OpenID Connect Auth [BASIC LICENSE]
- OpenDistro Elasticsearch

Apart from this repository contains examples of Elasticsearch deployment using OpenDistro Security plugin instead of X-Pack. 


Befor running any elasticsearch cluster on Kubernetes/Docker, make sure node has maximum number of memory map areas a process may have defined.

```
sysctl -w vm.max_map_count=262144

```




### OIDC 

```
curl https://login.microsoftonline.com/<TENANT_ID>/v2.0/.well-known/openid-configuration | jq
https://gist.github.com/paulgrav/31909667f96614a645b1ceec5b9b06b0
```

### LOGGING
Module based logging. Find list of modules at - https://github.com/elastic/elasticsearch/tree/master/server/src/main/java/org/elasticsearch

3 ways to achieve -

- By updating the cluster settings dynamically

```
PUT /_cluster/settings
{
  "transient": {
    "logger.org.elasticsearch.http": "DEBUG",
    "logger.org.elasticsearch.index": "DEBUG",
    "logger.org.elasticsearch.rest" : "DEBUG",
    "logger.org.elasticsearch.transport": "DEBUG",
    "logger.org.elasticsearch.snapshots":"DEBUG",
    "logger.org.elasticsearch.indices":"DEBUG"
  }
}

```
- By setting the log level directly in elasticsearch.yml

```
logger.org.elasticsearch.transport: DEBUG

```
- By setting the log level directly in log4j2.properties
```
logger.transport.level = trace
```


### Azure Snapshot Logging

Register 
```
PUT _snapshot/<nameofrepo>
{
  "type": "azure",
  "settings": {

	  "container": "<nameOfContainer>",
	  "base_path" : "/"

  }
}
```

Verify Snapshot repo
```
POST /_snapshot/<name>/_verify
```

Take Backup of all cluster
```
PUT /_snapshot/<nameofrepo>/<snapshot-{now/d}>?wait_for_completion=true

# more granual
PUT /_snapshot/<nameofrepo>/snapshot_2?wait_for_completion=true
{
  "indices": "index_1,index_2",
  "ignore_unavailable": true,
  "include_global_state": false,
  "metadata": {
    "taken_by": "arun",
    "taken_because": "backup"
  }
}
```


Increase Logging for debug

```
PUT /_cluster/settings
{
  "transient": {
    "logger.cloud.azure" : "DEBUG",
    "logger.repositories.azure" : "DEBUG",
    "logger.org.elasticsearch.snapshots":"DEBUG"
  }
}

```
