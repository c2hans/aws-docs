---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/security-best-practices-for-tool-integration.html
---

# Security best practices for tool integration
<a name="security-best-practices-for-tool-integration"></a>

Tool integration directly impacts your security posture. This section outlines best practices to consider for your organization.

## Authentication and authorization
<a name="authentication-and-authorization.b010bc85-7169-5338-a7ad-d7e4e03482bd"></a>

Make use of the following robust access controls:
+ **Use OAuth 2.0/2.1** – Implement industry-standard authentication for remote tools.
+ **Implement least privilege** – Grant tools only the permissions they need.
+ **Rotate credentials** – Regularly update API keys and access tokens.

## Data protection
<a name="data-protection.c4b4f471-f6b8-5176-bad2-880a89ea743f"></a>

To help safeguard data, adopt the following measures:
+ **Validate inputs and outputs** – Implement schema validation for all tool interactions.
+ **Encrypt sensitive data** – Use TLS for all remote tool communications.
+ **Implement data minimization** – Only pass necessary information to tools.

## Monitoring and auditing
<a name="monitoring-and-auditing.9fd5cd3f-a027-5934-a850-08d5b96400bc"></a>

Maintain visibility and control by using these mechanisms:
+ **Log all tool invocations** – Maintain comprehensive audit trails.
+ **Monitor for anomalies** – Detect unusual tool usage patterns.
+ **Implement rate limiting** – Prevent abuse through excessive tool calls.

The Model Context Protocol (MCP) security model addresses these concerns comprehensively. For more information, see [Security considerations](https://modelcontextprotocol.io/docs/concepts/architecture#security-considerations) in the MCP documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
