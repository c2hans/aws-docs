---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-remove-default-secg-rules.html
---

# `AWSConfigRemediation-RemoveVPCDefaultSecurityGroupRules`
<a name="automation-aws-remove-default-secg-rules"></a>

 **Description**

 The `AWSConfigRemediation-RemoveVPCDefaultSecurityGroupRules` runbook removes all rules from the default security group of the virtual private cloud (VPC) you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-RemoveVPCDefaultSecurityGroupRules)

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
+ GroupId

  Type: String

  Description: (Required) The ID of the security group that you want to remove all rules from.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `ec2:DescribeSecurityGroups`
+  `ec2:RevokeSecurityGroupEgress`
+  `ec2:RevokeSecurityGroupIngress`

 **Document Steps**
+  `aws:assertAwsResourceProperty` - Confirms the security group you specified in the `GroupId` parameter is named default.
+  `aws:executeScript` - Removes all rules from the security group you specified in the `GroupId` parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
