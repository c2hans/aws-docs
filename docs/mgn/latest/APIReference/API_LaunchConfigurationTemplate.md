---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_LaunchConfigurationTemplate.html
---

# LaunchConfigurationTemplate
<a name="API_LaunchConfigurationTemplate"></a>

## Contents
<a name="API_LaunchConfigurationTemplate_Contents"></a>

 ** launchConfigurationTemplateID **   <a name="mgn-Type-LaunchConfigurationTemplate-launchConfigurationTemplateID"></a>
ID of the Launch Configuration Template.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`
Required: Yes

 ** arn **   <a name="mgn-Type-LaunchConfigurationTemplate-arn"></a>
ARN of the Launch Configuration Template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** associatePublicIpAddress **   <a name="mgn-Type-LaunchConfigurationTemplate-associatePublicIpAddress"></a>
Associate public Ip address.
Type: Boolean
Required: No

 ** bootMode **   <a name="mgn-Type-LaunchConfigurationTemplate-bootMode"></a>
Launch configuration template boot mode.
Type: String
Valid Values: `LEGACY_BIOS | UEFI | USE_SOURCE`
Required: No

 ** copyPrivateIp **   <a name="mgn-Type-LaunchConfigurationTemplate-copyPrivateIp"></a>
Copy private Ip.
Type: Boolean
Required: No

 ** copyTags **   <a name="mgn-Type-LaunchConfigurationTemplate-copyTags"></a>
Copy tags.
Type: Boolean
Required: No

 ** ec2LaunchTemplateID **   <a name="mgn-Type-LaunchConfigurationTemplate-ec2LaunchTemplateID"></a>
EC2 launch template ID.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `lt-[0-9a-z]{17}`
Required: No

 ** enableMapAutoTagging **   <a name="mgn-Type-LaunchConfigurationTemplate-enableMapAutoTagging"></a>
Enable map auto tagging.
Type: Boolean
Required: No

 ** enableParametersEncryption **   <a name="mgn-Type-LaunchConfigurationTemplate-enableParametersEncryption"></a>
Enable parameters encryption.
Type: Boolean
Required: No

 ** largeVolumeConf **   <a name="mgn-Type-LaunchConfigurationTemplate-largeVolumeConf"></a>
Large volume config.
Type: [LaunchTemplateDiskConf](API_LaunchTemplateDiskConf.md) object
Required: No

 ** launchDisposition **   <a name="mgn-Type-LaunchConfigurationTemplate-launchDisposition"></a>
Launch disposition.
Type: String
Valid Values: `STOPPED | STARTED`
Required: No

 ** licensing **   <a name="mgn-Type-LaunchConfigurationTemplate-licensing"></a>
Configure Licensing.
Type: [Licensing](API_Licensing.md) object
Required: No

 ** mapAutoTaggingMpeID **   <a name="mgn-Type-LaunchConfigurationTemplate-mapAutoTaggingMpeID"></a>
Launch configuration template map auto tagging MPE ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** parametersEncryptionKey **   <a name="mgn-Type-LaunchConfigurationTemplate-parametersEncryptionKey"></a>
Parameters encryption key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** postLaunchActions **   <a name="mgn-Type-LaunchConfigurationTemplate-postLaunchActions"></a>
Post Launch Actions of the Launch Configuration Template.
Type: [PostLaunchActions](API_PostLaunchActions.md) object
Required: No

 ** smallVolumeConf **   <a name="mgn-Type-LaunchConfigurationTemplate-smallVolumeConf"></a>
Small volume config.
Type: [LaunchTemplateDiskConf](API_LaunchTemplateDiskConf.md) object
Required: No

 ** smallVolumeMaxSize **   <a name="mgn-Type-LaunchConfigurationTemplate-smallVolumeMaxSize"></a>
Small volume maximum size.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** tags **   <a name="mgn-Type-LaunchConfigurationTemplate-tags"></a>
Tags of the Launch Configuration Template.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** targetInstanceTypeRightSizingMethod **   <a name="mgn-Type-LaunchConfigurationTemplate-targetInstanceTypeRightSizingMethod"></a>
Target instance type right-sizing method.
Type: String
Valid Values: `NONE | BASIC`
Required: No

## See Also
<a name="API_LaunchConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/LaunchConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/LaunchConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/LaunchConfigurationTemplate)
