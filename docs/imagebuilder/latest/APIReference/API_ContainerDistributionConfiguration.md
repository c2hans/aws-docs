---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ContainerDistributionConfiguration.html
---

# ContainerDistributionConfiguration
<a name="API_ContainerDistributionConfiguration"></a>

Container distribution settings for encryption, licensing, and sharing in a specific Region.

## Contents
<a name="API_ContainerDistributionConfiguration_Contents"></a>

 ** targetRepository **   <a name="imagebuilder-Type-ContainerDistributionConfiguration-targetRepository"></a>
The destination repository for the container distribution configuration.
Type: [TargetContainerRepository](API_TargetContainerRepository.md) object
Required: Yes

 ** containerTags **   <a name="imagebuilder-Type-ContainerDistributionConfiguration-containerTags"></a>
Tags that are attached to the container distribution configuration.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** description **   <a name="imagebuilder-Type-ContainerDistributionConfiguration-description"></a>
The description of the container distribution configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ContainerDistributionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ContainerDistributionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ContainerDistributionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ContainerDistributionConfiguration)
