---
source_url: https://docs.aws.amazon.com/ebs/latest/userguide/dlm-script-monitoring.html
---

# Monitor Amazon Data Lifecycle Manager pre and post scripts
<a name="dlm-script-monitoring"></a>

**Amazon CloudWatch metrics**
Amazon Data Lifecycle Manager publishes the following CloudWatch metrics when pre and post scripts fail and succeed and when VSS backups fail and succeed.
+ `PreScriptStarted`
+ `PreScriptCompleted`
+ `PreScriptFailed`
+ `PostScriptStarted`
+ `PostScriptCompleted`
+ `PostScriptFailed`
+ `VSSBackupStarted`
+ `VSSBackupCompleted`
+ `VSSBackupFailed`

For more information, see [Monitor Data Lifecycle Manager policies using CloudWatch](monitor-dlm-cw-metrics.md).

**Amazon EventBridge**
Amazon Data Lifecycle Manager emits the following Amazon EventBridge event when a pre or post script is initiated, succeeds, or fails
+ `DLM Pre Post Script Notification`

For more information, see [Monitor Data Lifecycle Manager policies using EventBridge](monitor-cloudwatch-events.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EBS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ebs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
