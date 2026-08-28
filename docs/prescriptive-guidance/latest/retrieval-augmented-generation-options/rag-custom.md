---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-custom.html
---

# Custom Retrieval Augmented Generation architectures on AWS
<a name="rag-custom"></a>

The previous section describes how to use a fully managed AWS service for Retrieval Augmented Generation (RAG). However, some use cases require more control over the system components, such as the retriever or the LLM (also called the *generator*). For example, you might need the flexibility to choose your own vector database or access an unsupported data source. For these use cases, you can build a custom RAG architecture.

This section contains the following topics:
+ [Retrievers for RAG workflows](rag-custom-retrievers.md)
+ [Generators for RAG workflows](rag-custom-generators.md)

For more information about how to choose between the retriever and generator options in this section, see [Choosing a RAG option](choosing-option.md) in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
