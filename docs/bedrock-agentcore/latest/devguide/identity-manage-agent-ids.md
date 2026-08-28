---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-manage-agent-ids.html
---

# Manage workload identities with AgentCore Identity
<a name="identity-manage-agent-ids"></a>

Agent identities in AgentCore Identity are implemented as workload identities with specialized attributes that enable agent-specific capabilities. This approach follows established industry patterns where workloads have granular properties that indicate their specific type and purpose. Unlike traditional service accounts that are tied to specific infrastructure, agent identities are designed to be environment-agnostic and can support multiple authentication credentials simultaneously. The AgentCore Identity directory acts as a centralized registry and management system for all agent identities. For information about workload identity limits, see [AgentCore Identity Service Quotas](bedrock-agentcore-limits.md#identity-service-limits).

**Topics**
+ [Understanding workload identities](understanding-agent-identities.md)
+ [Understanding the agent identity directory](agent-identity-directory.md)
+ [Create and manage workload identities](creating-agent-identities.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
