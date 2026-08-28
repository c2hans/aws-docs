---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIRecommendationOutputResult.html
---

# AIRecommendationOutputResult
<a name="API_AIRecommendationOutputResult"></a>

The output configuration for an AI recommendation job, including the S3 location for results and the model package group for deployment.

## Contents
<a name="API_AIRecommendationOutputResult_Contents"></a>

 ** S3OutputLocation **   <a name="sagemaker-Type-AIRecommendationOutputResult-S3OutputLocation"></a>
The Amazon S3 URI where the recommendation job writes its output results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** MlflowConfig **   <a name="sagemaker-Type-AIRecommendationOutputResult-MlflowConfig"></a>
The MLflow tracking configuration for the job.
Type: [AIMlflowConfig](API_AIMlflowConfig.md) object
Required: No

 ** ModelPackageGroupIdentifier **   <a name="sagemaker-Type-AIRecommendationOutputResult-ModelPackageGroupIdentifier"></a>
The name or Amazon Resource Name (ARN) of the model package group where deployment-ready model packages are registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*/)?([a-zA-Z0-9]([a-zA-Z0-9\-]){0,62})(?<!-)`
Required: No

## See Also
<a name="API_AIRecommendationOutputResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIRecommendationOutputResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIRecommendationOutputResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIRecommendationOutputResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
