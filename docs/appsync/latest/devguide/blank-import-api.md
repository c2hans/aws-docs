---
source_url: https://docs.aws.amazon.com/appsync/latest/devguide/blank-import-api.html
---

# Structuring a GraphQL API (blank or imported APIs)
<a name="blank-import-api"></a>

Before you create your GraphQL API from a blank template, it would help to review the concepts surrounding GraphQL. There are three fundamental components of a GraphQL API:

1. The **schema** is the file containing the shape and definition of your data. When a request is made by a client to your GraphQL service, the data returned will follow the specification of the schema. For more information, see [GraphQL schemas](schema-components.md#aws-appsync-schema-components).

1. The **data source** is attached to your schema. When a request is made, this is where the data is retrieved and modified. For more information, see [Data sources](data-source-components.md#aws-appsync-data-source-components).

1. The **resolver** sits between the schema and the data source. When a request is made, the resolver performs the operation on the data from the source, then returns the result as a response. For more information, see [Resolvers](resolver-components.md#aws-appsync-resolver-components).

![GraphQL API architecture showing schema, resolvers, and data sources with AppSync integration.](http://docs.aws.amazon.com/appsync/latest/devguide/images/appsync-architecture-graphql-api.png)

AWS AppSync manages your APIs by allowing you to create, edit, and store the code for your schemas and resolvers. Your data sources will come from external repositories such as databases, DynamoDB tables, and Lambda functions. If you're using an AWS service to store your data or are planning on doing so, AWS AppSync provides a near-seamless experience when associating data from your AWS accounts to your GraphQL APIs.

In the next section, you will learn how to create each of these components using the AWS AppSync service.

**Topics**
+ [Designing your GraphQL schema](designing-your-schema.md)
+ [Attaching a data source](attaching-a-data-source.md)
+ [Configuring AWS AppSync resolvers](resolver-config-overview.md)
+ [Using APIs with the CDK](using-your-api.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
