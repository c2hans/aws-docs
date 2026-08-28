---
source_url: https://docs.aws.amazon.com/appsync/latest/devguide/tutorials-js.html
---

# JavaScript resolver tutorials for AWS AppSync
<a name="tutorials-js"></a>

Data sources and resolvers are used by AWS AppSync to translate GraphQL requests and fetch information from your AWS resources. AWS AppSync supports automatic provisioning and connections with certain data source types. AWS AppSync also supports AWS Lambda, Amazon DynamoDB, relational databases (Amazon Aurora Serverless), Amazon OpenSearch Service, and HTTP endpoints as data sources. You can use a GraphQL API with your existing AWS resources or build data sources and resolvers from scratch. The following sections are meant to elucidate some of the more common GraphQL use cases in the form of tutorials.

**Topics**
+ [Creating a simple post application using DynamoDB JavaScript resolvers](tutorial-dynamodb-resolvers-js.md)
+ [Using AWS Lambda resolvers](tutorial-lambda-resolvers-js.md)
+ [Using local resolvers](tutorial-local-resolvers-js.md)
+ [Combining GraphQL resolvers](tutorial-combining-graphql-resolvers-js.md)
+ [Using OpenSearch Service resolvers](tutorial-elasticsearch-resolvers-js.md)
+ [Performing DynamoDB transactions](tutorial-dynamodb-transact-js.md)
+ [Using DynamoDB batch operations](tutorial-dynamodb-batch-js.md)
+ [Using HTTP resolvers](tutorial-http-resolvers-js.md)
+ [Using Aurora PostgreSQL with Data API](aurora-serverless-tutorial-js.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
