---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-fully-managed.html
---

# Fully managed Retrieval Augmented Generation options on AWS
<a name="rag-fully-managed"></a>

To manage Retrieval Augmented Generation (RAG) workflows on AWS, you can use custom RAG pipelines or use some of the fully managed services capabilities that AWS offers. Because they include many of the core components of a RAG-based system, fully managed services can help you manage some of the undifferentiated heavy lifting. However, these services provide less opportunity for customization.

The fully managed AWS services use connectors to ingest data from external data sources, such as websites, Atlassian Confluence, or Microsoft SharePoint. The supported data sources vary by AWS service.

This section explores the following fully managed options for building RAG workflows on AWS:
+ [Knowledge bases for Amazon Bedrock](rag-fully-managed-bedrock.md)
+ [Amazon Q Business](rag-fully-managed-q-business.md)
+ [Amazon SageMaker AI Canvas](rag-fully-managed-sagemaker-canvas.md)

For more information about how to choose between these options, see [Choosing a RAG option](choosing-option.md) in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
