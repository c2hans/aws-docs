---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/rag-br-knowledge.html
---

# Using Amazon Bedrock Knowledge Bases
<a name="rag-br-knowledge"></a>

Amazon Nova Knowledge Bases is a fully managed capability that you can use to implement the entire RAG workflow from ingestion to retrieval and prompt augmentation—without building custom integrations to data sources and managing data flows.

To use Amazon Nova models with Bedrock Knowledge bases, you must first [create a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html) and then [connect to your data repository for your knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/data-source-resource.html). Next, you can [test your knowledge base with queries and responses](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-test.html). Then you're ready to [deploy your knowledge base for your AI application](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-deploy.html).

To customize steps in the process, see [Configure and customize queries and response generation](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html#kb-test-config-prompt-template).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
