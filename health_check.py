import json
import time
import requests

i = 0
# The script will run for 100 seconds 
while i in range(100):
    time.sleep(1)
    results_loop = requests.get("http://localhost:9200/_cluster/health",headers={'Metadata': 'true'},)
    #results_loop = requests.get("https://localhost:9201/_cluster/health",headers={'Authorization': 'Basic xxxxbase64-encxxxx'},verify=False)
    jdata = json.loads(results_loop.text)
    els_name = jdata["cluster_name"]
    els_health = jdata["status"]
    i = i+1
    print(f"Waiting Since {i} secs")
    if els_health == "green":
        print("Cluster is green ! Exiting")
        exit(0)
print("Fix Your Cluster")
exit(1)
