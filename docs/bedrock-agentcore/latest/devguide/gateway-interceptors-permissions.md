---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors-permissions.html
---

# Permissions for interceptors
<a name="gateway-interceptors-permissions"></a>

When configuring interceptors, your gateway service role must have the lambda:InvokeFunction IAM permissions to invoke the Lambda functions that serve as interceptors. The service role needs specific permissions to execute interceptor functions during request and response processing.

For detailed information about configuring the required permissions for your gateway service role, including permissions to Lambda, see [Gateway service role permissions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-prerequisites-permissions.html#gateway-service-role-permissions).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
