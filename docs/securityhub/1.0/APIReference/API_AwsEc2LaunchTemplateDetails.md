---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDetails.html
---

# AwsEc2LaunchTemplateDetails
<a name="API_AwsEc2LaunchTemplateDetails"></a>

 Specifies the properties for creating an Amazon Elastic Compute Cloud (Amazon EC2) launch template.

## Contents
<a name="API_AwsEc2LaunchTemplateDetails_Contents"></a>

 ** DefaultVersionNumber **   <a name="securityhub-Type-AwsEc2LaunchTemplateDetails-DefaultVersionNumber"></a>
 The default version of the launch template.
Type: Long
Required: No

 ** Id **   <a name="securityhub-Type-AwsEc2LaunchTemplateDetails-Id"></a>
 An ID for the launch template.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LatestVersionNumber **   <a name="securityhub-Type-AwsEc2LaunchTemplateDetails-LatestVersionNumber"></a>
 The latest version of the launch template.
Type: Long
Required: No

 ** LaunchTemplateData **   <a name="securityhub-Type-AwsEc2LaunchTemplateDetails-LaunchTemplateData"></a>
 The information to include in the launch template.
Type: [AwsEc2LaunchTemplateDataDetails](API_AwsEc2LaunchTemplateDataDetails.md) object
Required: No

 ** LaunchTemplateName **   <a name="securityhub-Type-AwsEc2LaunchTemplateDetails-LaunchTemplateName"></a>
 A name for the launch template.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
