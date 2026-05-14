from tabulate import tabulate
from pathlib import Path

def generate_report(version, targets):
    Path("reports").mkdir(exist_ok=True)

    table = [[idx + 1, t] for idx, t in enumerate(targets)]

    content = []
    content.append("sl_viewer Scan Report")
    content.append("")
    content.append(f"Detected Package: {version}")
    content.append("")
    content.append(
        tabulate(
            table,
            headers=["ID", "Target"],
            tablefmt="grid"
        )
    )

    with open("reports/report.txt", "w") as f:
        f.write("\n".join(content))
