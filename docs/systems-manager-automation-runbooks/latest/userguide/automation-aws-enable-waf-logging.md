---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-waf-logging.html
---

# `AWSConfigRemediation-EnableWAFClassicLogging`
<a name="automation-aws-enable-waf-logging"></a>

 **Description**

 The `AWSConfigRemediation-EnableWAFClassicLogging` runbook enables logging to Amazon Data Firehose (Firehose) for the AWS WAF web access control list (web ACL) you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableWAFClassicRegionalLogging)

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
+ DeliveryStreamName

  Type: String

  Description: (Required) The name of the Firehose delivery stream that you want to send logs to.
+ WebACLId

  Type: String

  Description: (Required) The ID of the AWS WAF web ACL that you want to enable logging on.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `iam:CreateServiceLinkedRole`
+  `waf:GetLoggingConfiguration`
+  `waf:GetWebAcl `
+  `waf:PutLoggingConfiguration `

 **Document Steps**
+  `aws:executeAwsApi` - Confirms the delivery stream you specify in the `DeliveryStreamName` exists.
+  `aws:executeAwsApi` - Gathers the ARN of the AWS WAF web ACL specified in the `WebACLId` parameter.
+  `aws:executeAwsApi` - Enables logging for the web ACL.
+  `aws:assertAwsResourceProperty` - Verifies logging has been enabled on the AWS WAF web ACL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
