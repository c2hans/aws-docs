---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/agentic-search.html
---

# Agentic search in Amazon OpenSearch Service
<a name="agentic-search"></a>

Starting with OpenSearch version 3.3, agentic search enables an AI-powered process that uses an autonomous agent to execute complex searches on your behalf.

Agentic search introduces an intelligent agent system that understands user intent, orchestrates the right tools, and generates optimized queries. It provides transparent summaries of its decisions through a natural language interface.

With OpenSearch Service, you can configure [AI connectors for AWS services](ml-amazon-connector.md) and [external services](ml-external-connector.md). Using the console, you can also create an ML model with a CloudFormation template that can be used for building your agent. For more information, see [Configuring Agentic Search with Bedrock Claude](cfn-template-agentic-search.md).

For complete documentation and step-by-step implementation, see [Agentic Search](https://docs.opensearch.org/latest/vector-search/ai-search/agentic-search/index/) in the OpenSearch documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
