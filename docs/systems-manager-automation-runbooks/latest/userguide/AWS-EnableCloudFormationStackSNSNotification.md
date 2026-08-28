---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-EnableCloudFormationStackSNSNotification.html
---

# `AWS-EnableCloudFormationSNSNotification`
<a name="AWS-EnableCloudFormationStackSNSNotification"></a>

 **Description**

 The `AWS-EnableCloudFormationSNSNotification` runbook enables Amazon Simple Notification Service (Amazon SNS) notifications for the AWS CloudFormation (CloudFormation) stack you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCloudFormationStackSNSNotification)

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
+ StackArn

  Type: String

  Description: (Required) The ARN or name of the CloudFormation stack you want to enable Amazon SNS notifications for.
+ NotificationArn

  Type: String

  Description: (Required) The ARN of the Amazon SNS topic you want to associate with the CloudFormation stack.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ ssm:GetAutomationExecution
+ ssm:StartAutomationExecution
+ cloudformation:DescribeStacks
+ cloudformation:UpdateStack
+ kms:Decrypt
+ kms:GenerateDataKey
+ sns:Publish
+ sqs:GetQueueAttributes

 **Document Steps**
+ CheckCfnSnsLimits (`aws:executeScript`) - Verifies the maximum number of Amazon SNS topics haven't already been associated with the CloudFormation stack you specify.
+ EnableCfnSnsNotification (`aws:executeAwsApi`) - Enables Amazon SNS notifications for the CloudFormation stack.
+ VerificationCfnSnsNotification (`aws:executeScript`) - Verifies that Amazon SNS notifications have been enabled for the CloudFormation stack.

 **Outputs**

CheckCfnSnsLimits.NotificationArnList - A list of ARNs that receive Amazon SNS notifications for the CloudFormation stack.

VerificationCfnSnsNotification.VerifySnsTopicsResponse - Response from the API operation confirming Amazon SNS notifications have been enabled for the CloudFormation stack.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
