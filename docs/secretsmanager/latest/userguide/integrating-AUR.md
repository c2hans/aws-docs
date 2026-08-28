---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-AUR.html
---

# How Amazon Aurora uses AWS Secrets Manager
<a name="integrating-AUR"></a>

Amazon Aurora is a fully managed relational database engine that's compatible with MySQL and PostgreSQL.

To manage master user credentials for Aurora, Aurora can create a [managed secret](service-linked-secrets.md) for you. You are charged for that secret. Aurora also [manages rotation](rotate-secrets_managed.md) for these credentials. For more information, see [Password management with Amazon Aurora and AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide*.

For other Aurora credentials, see [Create an AWS Secrets Manager secret](create_secret.md).

When you call the Amazon RDS Data API, you can pass credentials for the database by using a secret in Secrets Manager. For more information, see [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide*.

When you use the Amazon RDS query editor to connect to a database, you can store credentials for the database in Secrets Manager. For more information, see [Using the query editor](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/query-editor.html) in the *Amazon RDS User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
