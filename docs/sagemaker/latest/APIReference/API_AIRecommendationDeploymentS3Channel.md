---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIRecommendationDeploymentS3Channel.html
---

# AIRecommendationDeploymentS3Channel
<a name="API_AIRecommendationDeploymentS3Channel"></a>

An Amazon S3 data channel for a recommended deployment configuration, containing model artifacts or optimized model outputs.

## Contents
<a name="API_AIRecommendationDeploymentS3Channel_Contents"></a>

 ** ChannelName **   <a name="sagemaker-Type-AIRecommendationDeploymentS3Channel-ChannelName"></a>
A custom name for this Amazon S3 data channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\.\-_]+`
Required: No

 ** Uri **   <a name="sagemaker-Type-AIRecommendationDeploymentS3Channel-Uri"></a>
The Amazon S3 URI of the data for this channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_AIRecommendationDeploymentS3Channel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIRecommendationDeploymentS3Channel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIRecommendationDeploymentS3Channel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIRecommendationDeploymentS3Channel)
