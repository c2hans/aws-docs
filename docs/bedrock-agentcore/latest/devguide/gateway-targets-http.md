---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-targets-http.html
---

# HTTP targets
<a name="gateway-targets-http"></a>

For HTTP targets, the gateway sends traffic directly to the target without aggregation or protocol translation. Unlike MCP targets, HTTP targets do not support capability synchronization or semantic tool search. Clients address each target individually through path-based routing.

The following topics describe the HTTP target types that you can add to your gateway.

**Topics**
+ [Amazon Bedrock AgentCore Runtime targets](gateway-target-http-runtime.md)
+ [HTTP passthrough targets](gateway-target-http-passthrough.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
