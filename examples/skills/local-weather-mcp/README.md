# Local Weather MCP Server (Python)

This example provides a local MCP server with one tool:

- `check_weather(city: str, unit: "c" | "f" = "c")`

It uses a local mock dataset so you can test MCP behavior without external APIs.

## Run

```bash
cd examples/skills/local-weather-mcp
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python server.py
```

## VS Code MCP configuration

Use [`copilot-mcp-settings.good.json`](./copilot-mcp-settings.good.json) as your template for `.vscode/settings.json`.

## Prompt patterns

Good pattern:

> Use `check_weather` with city `Nairobi` and unit `f`. Return only city, temperature, condition.

Bad pattern:

> Check weather anywhere and give me whatever.
