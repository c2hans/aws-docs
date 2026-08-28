---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-console-logging.html
---

# Requirements for Amazon CloudWatch Logs—setting up channel logging
<a name="requirements-for-console-logging"></a>

 MediaLive produces channel logs that it sends to CloudWatch Logs, where users can view them. For more information about channel logs, see [Monitoring a channel using Amazon CloudWatch Logs](monitoring-with-logs.md).

You must decide if you want to give some or all of your users permission to view the logs in CloudWatch Logs.

You must also decide if you want to give some or all of your users permission to set the retention policy for logs. If you decide not to give this access to any user, an administrator must be responsible for setting the policy.

Users don't need special permission to enable logging from within MediaLive.

The following table shows the actions in IAM that relate to access for setting up channel logs.

| Permissions | Service name in IAM | Actions |
| --- | --- | --- |
| View Logs  | CloudWatch Logs | FilterLogEvents`GetLogEvents` |
| Set Retention Policy |  CloudWatch Logs | DeleteRetentionPolicy`PutRetentionPolicy`  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
