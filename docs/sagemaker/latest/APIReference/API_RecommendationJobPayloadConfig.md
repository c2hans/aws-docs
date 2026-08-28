---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RecommendationJobPayloadConfig.html
---

# RecommendationJobPayloadConfig
<a name="API_RecommendationJobPayloadConfig"></a>

The configuration for the payload for a recommendation job.

## Contents
<a name="API_RecommendationJobPayloadConfig_Contents"></a>

 ** SamplePayloadUrl **   <a name="sagemaker-Type-RecommendationJobPayloadConfig-SamplePayloadUrl"></a>
The Amazon Simple Storage Service (Amazon S3) path where the sample payload is stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** SupportedContentTypes **   <a name="sagemaker-Type-RecommendationJobPayloadConfig-SupportedContentTypes"></a>
The supported MIME types for the input data.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_RecommendationJobPayloadConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RecommendationJobPayloadConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RecommendationJobPayloadConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RecommendationJobPayloadConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
