---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Deletion.html
---

# Effects of deleting a field index policy
<a name="CloudWatchLogs-Field-Indexing-Deletion"></a>

If you delete a field index policy that has been in effect for a time, the following happens:
+ For up to 30 days after the policy is deleted, queries can still benefit from the indexed log events.
+ If you delete a log-group level index policy, and there is already an account-level policy in place that would apply to that log group, the account-level policy will eventually apply to that log group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
