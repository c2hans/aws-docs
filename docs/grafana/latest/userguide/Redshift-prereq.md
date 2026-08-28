---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/Redshift-prereq.html
---

# Prerequisites
<a name="Redshift-prereq"></a>

To use the AWS managed policies for Amazon Managed Grafana, complete the following tasks before you configure the Amazon Redshift data source:
+ Tag your Amazon Redshift cluster with `GrafanaDataSource: true`. Otherwise, it won't be accessible.
+ Create the database credentials in one of the following mutually exclusive ways:
  + If you want to use the default mechanism (the temporary credentials options) to authenticate against the Redshift database, you must create a database user named `redshift_data_api_user`.
  + If you want to use the credentials from Secrets Manager, you must tag the secret with `RedshiftQueryOwner: true`. For more information, see [Identity-based policy examples in Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/security_iam_id-based-policy-examples.html)in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
