---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAIRecommendationJob.html
---

# DescribeAIRecommendationJob
<a name="API_DescribeAIRecommendationJob"></a>

Returns details of an AI recommendation job, including its status, model source, performance targets, optimization recommendations, and deployment configurations.

## Request Syntax
<a name="API_DescribeAIRecommendationJob_RequestSyntax"></a>

```
{
   "AIRecommendationJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAIRecommendationJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AIRecommendationJobName](#API_DescribeAIRecommendationJob_RequestSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-request-AIRecommendationJobName"></a>
The name of the AI recommendation job to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeAIRecommendationJob_ResponseSyntax"></a>

```
{
   "AdapterSource": { ... },
   "AIRecommendationJobArn": "string",
   "AIRecommendationJobName": "string",
   "AIRecommendationJobStatus": "string",
   "AIWorkloadConfigIdentifier": "string",
   "ComputeSpec": {
      "CapacityReservationConfig": {
         "CapacityReservationPreference": "string",
         "MlReservationArns": [ "string" ]
      },
      "InstanceTypes": [ "string" ]
   },
   "CreationTime": number,
   "EndTime": number,
   "FailureReason": "string",
   "InferenceSpecification": {
      "Framework": "string"
   },
   "ModelSource": { ... },
   "OptimizeModel": boolean,
   "OutputConfig": {
      "MlflowConfig": {
         "MlflowExperimentName": "string",
         "MlflowResourceArn": "string",
         "MlflowRunName": "string"
      },
      "ModelPackageGroupIdentifier": "string",
      "S3OutputLocation": "string"
   },
   "PerformanceTarget": {
      "Constraints": [
         {
            "Metric": "string"
         }
      ]
   },
   "Recommendations": [
      {
         "AdapterDetails": {
            "ModelPackageArns": [
               {
                  "AdapterId": "string",
                  "ModelPackageArn": "string"
               }
            ],
            "S3Uris": [
               {
                  "AdapterId": "string",
                  "S3Uri": "string"
               }
            ]
         },
         "AIBenchmarkJobArn": "string",
         "DeploymentConfiguration": {
            "CopyCountPerInstance": number,
            "EnvironmentVariables": {
               "string" : "string"
            },
            "ImageUri": "string",
            "InstanceCount": number,
            "InstanceType": "string",
            "MinCpuMemoryRequiredInMb": number,
            "S3": [
               {
                  "ChannelName": "string",
                  "Uri": "string"
               }
            ]
         },
         "ExpectedPerformance": [
            {
               "Metric": "string",
               "Stat": "string",
               "Unit": "string",
               "Value": "string"
            }
         ],
         "ModelDetails": {
            "InferenceSpecificationName": "string",
            "InstanceDetails": [
               {
                  "CopyCountPerInstance": number,
                  "InstanceCount": number,
                  "InstanceType": "string"
               }
            ],
            "ModelPackageArn": "string"
         },
         "OptimizationDetails": [
            {
               "OptimizationConfig": {
                  "string" : "string"
               },
               "OptimizationType": "string"
            }
         ],
         "RecommendationDescription": "string"
      }
   ],
   "RoleArn": "string",
   "StartTime": number,
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAIRecommendationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdapterSource](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-AdapterSource"></a>
The LoRA adapter source that you specified when you created the recommendation job. This field is absent when you created the job without LoRA adapters.
Type: [AIAdapterSource](API_AIAdapterSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [AIRecommendationJobArn](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-AIRecommendationJobArn"></a>
The Amazon Resource Name (ARN) of the AI recommendation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:ai-recommendation-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [AIRecommendationJobName](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-AIRecommendationJobName"></a>
The name of the AI recommendation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [AIRecommendationJobStatus](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-AIRecommendationJobStatus"></a>
The status of the AI recommendation job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`

 ** [AIWorkloadConfigIdentifier](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-AIWorkloadConfigIdentifier"></a>
The name or Amazon Resource Name (ARN) of the AI workload configuration used for this recommendation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*/)?([a-zA-Z0-9]([a-zA-Z0-9\-]){0,62})(?<!-)`

 ** [ComputeSpec](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-ComputeSpec"></a>
The compute resource specification for the recommendation job.
Type: [AIRecommendationComputeSpec](API_AIRecommendationComputeSpec.md) object

 ** [CreationTime](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-CreationTime"></a>
A timestamp that indicates when the recommendation job was created.
Type: Timestamp

 ** [EndTime](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-EndTime"></a>
A timestamp that indicates when the recommendation job completed.
Type: Timestamp

 ** [FailureReason](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-FailureReason"></a>
If the recommendation job failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [InferenceSpecification](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-InferenceSpecification"></a>
The inference framework configuration.
Type: [AIRecommendationInferenceSpecification](API_AIRecommendationInferenceSpecification.md) object

 ** [ModelSource](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-ModelSource"></a>
The source of the model that was analyzed.
Type: [AIModelSource](API_AIModelSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [OptimizeModel](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-OptimizeModel"></a>
Whether model optimization techniques were allowed.
Type: Boolean

 ** [OutputConfig](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-OutputConfig"></a>
The output configuration for the recommendation job.
Type: [AIRecommendationOutputResult](API_AIRecommendationOutputResult.md) object

 ** [PerformanceTarget](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-PerformanceTarget"></a>
The performance targets specified for the recommendation job.
Type: [AIRecommendationPerformanceTarget](API_AIRecommendationPerformanceTarget.md) object

 ** [Recommendations](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-Recommendations"></a>
The list of optimization recommendations generated by the job. Each recommendation includes optimization details, deployment configuration, expected performance metrics, and the associated benchmark job ARN.
Type: Array of [AIRecommendation](API_AIRecommendation.md) objects

 ** [RoleArn](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used by the recommendation job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [StartTime](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-StartTime"></a>
A timestamp that indicates when the recommendation job started running.
Type: Timestamp

 ** [Tags](#API_DescribeAIRecommendationJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIRecommendationJob-response-Tags"></a>
The tags associated with the recommendation job.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_DescribeAIRecommendationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAIRecommendationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeAIRecommendationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeAIRecommendationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeAIRecommendationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeAIRecommendationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeAIRecommendationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeAIRecommendationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeAIRecommendationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeAIRecommendationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeAIRecommendationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeAIRecommendationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
