### ELASTICSEARCH-KIBANA DEPLOYMENT USING PLAIN YAMLs

This deployment is special as instead of using default X-PACK plugin for security we are using OPENDISTRO security plugin. The Elastic/Kibana image used for the deployment are customised to add OpenDistro Plugin. 

```
Step 1: Generate required Certificates and Keys base64 enc value in certs.yaml
Step 2: Update base64 enc Azure Storage Accnt and Key value in Elasticsearch YAML
Step 3: Execute all YAMLs
```
