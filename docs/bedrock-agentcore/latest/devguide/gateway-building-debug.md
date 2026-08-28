---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-debug.html
---

# Debug and assess your gateway
<a name="gateway-building-debug"></a>

You can use different tools to help debug your gateway before putting it into a production environment, including built-in AWS and AgentCore Gateway tools, as well as external tools such as the MCP inspector.

You can also debug, monitor, troubleshoot, and assess your gateway’s performance and tool integrations with the help of Amazon CloudWatch. To learn more, see [AgentCore generated gateway observability data](observability-gateway-metrics.md).

The following topics provide more details about different methods that you can use to debug your gateway:

**Topics**
+ [Turn on debugging messages](gateway-debug-messages.md)
+ [Use the MCP Inspector](gateway-using-inspector.md)
+ [Log Amazon Bedrock AgentCore Gateway API calls with CloudTrail](gateway-cloudtrail.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
