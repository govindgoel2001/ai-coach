# Tool Map

This file defines the user's current data sources. The coach should use only connected/authorized data.

| Tool / data | Mode | Provides | Freshness | Allowed actions |
| --- | --- | --- | --- | --- |
| Wearable export | file/API/MCP | sleep, HRV, resting HR, steps | daily | read only |
| Portfolio | file/API/MCP | holdings, allocation, returns, risk | live/daily | read only |
| Calendar/tasks | API/MCP | commitments, deep work, deadlines | live | read; write with approval |
| Business analytics | file/API/MCP | revenue, leads, conversion, content | daily | read only |

## Guardrail
External writes (sending messages, changing budgets, trading, publishing) require explicit approval unless the user has created a separate approved automation policy.
