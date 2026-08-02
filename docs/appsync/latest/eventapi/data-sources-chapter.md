---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/data-sources-chapter.html
---

# Working with data sources for AWS AppSync Event APIs
<a name="data-sources-chapter"></a>

Data sources are resources in your AWS account that AWS AppSync Events can interact with. AWS AppSync supports multiple data sources including AWS Lambda, Amazon DynamoDB, Amazon Aurora Serverless, Amazon OpenSearch Service, and HTTP endpoints. An AWS AppSync Events API can be configured to interact with multiple data sources, enabling you to process and route events efficiently.

Once you have configured a data source, you can use it as an integration in your namespaces. This allows you to interact with your data sources from your channel namespace handlers. For example, you can save events to a DynamoDB table as they are published, before they are broadcast. You can trigger a Lambda function asynchronously in response to a publish to start a processing job. You can check user information in an Amazon RDS Aurora PostgreSQL table as clients try to subscribe to a channel.

**Topics**
+ [Supported data sources](supported-datasources.md)
+ [Adding a data source](adding-a-data-source.md)
