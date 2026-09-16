---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceRecommendationsJob.html
---

# DescribeInferenceRecommendationsJob
<a name="API_DescribeInferenceRecommendationsJob"></a>

Provides the results of the Inference Recommender job. One or more recommendation jobs are returned.

## Request Syntax
<a name="API_DescribeInferenceRecommendationsJob_RequestSyntax"></a>

```
{
   "JobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInferenceRecommendationsJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobName](#API_DescribeInferenceRecommendationsJob_RequestSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-request-JobName"></a>
The name of the job. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: Yes

## Response Syntax
<a name="API_DescribeInferenceRecommendationsJob_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "EndpointPerformances": [
      {
         "EndpointInfo": {
            "EndpointName": "string"
         },
         "Metrics": {
            "MaxInvocations": number,
            "ModelLatency": number
         }
      }
   ],
   "FailureReason": "string",
   "InferenceRecommendations": [
      {
         "EndpointConfiguration": {
            "EndpointName": "string",
            "InitialInstanceCount": number,
            "InstanceType": "string",
            "ServerlessConfig": {
               "MaxConcurrency": number,
               "MemorySizeInMB": number,
               "ProvisionedConcurrency": number
            },
            "VariantName": "string"
         },
         "InvocationEndTime": number,
         "InvocationStartTime": number,
         "Metrics": {
            "CostPerHour": number,
            "CostPerInference": number,
            "CpuUtilization": number,
            "MaxInvocations": number,
            "MemoryUtilization": number,
            "ModelLatency": number,
            "ModelSetupTime": number
         },
         "ModelConfiguration": {
            "CompilationJobName": "string",
            "EnvironmentParameters": [
               {
                  "Key": "string",
                  "Value": "string",
                  "ValueType": "string"
               }
            ],
            "InferenceSpecificationName": "string"
         },
         "RecommendationId": "string"
      }
   ],
   "InputConfig": {
      "ContainerConfig": {
         "DataInputConfig": "string",
         "Domain": "string",
         "Framework": "string",
         "FrameworkVersion": "string",
         "NearestModelName": "string",
         "PayloadConfig": {
            "SamplePayloadUrl": "string",
            "SupportedContentTypes": [ "string" ]
         },
         "SupportedEndpointType": "string",
         "SupportedInstanceTypes": [ "string" ],
         "SupportedResponseMIMETypes": [ "string" ],
         "Task": "string"
      },
      "EndpointConfigurations": [
         {
            "EnvironmentParameterRanges": {
               "CategoricalParameterRanges": [
                  {
                     "Name": "string",
                     "Value": [ "string" ]
                  }
               ]
            },
            "InferenceSpecificationName": "string",
            "InstanceType": "string",
            "ServerlessConfig": {
               "MaxConcurrency": number,
               "MemorySizeInMB": number,
               "ProvisionedConcurrency": number
            }
         }
      ],
      "Endpoints": [
         {
            "EndpointName": "string"
         }
      ],
      "JobDurationInSeconds": number,
      "ModelName": "string",
      "ModelPackageVersionArn": "string",
      "ResourceLimit": {
         "MaxNumberOfTests": number,
         "MaxParallelOfTests": number
      },
      "TrafficPattern": {
         "Phases": [
            {
               "DurationInSeconds": number,
               "InitialNumberOfUsers": number,
               "SpawnRate": number
            }
         ],
         "Stairs": {
            "DurationInSeconds": number,
            "NumberOfSteps": number,
            "UsersPerStep": number
         },
         "TrafficType": "string"
      },
      "VolumeKmsKeyId": "string",
      "VpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "Subnets": [ "string" ]
      }
   },
   "JobArn": "string",
   "JobDescription": "string",
   "JobName": "string",
   "JobType": "string",
   "LastModifiedTime": number,
   "RoleArn": "string",
   "Status": "string",
   "StoppingConditions": {
      "FlatInvocations": "string",
      "MaxInvocations": number,
      "ModelLatencyThresholds": [
         {
            "Percentile": "string",
            "ValueInMilliseconds": number
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeInferenceRecommendationsJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-CreationTime"></a>
A timestamp that shows when the job was created.
Type: Timestamp

 ** [EndpointPerformances](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-EndpointPerformances"></a>
The performance results from running an Inference Recommender job on an existing endpoint.
Type: Array of [EndpointPerformance](API_EndpointPerformance.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [FailureReason](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-FailureReason"></a>
If the job fails, provides information why the job failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [InferenceRecommendations](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-InferenceRecommendations"></a>
The recommendations made by Inference Recommender.
Type: Array of [InferenceRecommendation](API_InferenceRecommendation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [InputConfig](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-InputConfig"></a>
Returns information about the versioned model package Amazon Resource Name (ARN), the traffic pattern, and endpoint configurations you provided when you initiated the job.
Type: [RecommendationJobInputConfig](API_RecommendationJobInputConfig.md) object

 ** [JobArn](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-JobArn"></a>
The Amazon Resource Name (ARN) of the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:inference-recommendations-job/.*`

 ** [JobDescription](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-JobDescription"></a>
The job description that you provided when you initiated the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [JobName](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-JobName"></a>
The name of the job. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`

 ** [JobType](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-JobType"></a>
The job type that you provided when you initiated the job.
Type: String
Valid Values: `Default | Advanced`

 ** [LastModifiedTime](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-LastModifiedTime"></a>
A timestamp that shows when the job was last modified.
Type: Timestamp

 ** [RoleArn](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role you provided when you initiated the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [Status](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-Status"></a>
The status of the job.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | STOPPING | STOPPED | DELETING | DELETED`

 ** [StoppingConditions](#API_DescribeInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRecommendationsJob-response-StoppingConditions"></a>
The stopping conditions that you provided when you initiated the job.
Type: [RecommendationJobStoppingConditions](API_RecommendationJobStoppingConditions.md) object

## Errors
<a name="API_DescribeInferenceRecommendationsJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeInferenceRecommendationsJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)
