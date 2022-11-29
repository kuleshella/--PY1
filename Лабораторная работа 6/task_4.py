import json
from pathlib import Path

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=',', new_line='\n') -> list[dict]:
    def record_to_dict(column_names: list[str], record: list[str]) -> dict:
        return {column_names[i]: record[i] for i in range(len(column_names))}

    csv_lines = Path(filename).read_text().split(new_line)
    column_names = csv_lines[0].split(delimiter)
    return [record_to_dict(column_names, line.split(delimiter)) for line in csv_lines[1:]]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
