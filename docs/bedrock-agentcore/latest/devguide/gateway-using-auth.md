---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-auth.html
---

# Authorize and authenticate to an AgentCore gateway and gateway target
<a name="gateway-using-auth"></a>

To invoke your gateway and gateway target, you’ll need to make sure that the following credentials that you set up while fulfilling the [prerequisites](gateway-prerequisites.md) are recognized during gateway invocation:
+  [Inbound authorization](gateway-inbound-auth.md) – Authorization and authentication to the gateway.
+  [Outbound authorization](gateway-outbound-auth.md) – Authorization and authentication to the gateway target.

To learn how to obtain and configure credentials, review the provider documentation for the methods that you choose.

The following sections provide examples of obtaining and configuring credentials for different use cases.

**Topics**
+ [Example: Authorization for the default gateway and target created by the AgentCore CLI](gateway-using-auth-ex-starter.md)
+ [Example: Authentication with an authorization code grant when invoking a gateway](gateway-using-auth-ex-3lo.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
