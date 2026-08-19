import requests


user = input()
response = requests.get(f"https://api.github.com/users/{user}/events")
print(response.status_code)
rjson = response.json()
for i, exp in enumerate(rjson, 1):
    eventType = exp["type"]
    repoName = exp["repo"]["name"]
    if eventType == "PullRequestEvent":
        pr = exp["payload"]["pull_request"]["head"]["repo"]["name"]
        print(f"{i}. {eventType} | {repoName} | {pr}")
    elif eventType == "PushEvent":
        print(f"{i}. {eventType} | {repoName}")
    print("--------------------")
stall = input()