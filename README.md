# ELK_Deployment_Options





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
