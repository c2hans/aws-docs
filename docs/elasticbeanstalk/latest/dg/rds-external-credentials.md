---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/rds-external-credentials.html
---

# Storing the Amazon RDS credentials in AWS Secrets Manager
<a name="rds-external-credentials"></a>

This topic explains how AWS Secrets Manager can improve your security posture for credential retrieval with Elastic Beanstalk. It also provides references to specific resources that can help you configure credentials for your Elastic Beanstalk application.

AWS Secrets Manager helps you improve your security posture, by providing the ability to store and retrieve encrypted credentials. Storing the credentials in Secrets Manager helps avoid possible compromise by anyone who can inspect your application or the components related to it. Your code can make a runtime call to the Secrets Manager service to retrieve credentials dynamically. Secrets Manager also offers features like client-side secret caching components for runtime languages, which include Python, Go, and Java.

For more information, see the following topics in the *AWS Secrets Manager User Guide*.
+ [How Amazon RDS uses AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_RDS.html)
+ [Create an AWS Secrets Manager database secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html)
+ [Retrieve secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
