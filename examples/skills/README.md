# Example Skill Definitions

This directory contains example skill (tool) definitions for use with the
[Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

Each file illustrates how to describe a custom skill so that an agent
can call it correctly.

---

## Files

| File | Description |
|------|-------------|
| [`jira-skill.json`](./jira-skill.json) | Creates and queries Jira tickets |
| [`slack-notifier.json`](./slack-notifier.json) | Sends Slack messages |
| [`database-query.json`](./database-query.json) | Executes read-only SQL queries |
| [`local-weather-mcp/`](./local-weather-mcp/) | Runnable local Python MCP server with one `check_weather` skill |

---

## How to Register a Custom Skill

1. Create a JSON file following the MCP tool definition schema (see examples).
2. Set up an MCP server that implements the skill's handler.
3. Register the MCP server in `.vscode/settings.json`:

```json
{
  "github.copilot.chat.mcpServers": {
    "my-tools": {
      "command": "node",
      "args": ["./mcp-server/index.js"],
      "env": {}
    }
  }
}
```

4. Declare the skill name in your agent file's `tools:` list.

---

## Local Python MCP Example (`check_weather`)

This repository includes a runnable local MCP server:

- Server: [`local-weather-mcp/server.py`](./local-weather-mcp/server.py)
- Dependency list: [`local-weather-mcp/requirements.txt`](./local-weather-mcp/requirements.txt)
- Good config example: [`local-weather-mcp/copilot-mcp-settings.good.json`](./local-weather-mcp/copilot-mcp-settings.good.json)
- Bad config example: [`local-weather-mcp/copilot-mcp-settings.bad.json`](./local-weather-mcp/copilot-mcp-settings.bad.json)

### Run locally

```bash
cd examples/skills/local-weather-mcp
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python server.py
```

### Good prompt pattern

> Use `check_weather` with city `Tokyo` and unit `c`. Return only city, temperature, and condition.

### Bad prompt pattern

> Weather please.
