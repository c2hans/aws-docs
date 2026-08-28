---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_LFMlong.html
---

# How Amazon Lookout for Metrics uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_LFMlong"></a>

Amazon Lookout for Metrics is a service that finds anomalies in your data, determines their root causes, and enables you to quickly take action. You can use Amazon Redshift or Amazon RDS as a datasource for an Lookout for Metrics detector. To configure the datasource, you use a secret that contains the database password. For more information, see [Using Amazon RDS with Lookout for Metrics](https://docs.aws.amazon.com/lookoutmetrics/latest/dev/services-rds.html) and [Using Amazon Redshift with Lookout for Metrics](https://docs.aws.amazon.com/lookoutmetrics/latest/dev/services-redshift.html) in the *Amazon Lookout for Metrics Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
