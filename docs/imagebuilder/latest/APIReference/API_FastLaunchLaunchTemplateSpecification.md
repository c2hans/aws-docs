---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_FastLaunchLaunchTemplateSpecification.html
---

# FastLaunchLaunchTemplateSpecification
<a name="API_FastLaunchLaunchTemplateSpecification"></a>

Identifies the launch template that the associated Windows AMI uses for launching an instance when faster launching is enabled.

**Note**
You can specify either the `launchTemplateName` or the `launchTemplateId`, but not both.

## Contents
<a name="API_FastLaunchLaunchTemplateSpecification_Contents"></a>

 ** launchTemplateId **   <a name="imagebuilder-Type-FastLaunchLaunchTemplateSpecification-launchTemplateId"></a>
The ID of the launch template to use for faster launching for a Windows AMI.
Type: String
Pattern: `^lt-[a-z0-9-_]{17}$`
Required: No

 ** launchTemplateName **   <a name="imagebuilder-Type-FastLaunchLaunchTemplateSpecification-launchTemplateName"></a>
The name of the launch template to use for faster launching for a Windows AMI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** launchTemplateVersion **   <a name="imagebuilder-Type-FastLaunchLaunchTemplateSpecification-launchTemplateVersion"></a>
The version of the launch template to use for faster launching for a Windows AMI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_FastLaunchLaunchTemplateSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/FastLaunchLaunchTemplateSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/FastLaunchLaunchTemplateSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/FastLaunchLaunchTemplateSpecification)
