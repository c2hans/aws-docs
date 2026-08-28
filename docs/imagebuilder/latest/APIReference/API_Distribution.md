---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Distribution.html
---

# Distribution
<a name="API_Distribution"></a>

Defines the settings for a specific Region.

## Contents
<a name="API_Distribution_Contents"></a>

 ** region **   <a name="imagebuilder-Type-Distribution-region"></a>
The target Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** amiDistributionConfiguration **   <a name="imagebuilder-Type-Distribution-amiDistributionConfiguration"></a>
The specific AMI settings; for example, launch permissions or AMI tags.
Type: [AmiDistributionConfiguration](API_AmiDistributionConfiguration.md) object
Required: No

 ** containerDistributionConfiguration **   <a name="imagebuilder-Type-Distribution-containerDistributionConfiguration"></a>
Container distribution settings for encryption, licensing, and sharing in a specific Region.
Type: [ContainerDistributionConfiguration](API_ContainerDistributionConfiguration.md) object
Required: No

 ** fastLaunchConfigurations **   <a name="imagebuilder-Type-Distribution-fastLaunchConfigurations"></a>
The Windows faster-launching configurations to use for AMI distribution.
Type: Array of [FastLaunchConfiguration](API_FastLaunchConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: No

 ** launchTemplateConfigurations **   <a name="imagebuilder-Type-Distribution-launchTemplateConfigurations"></a>
A group of launchTemplateConfiguration settings that apply to image distribution for specified accounts.
Type: Array of [LaunchTemplateConfiguration](API_LaunchTemplateConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** licenseConfigurationArns **   <a name="imagebuilder-Type-Distribution-licenseConfigurationArns"></a>
The License Manager Configuration to associate with the AMI in the specified Region.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `^arn:aws[^:]*:license-manager:[^:]+:[0-9]{12}:license-configuration:lic-[a-z0-9-_]{32}$`
Required: No

 ** s3ExportConfiguration **   <a name="imagebuilder-Type-Distribution-s3ExportConfiguration"></a>
Configure export settings to deliver disk images created from your image build, using a file format that is compatible with your VMs in that Region.
Type: [S3ExportConfiguration](API_S3ExportConfiguration.md) object
Required: No

 ** ssmParameterConfigurations **   <a name="imagebuilder-Type-Distribution-ssmParameterConfigurations"></a>
Contains settings to update AWS Systems Manager (SSM) Parameter Store Parameters with output AMI IDs from the build by target Region.
Type: Array of [SsmParameterConfiguration](API_SsmParameterConfiguration.md) objects
Required: No

## See Also
<a name="API_Distribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/Distribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/Distribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/Distribution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
