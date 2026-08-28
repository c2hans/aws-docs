---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-account-access-analyzer.html
---

# `AWSConfigRemediation-EnableAccountAccessAnalyzer`
<a name="automation-aws-enable-account-access-analyzer"></a>

 **Description**

 The `AWSConfigRemediation-EnableAccountAccessAnalyzer` runbook creates an AWS Identity and Access Management (IAM) Access Analyzer in your AWS account. For information about Access Analyzer, see [Using AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) in the *IAM User Guide* .

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableAccountAccessAnalyzer)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AnalyzerName

  Type: String

  Description: (Required) The name of the analyzer to create.
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `access-analyzer:CreateAnalyzer`
+  `access-analyzer:GetAnalyzer`

 **Document Steps**
+  `aws:executeAwsApi` - Creates an access analyzer for your account.
+  `aws:waitForAwsResourceProperty` - Waits for the status of the access analyzer to be `ACTIVE` .
+  `aws:assertAwsResourceProperty` - Confirms the status of the access analyzer is `ACTIVE` .

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
