---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-cli-delete.html
---

# Delete a dashboard with the AWS CLI
<a name="lake-dashboard-cli-delete"></a>

This section describes how to use the AWS CLI `delete-dashboard` command to delete a CloudTrail Lake dashboard.

To delete a dashboard, specify the `--dashboard-id` by providing the dashboard ARN, or the dashboard name.

```
aws cloudtrail delete-dashboard --dashboard-id arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash
```

There is no response if the operation is successful.

**Note**
You can't delete a dashboard if `--termination-protection-enabled` is set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
