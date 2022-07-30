from sys import argv
import requests

req = requests.get(f"https://crt.sh/?q={argv[1]}&output={argv[2]}")

with open(f"output-{argv[1].split('.')[0]}.txt", "a+") as f:

    for i in range(len(req.json())):
        cn = req.json()[i]["common_name"]
        nv = req.json()[i]["name_value"]

        print(cn)
        print(nv)
        f.writelines(f"{cn}\n")
        f.writelines(f"{nv}\n")

arr = []
with open(f"output-{argv[1].split('.')[0]}.txt","r") as f:
    s = set(line for line in f)
    for i in list(s):
        arr.append(i)

with open(f"unique-{argv[1].split('.')[0]}.txt", "w") as f:
    for i in arr:
        f.write(f"{i}")
