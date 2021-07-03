### ELASTICSEARCH-KIBANA DEPLOYMENT USING PLAIN YAMLs

This deployment is special as instead of using default X-PACK plugin for security we are using OPENDISTRO security plugin. The Elastic/Kibana image used for the deployment are customised to add OpenDistro Plugin. Deployment also uses certificates to expose Elastic and Kibana over SSL.

```
Step 1: Update required Certificates and Keys base64 enc value in certs.yaml as per your requirement. I am using self signed for the time.

Step 2: Update base64 enc Azure Storage Accnt and Key value in Elasticsearch YAML. Please note Azure Storage Account and Key, dont put them in double quotes.

Step 3: Make sure Max Virtual Memory is updated on worker nodes
        sysctl -w vm.max_map_count=262144

Step 3: Execute all YAMLs

Step 4: Login in Elaticsearch POD and deploy OpenDistro Security Plugin
```


### Generating Self Signed Certs

```
# Root CA
openssl genrsa -out root-ca-key.pem 2048
openssl req -new -x509 -sha256 -key root-ca-key.pem -out root-ca.pem
# Admin cert
openssl genrsa -out admin-key-temp.pem 2048
openssl pkcs8 -inform PEM -outform PEM -in admin-key-temp.pem -topk8 -nocrypt -v1 PBE-SHA1-3DES -out admin-key.pem
openssl req -new -key admin-key.pem -out admin.csr
openssl x509 -req -in admin.csr -CA root-ca.pem -CAkey root-ca-key.pem -CAcreateserial -sha256 -out admin.pem
# Node cert
openssl genrsa -out node-key-temp.pem 2048
openssl pkcs8 -inform PEM -outform PEM -in node-key-temp.pem -topk8 -nocrypt -v1 PBE-SHA1-3DES -out node-key.pem
openssl req -new -key node-key.pem -out node.csr
openssl x509 -req -in node.csr -CA root-ca.pem -CAkey root-ca-key.pem -CAcreateserial -sha256 -out node.pem

# elk
openssl genrsa -out elastic-key-temp.pem 2048
openssl pkcs8 -inform PEM -outform PEM -in elastic-key-temp.pem -topk8 -nocrypt -v1 PBE-SHA1-3DES -out elastic-key.pem
openssl req -new -key elastic-key.pem -out elastic.csr
openssl x509 -req -in elastic.csr -CA root-ca.pem -CAkey root-ca-key.pem -CAcreateserial -sha256 -out elastic.pem

# Cleanup
rm admin-key-temp.pem
rm admin.csr
rm node-key-temp.pem
rm node.csr
rm elastic.csr elastic-key-temp.pem

```


### Deploying OpenDistro Security Plugin

```
export JAVA_HOME=/usr/share/elasticsearch/jdk; export PATH=$PATH:JAVA_HOME=/usr/share/elasticsearch/jdk/bin; cd /usr/share/elasticsearch/plugins/opendistro_security/tools/; ./securityadmin.sh -cacert /usr/share/elasticsearch/config/root-ca.pem -cert /usr/share/elasticsearch/config/admin.pem -key /usr/share/elasticsearch/config/admin-key.pem -cd /usr/share/elasticsearch/plugins/opendistro_security/securityconfig -nhnv

```