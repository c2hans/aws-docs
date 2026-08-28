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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
