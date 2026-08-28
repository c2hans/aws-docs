---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-cloudfront-failover.html
---

# `AWSConfigRemediation-EnableCloudFrontOriginFailover`
<a name="automation-aws-enable-cloudfront-failover"></a>

 **Description**

 The `AWSConfigRemediation-EnableCloudFrontOriginFailover` runbook enables origin failover for the Amazon CloudFront (CloudFront) distribution you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableCloudFrontOriginFailover)

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
+ CloudFrontDistributionId

  Type: String

  Description: (Required) The ID of the CloudFront distribution you want to enable origin failover on.
+ OriginGroupId

  Type: String

  Description: (Required) The ID of the origin group.
+ PrimaryOriginId

  Type: String

  Description: (Required) The ID of the primary origin in the origin group.
+ SecondaryOriginId

  Type: String

  Description: (Required) The ID of the secondary origin in the origin group.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `cloudfront:GetDistributionConfig`
+  `cloudfront:UpdateDistribution`

 **Document Steps**
+  `aws:executeScript` - Enables origin failover for the CloudFront distribution you specify in the `CloudFrontDistributionId` parameter, and verifies that failover has been enabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
