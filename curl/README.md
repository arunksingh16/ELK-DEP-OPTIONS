

##### cluster health

```
curl -X GET 'localhost:9200/_cluster/health?pretty'
```

##### index 
```
curl -X GET 'localhost:9200/some_index?pretty'
```

##### index create

```
curl -v -XPUT "localhost:9200/some_index" -H 'Content-Type: application/json' -d '
{
  "settings" : {
    "number_of_shards" : 3,
    "number_of_replicas" : 1
  }
}
'
```

