---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-cloudfront-viewer-policy.html
---

# `AWSConfigRemediation-EnableCloudFrontViewerPolicyHTTPS`
<a name="automation-aws-enable-cloudfront-viewer-policy"></a>

 **Description**

 The `AWSConfigRemediation-EnableCloudFrontViewerPolicyHTTPS` runbook enables the viewer protocol policy for the Amazon CloudFront (CloudFront) distribution you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableCloudFrontViewerPolicyHTTPS)

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

  Description: (Required) The ID of the CloudFront distribution you want to enable the viewer protocol policy on.
+ ViewerProtocolPolicy

  Type: String

  Valid values: https-only, redirect-to-https

  Description: (Required) The protocol that viewers can use to access the files in the origin.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `cloudfront:GetDistributionConfig`
+  `cloudfront:UpdateDistribution`
+  `cloudfront:GetDistribution`

 **Document Steps**
+  `aws:executeScript` - Enables the viewer protocol policy for the CloudFront distribution you specify in the `CloudFrontDistributionId` parameter, and verifies the policy was assigned.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
