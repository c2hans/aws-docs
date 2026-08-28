---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HiddenSageMakerImage.html
---

# HiddenSageMakerImage
<a name="API_HiddenSageMakerImage"></a>

The SageMaker images that are hidden from the Studio user interface. You must specify the SageMaker image name and version aliases.

## Contents
<a name="API_HiddenSageMakerImage_Contents"></a>

 ** SageMakerImageName **   <a name="sagemaker-Type-HiddenSageMakerImage-SageMakerImageName"></a>
 The SageMaker image name that you are hiding from the Studio user interface.
Type: String
Valid Values: `sagemaker_distribution`
Required: No

 ** VersionAliases **   <a name="sagemaker-Type-HiddenSageMakerImage-VersionAliases"></a>
 The version aliases you are hiding from the Studio user interface.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(0|[1-9]\d*)\.(0|[1-9]\d*)`
Required: No

## See Also
<a name="API_HiddenSageMakerImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HiddenSageMakerImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HiddenSageMakerImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HiddenSageMakerImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
