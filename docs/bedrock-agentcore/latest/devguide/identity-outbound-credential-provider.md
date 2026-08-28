---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-outbound-credential-provider.html
---

# Manage credential providers with AgentCore Identity
<a name="identity-outbound-credential-provider"></a>

Credential management is a core feature of Amazon Bedrock AgentCore Identity that addresses the complex challenge of securely storing, retrieving, and managing credentials across multiple trust domains and authentication systems. The service implements defense-in-depth security measures to protect sensitive authentication tokens, API keys, and certificates while providing agents with efficient access to the credentials they need for authorized operations. AgentCore Identity’s credential management architecture separates credential storage from credential access, helping to ensure that agents never have direct access to long-term secrets or refresh tokens.

The credential management system supports multiple credential types including OAuth2 access tokens, API keys, client certificates, SAML assertions, and custom authentication tokens. Each credential type has specific handling requirements for storage encryption and access patterns. All credential operations are logged and audited to provide complete visibility into credential usage and access patterns.

Integration with the Resource Credential Provider enables AgentCore Identity to support cross-capability credential vending, where agents can access resources across different cloud providers, SaaS applications, and enterprise systems using a unified credential management interface. The system maintains proper security boundaries while enabling necessary functionality, with comprehensive monitoring and alerting capabilities that detect unusual credential usage patterns or potential security threats.

**Topics**
+ [Supported authentication patterns](common-use-cases.md)
+ [Client authentication methods](client-auth-methods.md)
+ [Configure credential provider](resource-providers.md)
+ [Obtain credentials](obtain-credentials.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
