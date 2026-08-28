---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-lake-graphql-api/data-lake-graphql-api.html
---

# Expose Your Data Lake as a GraphQL API
<a name="data-lake-graphql-api"></a>

Publication date: **April 25, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to build a data lake using [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) and share it as a self-documented GraphQL API. You can automatically build the API with a reactive CI/CD pipeline, and allow authorized external clients to query your data lake using GraphQL syntax over HTTPS.

## Expose Your Data Lake as a GraphQL API
<a name="diagram1"></a>

![Architecture diagram showing how to expose a data lake as a GraphQL API using Amazon AppSync, Athena, Lake Formation, and AWS Glue.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-lake-graphql-api/images/data-lake-graphql-api.png)

The following steps describe the architecture:

1. Set up a data lake using Lake Formation and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

1. Crawl the data in the Amazon S3 buckets with [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) to build a data catalog.

1. Monitor any changes in the AWS Glue Data Catalog with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), and trigger an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function on every catalog change to update the schema of the external API.

1. In the Lambda function, query the latest data catalog and security settings, automatically generate source code to build and deploy a new version of the external API's schema and resolvers, and commit the code to AWS CodeCommit.

1. Set up CodeCommit to automatically start a new CI/CD pipeline on AWS CodePipeline after any code commit.

1. Use CodePipeline to build a new version of the API with AWS CodeBuild using the newly generated source code, and use AWS CodeDeploy to deploy both the new [Amazon AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) GraphQL API and the new Lambda query resolvers.

1. Allow your GraphQL clients to securely invoke the external API over HTTPS with your chosen authentication mechanism. Activate the AppSync server-side caching.

1. Use the AppSync Lambda query resolvers to translate the GraphQL query into SQL queries supported by [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html).

1. Run Athena jobs synchronously with the athena-express library, appropriately timing out and limiting the result set.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date |
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | April 25, 2022 |

**Note**
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Reference Architecture Diagrams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query reference-architecture-diagrams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
