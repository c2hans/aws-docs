---
source_url: https://docs.aws.amazon.com/glue/latest/dg/iceberg-column-stats-prereqs.html
---

# Prerequisites for generating column statistics
<a name="iceberg-column-stats-prereqs"></a>

To generate or update column statistics for Iceberg tables, the statistics generation task assumes an AWS Identity and Access Management (IAM) role on your behalf. Based on the permissions granted to the role, the column statistics generation task can read the data from the Amazon S3 data store.

When you configure the column statistics generation task, AWS Glue allows you to create a role that includes the `AWSGlueServiceRole` AWS managed policy plus the required inline policy for the specified data source.

If you specify an existing role for generating column statistics, ensure that it includes the `AWSGlueServiceRole` policy or equivalent (or a scoped down version of this policy), and the required inline policies.

For more information about the required permissions, see [Prerequisites for generating column statistics](column-stats-prereqs.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
