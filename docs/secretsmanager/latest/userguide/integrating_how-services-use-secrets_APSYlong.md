---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_APSYlong.html
---

# How AWS AppSync uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_APSYlong"></a>

AWS AppSync provides a robust, scalable GraphQL interface for application developers to combine data from multiple sources, including Amazon DynamoDB, AWS Lambda, and HTTP APIs.

AWS AppSync uses the credentials in a Secrets Manager secret to connect to Amazon RDS and Aurora. For more information, see [Tutorial: Aurora Serverless](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-rds-resolvers.html) in the *AWS AppSync Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
