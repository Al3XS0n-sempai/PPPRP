import requests
import json
import os
import datetime

from pathlib import Path


host: str = os.getenv("SERVER_HOST", default="127.0.0.1")
port: int = int(os.getenv("SERVER_PORT", default="80"))

file_path = Path("/data/client_data")
name_for_file = f"result_{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")}.txt"
filename = str(file_path / name_for_file) if file_path.exists() else name_for_file

print(f"Trying to run with:\n\t{host = }\n\t{port = }")
try:
    r = requests.get(f"http://{host}:{port}/statistics")
except Exception as e:
    print(f"Something went wrong:\n{repr(e)}")
else:
    print(f"Succes")

    print(f"Prechecking file {filename}")
    try:
        with open(filename, "rc") as f:
            print(f"Currentrly contains:\n {f.read()}")
    except:
        print('Empty')

    print(f"Starting to write in file {filename}")
    with open(filename, "w") as f:
        f.write(json.dumps(r.json(), indent=4))

    print(f"Postchecking file {filename}")
    with open(filename, "r") as f:
        print(f"Currentrly contains:\n {f.read()}")

    print(f"Done")