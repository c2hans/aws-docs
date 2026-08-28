---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/choosing-option.html
---

# Choosing a Retrieval Augmented Generation option on AWS
<a name="choosing-option"></a>

The [Fully managed RAG options](rag-fully-managed.md) and [Custom RAG architectures](rag-custom.md) sections of this guide describe various approaches for building a RAG-based search solution on AWS. This section describes how to select between these options based on your use case. In some situations, more than one option might work. In that scenario, the choice depends on the ease of implementation, skills available in your organization, and your company's policies and standards.

We recommend that you consider the fully managed and custom RAG options in the following sequence and choose the first option that fits your use case:

1. Use [Amazon Q Business](rag-fully-managed-q-business.md) unless:
   + This service is not available in your AWS Region, and your data cannot be moved to a Region where it is available
   + You have a specific reason to customize the RAG workflow
   + You want to use an existing vector database or a specific LLM

1. Use [knowledge bases for Amazon Bedrock](rag-fully-managed-bedrock.md) unless:
   + You have a vector database that is not supported
   + You have a specific reason to customize the RAG workflow

1. Combine [Amazon Kendra](rag-custom-retrievers.md#rag-custom-kendra) with your choice of [generator](rag-custom-generators.md) unless:
   + You want to choose your own vector database
   + You want to customize the chunking strategy

1. If you want more control over the retriever and want to select your own vector database:
   + If you don't have an existing vector database and don't need low latency or graph queries, consider using [Amazon OpenSearch Service](rag-custom-retrievers.md#rag-custom-opensearch).
   + If you have an existing PostgreSQL vector database, consider using the [Amazon Aurora PostgreSQL and pgvector](rag-custom-retrievers.md#rag-custom-aurora) option.
   + If you need low latency, consider an in-memory option, such as [Amazon MemoryDB](rag-custom-retrievers.md#rag-custom-memorydb) or [Amazon DocumentDB](rag-custom-retrievers.md#rag-custom-docdb).
   + If you want to combine vector search with a graph query, consider [Amazon Neptune Analytics](rag-custom-retrievers.md#rag-custom-neptune).
   + If you are already using a third-party vector database or find a specific benefit from one, consider [Pinecone](rag-custom-retrievers.md#rag-custom-pinecone), [MongoDB Atlas](rag-custom-retrievers.md#rag-custom-mongodb-atlas), and [Weaviate](rag-custom-retrievers.md#rag-custom-weaviate).

1. If you want to choose an LLM:
   + If you use Amazon Q Business, you can't choose the LLM.
   + If you use Amazon Bedrock, you can choose one of the [supported foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html).
   + If you use Amazon Kendra or a custom vector database, you can use one of the [generators](rag-custom-generators.md) described in this guide or use a custom LLM.
**Note**
You can also use your custom documents to fine-tune an existing LLM to increase the accuracy of its responses. For more information, see [Comparing RAG and fine-tuning](rag-vs-fine-tuning.md) in this guide.

1. If you have an existing implementation of Amazon SageMaker AI Canvas that you want to use or if you want to compare RAG responses from different LLMs, consider [Amazon SageMaker AI Canvas](rag-fully-managed-sagemaker-canvas.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
