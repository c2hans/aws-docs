---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CustomImage.html
---

# CustomImage
<a name="API_CustomImage"></a>

A custom SageMaker AI image. For more information, see [Bring your own SageMaker AI image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html).

## Contents
<a name="API_CustomImage_Contents"></a>

 ** AppImageConfigName **   <a name="sagemaker-Type-CustomImage-AppImageConfigName"></a>
The name of the AppImageConfig.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ImageName **   <a name="sagemaker-Type-CustomImage-ImageName"></a>
The name of the CustomImage. Must be unique to your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ImageVersionNumber **   <a name="sagemaker-Type-CustomImage-ImageVersionNumber"></a>
The version number of the CustomImage.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_CustomImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CustomImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CustomImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CustomImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
