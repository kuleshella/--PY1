import json
from pathlib import Path

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=',', newline='\n') -> list[dict]:
    with open(filename, mode='r', newline=newline) as output:
        headers = next(output).rstrip(newline).split(delimiter)
        return [
            {headers[n]: it.rstrip(newline) for n, it in enumerate(line.rstrip(newline).split(delimiter))}
            for line in output
        ]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
