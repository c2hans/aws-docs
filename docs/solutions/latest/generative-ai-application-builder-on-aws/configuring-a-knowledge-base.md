---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/configuring-a-knowledge-base.html
---

# Configuring a knowledge base
<a name="configuring-a-knowledge-base"></a>

This section describes how to ingest data into the knowledge base you’ve selected for the solution. The solution currently supports Amazon Kendra and Amazon Bedrock Knowledge Bases as knowledge bases for your RAG-based use case deployment.

 **Amazon Kendra**

If you’re using Amazon Kendra as your knowledge base, refer to the [Amazon Kendra Developer Guide](https://docs.aws.amazon.com/kendra/latest/dg/data-source.html) for information on how to use various data source connectors to help you ingest data from a wide selection sources.

Important: To prevent accidental data loss, the solution does not automatically delete the Kendra index (whether created by the solution or otherwise) when a deployment or stack is deleted. If you want to delete your knowledge base and stop incurring costs, see the [Manual uninstall](uninstall-the-solution.md) section for details on which resources are retained and how to clean them up.

 **Amazon Bedrock Knowledge Bases**

Amazon Bedrock Knowledge Bases can be backed by a variety of different vector stores, each with the capability of indexing your data. To set up and populate your knowledge base, consult the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html). Specifically, you will want to:
+ First [set up your data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html)
+ Then [set up a vector index for your knowledge base in a supported vector store](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html). Note that this can be skipped if you use the "Quick create a new vector store" option in Bedrock console during knowledge base creation.
+ Finally, you can [create the knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html) and [sync your configured data sources](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ingest.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
