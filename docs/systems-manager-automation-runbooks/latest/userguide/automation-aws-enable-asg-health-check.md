---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-asg-health-check.html
---

# `AWSConfigRemediation-EnableAutoScalingGroupELBHealthCheck`
<a name="automation-aws-enable-asg-health-check"></a>

**Description**

The `AWSConfigRemediation-EnableAutoScalingGroupELBHealthCheck` runbook enables health checks for the Amazon EC2 Auto Scaling (Auto Scaling) group you specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableAutoScalingGroupELBHealthCheck)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
+ AutoScalingGroupARN

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the auto scaling group that you want to enable health checks on.
+ HealthCheckGracePeriod

  Type: Integer

  Default: 300

  Description: (Optional) The amount of time, in seconds, that Auto Scaling waits before checking the health status of an Amazon Elastic Compute Cloud (Amazon EC2) instance that has come into service.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ssm:StartAutomationExecution`
+ `ssm:GetAutomationExecution`
+ `ec2:DescribeAutoScalingGroups`
+ `ec2:UpdateAutoScalingGroup`

**Document Steps**
+ `aws:executeScript` - Enables health checks on the Auto Scaling group you specify in the `AutoScalingGroupARN` parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
