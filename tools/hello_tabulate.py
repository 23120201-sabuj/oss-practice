import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True, help="Your name")
args = parser.parse_args()

data = [
    ["Name", args.name],
    ["Student ID", "23120201"],
    ["Library", "tabulate"],
    ["Message", "Hello from Chapter 8!"]
]

print(tabulate(data, headers=["Field", "Value"], tablefmt="grid"))
