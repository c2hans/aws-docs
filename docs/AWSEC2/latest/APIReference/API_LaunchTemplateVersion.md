---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateVersion.html
---

# LaunchTemplateVersion
<a name="API_LaunchTemplateVersion"></a>

Describes a launch template version.

## Contents
<a name="API_LaunchTemplateVersion_Contents"></a>

 ** createdBy **
The principal that created the version.
Type: String
Required: No

 ** createTime **
The time the version was created.
Type: Timestamp
Required: No

 ** defaultVersion **
Indicates whether the version is the default version.
Type: Boolean
Required: No

 ** launchTemplateData **
Information about the launch template.
Type: [ResponseLaunchTemplateData](API_ResponseLaunchTemplateData.md) object
Required: No

 ** launchTemplateId **
The ID of the launch template.
Type: String
Required: No

 ** launchTemplateName **
The name of the launch template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9\(\)\.\-/_]+`
Required: No

 ** operator **
The entity that manages the launch template.
Type: [OperatorResponse](API_OperatorResponse.md) object
Required: No

 ** versionDescription **
The description for the version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** versionNumber **
The version number.
Type: Long
Required: No

## See Also
<a name="API_LaunchTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateVersion)
