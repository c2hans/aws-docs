---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/enable-cloudtrail-cloudwatch-logs.html
---

# `AWS-EnableCloudTrailCloudWatchLogs`
<a name="enable-cloudtrail-cloudwatch-logs"></a>

**Description**

This runbook updates the configuration of one or more AWS CloudTrail trails to send events to an Amazon CloudWatch Logs log group.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCloudTrailCloudWatchLogs)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ CloudWatchLogsLogGroupArn

  Type: String

  Description: (Required) The ARN of the CloudWatch Logs log group where the CloudTrail logs will be delivered.
+ CloudWatchLogsRoleArn

  Type: String

  Description: (Required) The ARN of the IAM role CloudWatch Logs Logs assumes to write to the specified log group.
+ TrailNames

  Type: StringList

  Description: (Required) A comma separated list of the names of the CloudTrail trails whose events you want to send to CloudWatch Logs.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudtrail:UpdateTrail`
+ `iam:PassRole`

**Document Steps**
+ `aws:executeScript` - Updates the specified CloudTrail trails to deliver events to the specified CloudWatch Logs log group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
