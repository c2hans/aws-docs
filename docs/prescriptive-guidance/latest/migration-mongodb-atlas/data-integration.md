---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/data-integration.html
---

# Streamlined data integration with AWS AppSync
<a name="data-integration"></a>

Integrating MongoDB Atlas with [AWS AppSync](https://aws.amazon.com/pm/appsync/)provides seamless data synchronization, real-time interactions, and dynamic, responsive user experiences. The following diagram shows an example implementation.

![Integrating MongoDB Atlas with AWS AppSync for data synchronization.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/images/guide-img/2acef6bf-a074-43c2-a021-70385dda418f/images/0d7bd1bb-9d50-4812-9cdc-0199eb129bd5.png)

Key highlights:
+ A unified GraphQL endpoint for multiple data sources
+ Sub-graphs managed independently
+ End-to-end serverless architecture
+ Conflict resolution by using schema directives
+ Automatic scaling based on API request volumes

For more information, see the blog post [How to Build Advanced GraphQL-based APIs With MongoDB Atlas and AWS AppSync Merged APIs](https://www.mongodb.com/blog/post/how-build-advanced-graphql-based-apis-mongodb-atlas-aws-appsync-merged-apis) on the MongoDB website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
