---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchConfigurationTemplate.html
---

# LaunchConfigurationTemplate
<a name="API_LaunchConfigurationTemplate"></a>

Account level Launch Configuration Template.

## Contents
<a name="API_LaunchConfigurationTemplate_Contents"></a>

 ** arn **   <a name="drs-Type-LaunchConfigurationTemplate-arn"></a>
ARN of the Launch Configuration Template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** copyPrivateIp **   <a name="drs-Type-LaunchConfigurationTemplate-copyPrivateIp"></a>
Copy private IP.
Type: Boolean
Required: No

 ** copyTags **   <a name="drs-Type-LaunchConfigurationTemplate-copyTags"></a>
Copy tags.
Type: Boolean
Required: No

 ** exportBucketArn **   <a name="drs-Type-LaunchConfigurationTemplate-exportBucketArn"></a>
S3 bucket ARN to export Source Network templates.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** launchConfigurationTemplateID **   <a name="drs-Type-LaunchConfigurationTemplate-launchConfigurationTemplateID"></a>
ID of the Launch Configuration Template.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`
Required: No

 ** launchDisposition **   <a name="drs-Type-LaunchConfigurationTemplate-launchDisposition"></a>
Launch disposition.
Type: String
Valid Values: `STOPPED | STARTED`
Required: No

 ** launchIntoSourceInstance **   <a name="drs-Type-LaunchConfigurationTemplate-launchIntoSourceInstance"></a>
DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.
Type: Boolean
Required: No

 ** licensing **   <a name="drs-Type-LaunchConfigurationTemplate-licensing"></a>
Licensing.
Type: [Licensing](API_Licensing.md) object
Required: No

 ** postLaunchEnabled **   <a name="drs-Type-LaunchConfigurationTemplate-postLaunchEnabled"></a>
Post-launch actions activated.
Type: Boolean
Required: No

 ** recoveryMode **   <a name="drs-Type-LaunchConfigurationTemplate-recoveryMode"></a>
Recovery mode.
Type: String
Valid Values: `FAST | OPTIMAL`
Required: No

 ** tags **   <a name="drs-Type-LaunchConfigurationTemplate-tags"></a>
Tags of the Launch Configuration Template.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** targetInstanceTypeRightSizingMethod **   <a name="drs-Type-LaunchConfigurationTemplate-targetInstanceTypeRightSizingMethod"></a>
Target instance type right-sizing method.
Type: String
Valid Values: `NONE | BASIC | IN_AWS`
Required: No

## See Also
<a name="API_LaunchConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/LaunchConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/LaunchConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/LaunchConfigurationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
