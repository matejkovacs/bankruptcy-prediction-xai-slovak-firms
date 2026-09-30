"""Compile public notebook cells and require clean outputs; no model execution."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
cell_count = 0
notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
if not notebooks:
    errors.append("No notebooks found")
for path in notebooks:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    if notebook.get("nbformat") != 4:
        errors.append(f"{path.name}: expected notebook format 4")
    for index, cell in enumerate(notebook["cells"], 1):
        if cell["cell_type"] != "code":
            continue
        source = cell["source"]
        source = "".join(source) if isinstance(source, list) else source
        cell_count += 1
        try:
            compile(source, f"{path.name}:cell-{index}", "exec")
        except SyntaxError as exc:
            errors.append(str(exc))
        if cell.get("outputs"):
            errors.append(f"{path.name}:cell-{index}: saved outputs present")
        if cell.get("execution_count") is not None:
            errors.append(f"{path.name}:cell-{index}: execution count present")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(notebooks)} notebooks, {cell_count} code cells compiled; outputs cleared.")
print("Static checks only: model execution, dependencies and empirical results are not verified.")
