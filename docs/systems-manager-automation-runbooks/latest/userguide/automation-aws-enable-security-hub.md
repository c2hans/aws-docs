---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-security-hub.html
---

# `AWSConfigRemediation-EnableSecurityHub`
<a name="automation-aws-enable-security-hub"></a>

 **Description**

 The `AWSConfigRemediation-EnableSecurityHub` runbook enables AWS Security Hub CSPM (Security Hub CSPM) for the AWS account and AWS Region where you run the automation. For information about Security Hub CSPM, see [What is AWS Security Hub CSPM?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) in the *AWS Security Hub User Guide* .

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableSecurityHub)

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
+ EnableDefaultStandards

  Type: Boolean

  Default: true

   Description: (Required) If set to `true` , the default security standards designated by Security Hub CSPM are enabled.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `securityhub:DescribeHub`
+  `securityhub:EnableSecurityHub`
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`

 **Document Steps**
+  `aws:executeAwsApi` - Enables Security Hub CSPM in the current account and Region.
+  `aws:executeAwsApi` - Verifies that Security Hub CSPM has been enabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
