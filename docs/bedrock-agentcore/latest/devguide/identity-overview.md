---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-overview.html
---

# Overview of Amazon Bedrock AgentCore Identity
<a name="identity-overview"></a>

In the rapidly evolving landscape of AI agents, organizations need robust identity management solutions that can handle the unique challenges associated with non-human identities. Amazon Bedrock AgentCore Identity addresses these challenges by providing a centralized capability for managing agent identities, securing credentials, and enabling seamless integration with AWS and third-party services through Sigv4, standardized OAuth 2.0 flows, and API keys.

The service implements authentication and authorization controls that verify each request independently, requiring explicit verification for all access attempts regardless of source. It integrates seamlessly with AWS services while also enabling agents to securely access external tools and services. Whether you’re building simple automation scripts or complex multi-agent systems, AgentCore Identity provides the identity foundation to help your applications operate securely and efficiently.

**Topics**
+ [Features of AgentCore Identity](key-features-and-benefits.md)
+ [AgentCore Identity terminology](identity-terminology.md)
+ [Example use cases](identity-use-cases.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
