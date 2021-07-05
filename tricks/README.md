### Day to day tips and tricks for managing Elasticsearch


If you are frustrated with deprecation logging warnings!

```
# transient
PUT /_cluster/settings
{
  "transient" : {
    "logger.org.elasticsearch.deprecation" : "ERROR"
  }
}

# persistent
PUT /_cluster/settings
{
  "persistent" : {
    "logger.deprecation.level" : "ERROR"
  }
}

```
