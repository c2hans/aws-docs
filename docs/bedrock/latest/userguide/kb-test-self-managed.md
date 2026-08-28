---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-self-managed.html
---

# Test your customer-managed knowledge base
<a name="kb-test-self-managed"></a>

After you set up your customer-managed knowledge base, you can test its behavior in the following ways:
+ Send queries and generate responses to the queries based on the retrieved information from your data sources, by using the [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html) operation.
+ Generate a query for structured data sources.
+ Query a knowledge base connected to an Amazon Kendra GenAI index.
+ Query a knowledge base connected to an Amazon Neptune Analytics graph.
+ Configure and customize queries and response generation.
+ Configure response generation for reasoning models.

Select a topic to learn more about it.

**Topics**
+ [Query a knowledge base and generate responses based off the retrieved data](kb-test-retrieve-generate.md)
+ [Generate a query for structured data](knowledge-base-generate-query.md)
+ [Query a knowledge base connected to an Amazon Kendra GenAI index](kb-test-kendra.md)
+ [Query a knowledge base connected to an Amazon Neptune Analytics graph](kb-test-neptune.md)
+ [Configure and customize queries and response generation](kb-test-config.md)
+ [Configure response generation for reasoning models with Knowledge Bases](kb-test-configure-reasoning.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
