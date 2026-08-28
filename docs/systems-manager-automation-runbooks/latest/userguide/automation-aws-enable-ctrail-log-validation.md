---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-ctrail-log-validation.html
---

# `AWSConfigRemediation-EnableCloudTrailLogFileValidation`
<a name="automation-aws-enable-ctrail-log-validation"></a>

 **Description**

 The `AWSConfigRemediation-EnableCloudTrailLogFileValidation` runbook enables log file validation for your AWS CloudTrail trail.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableCloudTrailLogFileValidation)

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
+ TrailName

  Type: String

  Description: (Required) The name or Amazon Resource Name (ARN) of the trail you want to enable log validation for.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `cloudtrail:GetTrail`
+  `cloudtrail:UpdateTrail`

 **Document Steps**
+  `aws:executeAwsApi` - Enables log validation for the AWS CloudTrail trail you specify in the `TrailName` parameter.
+  `aws:assertAwsResourceProperty` - Verifies log validation is enabled for your trail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
