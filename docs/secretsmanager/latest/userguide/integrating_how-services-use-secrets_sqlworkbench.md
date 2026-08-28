---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_sqlworkbench.html
---

# Amazon Redshift query editor v2
<a name="integrating_how-services-use-secrets_sqlworkbench"></a>

Amazon Redshift query editor v2 is a web-based SQL client application that you can use to author and run queries on your Amazon Redshift data warehouse. When you use the Amazon Redshift query editor v2 to connect to a database, Amazon Redshift can store your credentials in a Secrets Manager [managed secret](service-linked-secrets.md) with the prefix `sqlworkbench`. The cost of storing the secret is included with the charge for using Amazon Redshift. To update the secret, you must use Amazon Redshift rather than Secrets Manager. For more information, see [Working with query editor v2 ](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-using.html) in the *Amazon Redshift Management Guide*.

For the previous query editor, see [How Amazon Redshift uses AWS Secrets Manager](integrating_how-services-use-secrets_RS.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
