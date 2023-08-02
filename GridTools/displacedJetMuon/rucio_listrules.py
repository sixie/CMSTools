import json
from rucio.client import Client
client = Client()
rse = "T2_US_Caltech"
filters = {"account": "t2_us_caltech_local_users"}
for rule in client.list_replication_rules(filters):
    print(rule['name'])
