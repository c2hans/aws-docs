---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html
---

# Choosing an AWS vector database for RAG use cases
<a name="introduction"></a>

*Mayuri Shinde, Ivan Cui, and Anand Bukkapatnam Tirumala, Amazon Web Services*

Vector databases are becoming increasingly important for organizations that implement generative AI applications. These databases store and manage *vectors*, which are numerical representations of data that enable processing of text, images, and other content in ways that capture their meaning and relationships.

As organizations explore vector database options on AWS they need to understand the capabilities, trade-offs, and best practices for different solutions. This guide helps you compare commonly used vector stores on AWS and make informed decisions about which options best suit your specific needs or [use case](use-cases.md). Whether you're implementing retrieval augmented generation (RAG), building recommendation systems, or developing other AI applications, this guide provides a framework to help you evaluate and choose a vector database solution.

## Intended audience
<a name="audience"></a>

This guide is intended for people in these roles:
+ Data scientists and machine learning (ML) engineers who use vector databases to store and retrieve high-dimensional data for ML models.
+ Data engineers who design and implement data pipelines that include vector databases for storing and processing high-dimensional data.
+ MLOps engineers who use vector databases as part of the ML pipeline to store and serve model outputs or intermediate representations.
+ Software engineers who integrate vector databases into applications that require similarity search or recommendation systems.
+ DevOps engineers who are responsible for deploying and maintaining vector databases in production environments, ensuring scalability and reliability.
+ AI researchers who use vector databases to store and analyze large datasets of embeddings or feature vectors.
+ AI product managers who need to understand the capabilities and limitations of vector databases to make informed decisions about product features and architecture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
