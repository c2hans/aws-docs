---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/obtain-credentials.html
---

# Obtain credentials
<a name="obtain-credentials"></a>

AgentCore Identity uses a workload access token to authorize agent access to credentials stored in the vault, and this token contains both the identity of the agent and the identity of the end user on whose behalf the agent is working. AgentCore Runtime will automatically provide a token when invoking an agent that it is hosting. Agents hosted on other systems can retrieve their agent token using the AgentCore SDK.

**Topics**
+ [Get workload access token](get-workload-access-token.md)
+ [Obtain OAuth 2.0 access token](identity-authentication.md)
+ [OAuth 2.0 authorization URL session binding](oauth2-authorization-url-session-binding.md)
+ [Scope down access to credential providers by workload identity](scope-credential-provider-access.md)
+ [Obtain API key](obtain-api-key.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
