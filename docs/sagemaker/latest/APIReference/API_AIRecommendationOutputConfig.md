---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIRecommendationOutputConfig.html
---

# AIRecommendationOutputConfig
<a name="API_AIRecommendationOutputConfig"></a>

The output configuration for an AI recommendation job.

## Contents
<a name="API_AIRecommendationOutputConfig_Contents"></a>

 ** MlflowConfig **   <a name="sagemaker-Type-AIRecommendationOutputConfig-MlflowConfig"></a>
The MLflow tracking configuration for the job. If you don't specify this parameter, MLflow tracking is disabled.
Type: [AIMlflowConfig](API_AIMlflowConfig.md) object
Required: No

 ** ModelPackageGroupIdentifier **   <a name="sagemaker-Type-AIRecommendationOutputConfig-ModelPackageGroupIdentifier"></a>
The name or Amazon Resource Name (ARN) of the model package group where the optimized model is registered as a new model package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*/)?([a-zA-Z0-9]([a-zA-Z0-9\-]){0,62})(?<!-)`
Required: No

 ** S3OutputLocation **   <a name="sagemaker-Type-AIRecommendationOutputConfig-S3OutputLocation"></a>
The Amazon S3 URI where recommendation results are stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_AIRecommendationOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIRecommendationOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIRecommendationOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIRecommendationOutputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
