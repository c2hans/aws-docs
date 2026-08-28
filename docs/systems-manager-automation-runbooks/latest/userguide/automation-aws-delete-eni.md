---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-eni.html
---

# `AWSConfigRemediation-DeleteUnusedENI`
<a name="automation-aws-delete-eni"></a>

 **Description**

 The `AWSConfigRemediation-DeleteUnusedENI` runbook deletes an elastic network interface (ENI) that has an attachment status of `detached` .

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteUnusedENI)

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
+ NetworkInterfaceId

  Type: String

  Description: (Required) The ID of the ENI that you want to delete.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `ec2:DeleteNetworkInterface`
+  `ec2:DescribeNetworkInterfaces `

 **Document Steps**
+  `aws:executeAwsApi` - Deletes the ENI you specify in the `NetworkInterfaceId` parameter.
+  `aws:executeScript` - Verifies the ENI has been deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
