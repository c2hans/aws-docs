---
source_url: https://docs.aws.amazon.com/appsync/latest/devguide/api-components.html
---

# Components of a GraphQL API
<a name="api-components"></a>

A standard GraphQL API is composed of a single schema that handles the shape of the data that will be queried. Your schema is linked to one or more of your data sources like a database or Lambda function. In between the two sits one or more resolvers that handle the business logic for your requests. Each component plays an important role in your GraphQL implementation. The following sections will introduce these three components and the role they play in the GraphQL service.

![GraphQL API architecture showing schema, resolvers, and data sources connected by arrows.](http://docs.aws.amazon.com/appsync/latest/devguide/images/appsync-architecture-graphql-api.png)

**Topics**
+ [GraphQL schemas](schema-components.md)
+ [Data sources](data-source-components.md)
+ [Resolvers](resolver-components.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
