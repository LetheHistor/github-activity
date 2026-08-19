import requests

def pr(exp):
    prr = exp["payload"]["action"]
    return f"{prr}"
    
def p(exp):
    commits = len(exp["payload"].get("commits", []))
    return f"Pushed {commits} commit(s)"

def c(exp):
    btr = exp["payload"]["ref_type"]
    return f"{btr}"

def ic(exp):
    title = exp["payload"]["issue"]["title"]
    return f"{title}"
    
def r(exp):
    tagName = exp["payload"]["release"]["tag_name"]
    return f"{tagName}"

DISPATCH_TABLE = {
    "PullRequestEvent": pr,
    "IssuesEvent": pr,
    "PullRequestReviewCommentEvent": pr,
    "PullRequestReviewEvent": pr,
    "PushEvent": p,
    "CreateEvent": c,
    "DeleteEvent": c,
    "IssueCommentEvent": ic,
    "ReleaseEvent": r,
}
user = input("Enter github username: ")
response = requests.get(f"https://api.github.com/users/{user}/events")
if response.status_code == 200:
    rjson = response.json()
    for i, exp in enumerate(rjson, 1):
        eventType = exp["type"]
        repoName = exp["repo"]["name"]
        handler_function = DISPATCH_TABLE.get(eventType)
        if handler_function:
            extra = handler_function(exp)
            print(f"{i}. {eventType} | {repoName} | {extra}")
        else:
            print(f"{i}. {eventType} | {repoName}")
        print("--------------------")
else:
    print(f"Error fetching activity. Status code: {response.status_code}")
input("\nPress Enter to exit.")
