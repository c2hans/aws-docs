---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-test.html
---

# Test your managed knowledge base with queries and responses
<a name="kb-managed-test"></a>

After you set up your managed knowledge base, you can test its behavior in the following ways:
+ Retrieve relevant information from your data sources, by using the [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) operation.
+ Use agentic retrieval to decompose complex queries into sub-queries and iteratively retrieve relevant information from your data sources, by using the `AgenticRetrieveStream` operation.
+ Connect to your knowledge base through AgentCore Gateway to expose it as an MCP tool.

Select a topic to learn more about it.

**Topics**
+ [ACL-aware retrieval on managed knowledge bases](kb-test-retrieve-acl.md)
+ [Retrieve the content of documents from knowledge base](kb-test-get-document-content.md)
+ [Use agentic retrieval to query a knowledge base](kb-test-agentic-retrieve.md)
+ [Configure and customize queries for managed knowledge bases](kb-managed-test-config.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
