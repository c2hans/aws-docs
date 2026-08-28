---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PresignedUrlAccessConfig.html
---

# PresignedUrlAccessConfig
<a name="API_PresignedUrlAccessConfig"></a>

Configuration for accessing hub content through presigned URLs, including license agreement acceptance and URL validation settings.

## Contents
<a name="API_PresignedUrlAccessConfig_Contents"></a>

 ** AcceptEula **   <a name="sagemaker-Type-PresignedUrlAccessConfig-AcceptEula"></a>
Indicates acceptance of the End User License Agreement (EULA) for gated models. Set to true to acknowledge acceptance of the license terms required for accessing gated content.
Type: Boolean
Required: No

 ** ExpectedS3Url **   <a name="sagemaker-Type-PresignedUrlAccessConfig-ExpectedS3Url"></a>
The expected S3 URL prefix for validation purposes. This parameter helps ensure consistency between the resolved S3 URIs and the deployment configuration, reducing potential compatibility issues.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_PresignedUrlAccessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PresignedUrlAccessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PresignedUrlAccessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PresignedUrlAccessConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
