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
