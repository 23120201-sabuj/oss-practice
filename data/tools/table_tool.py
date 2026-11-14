import argparse
import pandas as pd
from rich.console import Console
from rich.table import Table

parser = argparse.ArgumentParser()
parser.add_argument("csv_file", help="Path to the CSV file")
args = parser.parse_args()

# Read the CSV
df = pd.read_csv(args.csv_file)

# My filter: keep only servers that are online AND in asia
filtered = df[(df["status"] == "online") & (df["region"] == "asia")]

# Create a nice table with rich
console = Console()
table = Table(title="Filtered Servers (online + asia)")

table.add_column("Name", style="cyan")
table.add_column("Region", style="magenta")
table.add_column("Status", style="green")
table.add_column("CPU", justify="right")

for _, row in filtered.iterrows():
    table.add_row(row["name"], row["region"], row["status"], str(row["cpu"]))

console.print(table)

# Save the filtered result
filtered.to_excel("filtered_servers.xlsx", index=False)
print("Saved filtered_servers.xlsx")
