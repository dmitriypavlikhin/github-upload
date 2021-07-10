import requests
import json

url = 'https://ops-api-winter-s3.tom.takeoff.com/api/v1/order/search/search/'
headers = {'Content-type': 'application/json',
           'Accept': 'application/json',
           'X-Serial': '0',
           'X-Lang': 'en',
           'X-Token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjhhMzY5M2YxMzczZjgwYTI1M2NmYmUyMTVkMDJlZTMwNjhmZWJjMzYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiWWVseXphdmV0YSBQb2xpc2hjaHVrIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3dpbnRlci1zMy1pbnRlcm5hbC1hdXRoIiwiYXVkIjoid2ludGVyLXMzLWludGVybmFsLWF1dGgiLCJhdXRoX3RpbWUiOjE1NzQxODIzOTEsInVzZXJfaWQiOiJ4TVp5aW53MkhCZFZLN0tlbENXRWZXVU1YZloyIiwic3ViIjoieE1aeWludzJIQmRWSzdLZWxDV0VmV1VNWGZaMiIsImlhdCI6MTU3NDE4MjM5MSwiZXhwIjoxNTc0MTg1OTkxLCJlbWFpbCI6InllbHl6YXZldGEucG9saXNoY2h1a0B0YWtlb2ZmLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJ5ZWx5emF2ZXRhLnBvbGlzaGNodWtAdGFrZW9mZi5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.D9bqim4dP6JrHkSNP-6CmWCe2OFk1KzOnnvHbiUXepDRAunn7gLciDjhY2tlMsOD_Q3b_3JnpfwDBXc4GFxSAZPBCeDrFBAuztqZJIdtG2P1qeG0TRHYDKzff5xahIAbN-dulGpuQMZuFvwBDJhsMd26mH_nOxEeYcx5Evc8WzuRcF2q7bdoEtkG-V_Pyt-IRoURHeQJWsj78lKQNeZ373UKO94UECTzOT2Ub02GeNEGtP7Naq5pRfEamw9q0yFg_1YRwgbP1rVAMNFgK6pqGqC_Qa2nf_bZaumVUchWQ2Tw5ICUdoEl4O0DX3GY4CU0NB5kqgERl1BZwIyt9LR-ug'}

data = {
    "page": 1,
    "filter": {
        "status": ["ready"]
    }
}

answer = requests.post(url, data=json.dumps(data), headers=headers)
response = answer.json()

for order in response["orders"]:
    oid = order["order_id"]
    opsurl = 'https://ops-api-winter-s3.tom.takeoff.com/api/v1/picking-session/' + oid + '/status/'
    opsdata = {
        "status": "served",
        "created": "2019-11-22T22:24:09Z"
    }
    opsanswer = requests.put(opsurl, data=json.dumps(opsdata), headers=headers)
    opsresponse = opsanswer.json()
    print(opsresponse)
