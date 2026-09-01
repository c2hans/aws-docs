---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ddb-and-amazon-bedrock.html
---

# Leveraging DynamoDB Zero-ETL integration with OpenSearch Service
<a name="ddb-and-amazon-bedrock"></a>

You can use Amazon Bedrock with DynamoDB to provide serverless access to [foundational models (FMs)](https://aws.amazon.com/what-is/foundation-models/), such as Amazon Titan and other third-party models. For vector search on data in DynamoDB, you can use native vector indexes (see [Using vector indexes in DynamoDB](VectorSearch.md)). If you also want full-text search, analytics, or hybrid search capabilities alongside vector search, you can leverage the Zero-ETL integration with Amazon OpenSearch Service when building generative AI applications. The [Generative AI with DynamoDB zero-ETL to OpenSearch integration and Amazon Bedrock](https://catalog.workshops.aws/dynamodb-labs/en-US/dynamodb-opensearch-zetl) workshop provides you hands-on experience in setting up DynamoDB Zero-ETL integration with OpenSearch. This workshop does the following tasks:
+ Creates a pipeline from your DynamoDB table to OpenSearch.
+ Creates an Amazon Bedrock Connector in OpenSearch.
+ Queries Amazon Bedrock leveraging OpenSearch as a vector store.
+ Uses the Claude FM in Amazon Bedrock to create a written response in plain English explaining the search results returned by OpenSearch.

This workshop enables you to integrate DynamoDB with OpenSearch to build generative AI applications. It also demonstrates the flexible querying capability across database engines to help you integrate DynamoDB and OpenSearch for traditional use cases. This workshop is one of the seven modules in the [Amazon DynamoDB Immersion Day](https://catalog.workshops.aws/dynamodb-labs/en-US). You can run this workshop in any AWS account.

You can also refer to the following blog post about how to set up a Zero-ETL integration between DynamoDB and OpenSearch Service. This blog post also describes how to set up model connectors in OpenSearch Service to automatically generate embeddings using Amazon Bedrock for incoming data. [Vector search for Amazon DynamoDB with zero ETL for Amazon OpenSearch Service](https://aws.amazon.com/blogs/database/vector-search-for-amazon-dynamodb-with-zero-etl-for-amazon-opensearch-service/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
