---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/execution-roles.html
---

# IAM Execution roles
<a name="execution-roles"></a>

Jobs API operations use an AWS Identity and Access Management (IAM) role to access your Amazon S3 buckets securely. The role you specify in your API requests using the `ExecutionRoleArn` parameter must have permissions to read from your input bucket and write to your output bucket. Amazon Location Service assumes this role on your behalf when running jobs, ensuring secure access to your data without requiring long-term credentials.

For more information, see [Configure IAM permissions](https://docs.aws.amazon.com/location/latest/developerguide/configure-iam-role-policy-credentials.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
