---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-test.html
---

# Test your knowledge base with queries and responses
<a name="knowledge-base-test"></a>

After you set up your knowledge base, you can test its behavior in the following ways:

**Important**
For optimized retrieval accuracy and a managed experience, we recommend [Amazon Bedrock Managed Knowledge Base](kb-build-managed.md).
+ Send queries and retrieving relevant information from your data sources, by using the [[Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html)](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) operation.
+ Send queries and generate responses to the queries based on the retrieved information from your data sources.
+ Use a reranking model to retrieve more relevant sources.
+ Use optional metadata filters to specify which documents in your data source can be used.

When you are satisfied with your knowledge base's behavior, you can then set up your application to query the knowledge base or attach the knowledge base to an agent by proceeding to [Deploy your knowledge base for your AI application](knowledge-base-deploy.md).

The test behavior is different based on functionality available in customer-managed knowledge bases or managed knowledge bases. If you are using managed knowledge bases, for example, you can use agentic retrieval to decompose complex queries into sub-queries and iteratively retrieve relevant information from your data sources, by using the [`AgenticRetrieveStream`](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveStream.html) operation.

Select a topic to learn more about it.

**Topics**
+ [Query a knowledge base and retrieve data](kb-test-retrieve.md)
+ [Test your customer-managed knowledge base](kb-test-self-managed.md)
+ [Test your managed knowledge base with queries and responses](kb-managed-test.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
