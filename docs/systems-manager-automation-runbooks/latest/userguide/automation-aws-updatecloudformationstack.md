---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-updatecloudformationstack.html
---

# `AWS-UpdateCloudFormationStack`
<a name="automation-aws-updatecloudformationstack"></a>

 **Description**

Update an AWS CloudFormation stack by using an CloudFormation template stored in an Amazon S3 bucket.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateCloudFormationStack)

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
+ LambdaAssumeRole

  Type: String

  Description: (Required) The ARN of the role assumed by Lambda
+ StackNameOrId

  Type: String

  Description: (Required) Name or Unique ID of the CloudFormation stack to be updated
+ TemplateUrl

  Type: String

   Description: (Required) S3 bucket location that contains the updated CloudFormation template (e.g. `https://s3.amazonaws.com/amzn-s3-demo-bucket2/updated.template)`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
