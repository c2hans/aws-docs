---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/obtain-api-key.html
---

# Obtain API key
<a name="obtain-api-key"></a>

Once you have stored your API keys in the AgentCore Identity vault, you can retrieve them directly in your agent using the AgentCore SDK and the `@requires_api_key` annotation. For example, the code below will retrieve the API key from the “your-service-name” API key provider so that you can use it in the `need_api_key` function.

```
import asyncio
from bedrock_agentcore.identity.auth import requires_api_key

@requires_api_key(
    provider_name= "your-service-name" # replace with your own credential provider name
)
async def need_api_key(*, api_key: str):
    # Use the API key
    pass

# To invoke:
# asyncio.run(need_api_key())
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
