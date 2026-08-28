---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/response-streaming.html
---

# Stream agent responses
<a name="response-streaming"></a>

The following Strands Agents example shows how an AgentCore Runtime agent can stream a response back to a client.

```
from strands import Agent
from bedrock_agentcore import BedrockAgentCoreApp

app = BedrockAgentCoreApp()
agent = Agent()

@app.entrypoint
async def agent_invocation(payload):
    """Handler for agent invocation"""
    user_message = payload.get("prompt", "")
    if not isinstance(user_message, str) or not user_message.strip():
        yield {"error": "Invalid input: 'prompt' must be a non-empty string"}
        return
    stream = agent.stream_async(user_message)
    async for event in stream:
        print(event)
        yield (event)

if __name__ == "__main__":
    app.run()
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
