---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-memory-long-term.html
---

# Use long-term memory
<a name="long-term-memory-long-term"></a>

Long-term memory is enabled by adding one or more memory strategies to a memory resource. These strategies define what kind of information is extracted from conversations and stored persistently. This section guides you through configuring built-in and built-in with overrides strategies to enable long-term memory for your agent.

This section provides examples using the AWS SDK (Boto3). For complete end-to-end examples, see [Amazon Bedrock AgentCore Memory examples](memory-examples.md).

**Topics**
+ [Enable long-term memory](long-term-enabling-long-term-memory.md)
+ [Specify long-term memory organization with namespaces](specify-long-term-memory-organization.md)
+ [Configure built-in strategies](long-term-configuring-built-in-strategies.md)
+ [Configure a custom strategy](long-term-configuring-custom-strategies.md)
+ [Ingest content into long-term memory](long-term-ingest-data.md)
+ [Save and retrieve insights](long-term-saving-and-retrieving-insights.md)
+ [Retrieve memory records](long-term-retrieve-records.md)
+ [List memory records](long-term-list-memory-records.md)
+ [Structured metadata for long-term memories](long-term-memory-metadata.md)
+ [Delete memory records](long-term-delete-memory-records.md)
+ [Redrive failed ingestions](long-term-redrive.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
