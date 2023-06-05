import requests
import os
import json

ORGANIZATION = "cepdnaclk"

def urlOrganizationRepos(pageNo):
    return "https://api.github.com/orgs/{0}/repos?page={1}".format(ORGANIZATION, pageNo)

# r = requests.get(url="https://api.github.com/orgs/{0}".format(ORGANIZATION))
# j = r.json()

# repos = []

# for p in range(1, 1000):
#     r = requests.get(url=urlOrganizationRepos(p))
#     jsonData = r.json()

#     repos.extend(jsonData)

#     print("Page:{0}, Repos: {1}, Total:{2}".format(
#         p, len(jsonData), len(repos)))

#     if len(jsonData) == 0:
#         break


filename = "./backup/repos.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write(json.dumps(repos, indent=4))


url = './backup/repos.json'
with open(url, 'r') as f:
    repos = json.load(f)

counter = 0
script_file = []

for r in repos:
    repo_url = r['html_url']
    repo_name = r['name']
    path = "./backup/{}".format(repo_name)

    counter += 1
    if os.path.exists(path):
        script_file.append("cd {} && git pull".format(path))
        # os.system("cd {} && git pull".format(path))
    else:
        script_file.append("git clone {}".format(repo_url))
        #  os.system("cd './backup/' && git clone {}".format(repo_url))

    if counter > 5:
        break


execute_file = "./backup/execute.sh"
os.makedirs(os.path.dirname(execute_file), exist_ok=True)
f = open(execute_file, "w")
f.write("\n".join(script_file))
