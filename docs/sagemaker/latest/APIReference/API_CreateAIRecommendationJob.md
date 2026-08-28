---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAIRecommendationJob.html
---

# CreateAIRecommendationJob
<a name="API_CreateAIRecommendationJob"></a>

Creates a recommendation job that generates intelligent optimization recommendations for generative AI inference deployments. The job analyzes your model, workload configuration, and performance targets to recommend optimal instance types, model optimization techniques (such as quantization and speculative decoding), and deployment configurations.

## Request Syntax
<a name="API_CreateAIRecommendationJob_RequestSyntax"></a>

```
{
   "AdapterSource": { ... },
   "AIRecommendationJobName": "{{string}}",
   "AIWorkloadConfigIdentifier": "{{string}}",
   "ComputeSpec": {
      "CapacityReservationConfig": {
         "CapacityReservationPreference": "{{string}}",
         "MlReservationArns": [ "{{string}}" ]
      },
      "InstanceTypes": [ "{{string}}" ]
   },
   "InferenceSpecification": {
      "Framework": "{{string}}"
   },
   "ModelSource": { ... },
   "OptimizeModel": {{boolean}},
   "OutputConfig": {
      "MlflowConfig": {
         "MlflowExperimentName": "{{string}}",
         "MlflowResourceArn": "{{string}}",
         "MlflowRunName": "{{string}}"
      },
      "ModelPackageGroupIdentifier": "{{string}}",
      "S3OutputLocation": "{{string}}"
   },
   "PerformanceTarget": {
      "Constraints": [
         {
            "Metric": "{{string}}"
         }
      ]
   },
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAIRecommendationJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdapterSource](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-AdapterSource"></a>
The LoRA adapter source for the recommendation job. Specify either a list of model package ARNs or Amazon S3 URIs for your LoRA adapters. When this parameter is absent, the recommendation job runs without LoRA adapter support.
Type: [AIAdapterSource](API_AIAdapterSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [AIRecommendationJobName](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-AIRecommendationJobName"></a>
The name of the AI recommendation job. The name must be unique within your AWS account in the current AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [AIWorkloadConfigIdentifier](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-AIWorkloadConfigIdentifier"></a>
The name or Amazon Resource Name (ARN) of the AI workload configuration to use for this recommendation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*/)?([a-zA-Z0-9]([a-zA-Z0-9\-]){0,62})(?<!-)`
Required: Yes

 ** [ComputeSpec](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-ComputeSpec"></a>
The compute resource specification for the recommendation job. You can specify up to 3 instance types to consider, and optionally provide capacity reservation configuration.
Type: [AIRecommendationComputeSpec](API_AIRecommendationComputeSpec.md) object
Required: No

 ** [InferenceSpecification](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-InferenceSpecification"></a>
The inference framework configuration. Specify the framework (such as LMI or vLLM) for the recommendation job.
Type: [AIRecommendationInferenceSpecification](API_AIRecommendationInferenceSpecification.md) object
Required: No

 ** [ModelSource](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-ModelSource"></a>
The source of the model to optimize. Specify the Amazon S3 location of the model artifacts.
Type: [AIModelSource](API_AIModelSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [OptimizeModel](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-OptimizeModel"></a>
Whether to allow model optimization techniques such as quantization, speculative decoding, and kernel tuning. The default is `true`.
Type: Boolean
Required: No

 ** [OutputConfig](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-OutputConfig"></a>
The output configuration for the recommendation job, including the Amazon S3 location for results and an optional model package group where the optimized model is registered.
Type: [AIRecommendationOutputConfig](API_AIRecommendationOutputConfig.md) object
Required: Yes

 ** [PerformanceTarget](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-PerformanceTarget"></a>
The performance targets for the recommendation job. Specify constraints on metrics such as time to first token (`ttft-ms`), `throughput`, or `cost`.
Type: [AIRecommendationPerformanceTarget](API_AIRecommendationPerformanceTarget.md) object
Required: Yes

 ** [RoleArn](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Tags](#API_CreateAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-request-Tags"></a>
The metadata that you apply to AWS resources to help you categorize and organize them.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAIRecommendationJob_ResponseSyntax"></a>

```
{
   "AIRecommendationJobArn": "string"
}
```

## Response Elements
<a name="API_CreateAIRecommendationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AIRecommendationJobArn](#API_CreateAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-CreateAIRecommendationJob-response-AIRecommendationJobArn"></a>
The Amazon Resource Name (ARN) of the created recommendation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:ai-recommendation-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_CreateAIRecommendationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateAIRecommendationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateAIRecommendationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateAIRecommendationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateAIRecommendationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateAIRecommendationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateAIRecommendationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateAIRecommendationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateAIRecommendationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateAIRecommendationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateAIRecommendationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateAIRecommendationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
