---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/Athena-prereq.html
---

# Prerequisites
<a name="Athena-prereq"></a>

To use the managed policies for Amazon Managed Grafana for Athena, complete the following tasks before you configure the Athena data source:
+ Tag your Athena work groups with `GrafanaDataSource: true`.
+ Create an S3 bucket with a name that starts with `grafana-athena-query-results-`. This policy provides permissions for writing query results into an S3 bucket with that naming convention.

The Amazon S3 permissions for accessing the underlying data source of an Athena query are not included in this managed policy. You must add the necessary permissions for the Amazon S3 buckets manually, on a case-by-case basis. For more information, see [Identity-based policy examples in Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/security_iam_id-based-policy-examples.html) in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
