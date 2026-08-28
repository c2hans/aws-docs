---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html
---

# CreateInferenceRecommendationsJob
<a name="API_CreateInferenceRecommendationsJob"></a>

Starts a recommendation job. You can create either an instance recommendation or load test job.

## Request Syntax
<a name="API_CreateInferenceRecommendationsJob_RequestSyntax"></a>

```
{
   "InputConfig": {
      "ContainerConfig": {
         "DataInputConfig": "{{string}}",
         "Domain": "{{string}}",
         "Framework": "{{string}}",
         "FrameworkVersion": "{{string}}",
         "NearestModelName": "{{string}}",
         "PayloadConfig": {
            "SamplePayloadUrl": "{{string}}",
            "SupportedContentTypes": [ "{{string}}" ]
         },
         "SupportedEndpointType": "{{string}}",
         "SupportedInstanceTypes": [ "{{string}}" ],
         "SupportedResponseMIMETypes": [ "{{string}}" ],
         "Task": "{{string}}"
      },
      "EndpointConfigurations": [
         {
            "EnvironmentParameterRanges": {
               "CategoricalParameterRanges": [
                  {
                     "Name": "{{string}}",
                     "Value": [ "{{string}}" ]
                  }
               ]
            },
            "InferenceSpecificationName": "{{string}}",
            "InstanceType": "{{string}}",
            "ServerlessConfig": {
               "MaxConcurrency": {{number}},
               "MemorySizeInMB": {{number}},
               "ProvisionedConcurrency": {{number}}
            }
         }
      ],
      "Endpoints": [
         {
            "EndpointName": "{{string}}"
         }
      ],
      "JobDurationInSeconds": {{number}},
      "ModelName": "{{string}}",
      "ModelPackageVersionArn": "{{string}}",
      "ResourceLimit": {
         "MaxNumberOfTests": {{number}},
         "MaxParallelOfTests": {{number}}
      },
      "TrafficPattern": {
         "Phases": [
            {
               "DurationInSeconds": {{number}},
               "InitialNumberOfUsers": {{number}},
               "SpawnRate": {{number}}
            }
         ],
         "Stairs": {
            "DurationInSeconds": {{number}},
            "NumberOfSteps": {{number}},
            "UsersPerStep": {{number}}
         },
         "TrafficType": "{{string}}"
      },
      "VolumeKmsKeyId": "{{string}}",
      "VpcConfig": {
         "SecurityGroupIds": [ "{{string}}" ],
         "Subnets": [ "{{string}}" ]
      }
   },
   "JobDescription": "{{string}}",
   "JobName": "{{string}}",
   "JobType": "{{string}}",
   "OutputConfig": {
      "CompiledOutputConfig": {
         "S3OutputUri": "{{string}}"
      },
      "KmsKeyId": "{{string}}"
   },
   "RoleArn": "{{string}}",
   "StoppingConditions": {
      "FlatInvocations": "{{string}}",
      "MaxInvocations": {{number}},
      "ModelLatencyThresholds": [
         {
            "Percentile": "{{string}}",
            "ValueInMilliseconds": {{number}}
         }
      ]
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateInferenceRecommendationsJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InputConfig](#API_CreateInferenceRecommendationsJob_RequestSyntax) **   <a name="sagemaker-CreateInferenceRecommendationsJob-request-InputConfig"></a>
Provides information about the versioned model package Amazon Resource Name (ARN), the traffic pattern, and endpoint configurations.
Type: [RecommendationJobInputConfig](API_RecommendationJobInputConfig.md) object
Required: Yes

 ** [JobDescription](#API_CreateInferenceRecommendationsJob_RequestSyntax) **   <a name="sagemaker-CreateInferenceRecommendationsJob-request-JobDescription"></a>
Description of the recommendation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [JobName](#API_CreateInferenceRecommendationsJob_RequestSyntax) **   <a name="sagemaker-CreateInferenceRecommendationsJob-request-JobName"></a>
A name for the recommendation job. The name must be unique within the AWS Region and within your AWS account. The job name is passed down to the resources created by the recommendation job. The names of resources (such as the model, endpoint configuration, endpoint, and compilation) that are prefixed with the job name are truncated at 40 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** [JobType](#API_CreateInferenceRecommendationsJob_RequestSyntax) **   <a name="sagemaker-CreateInferenceRecommendationsJob-request-JobType"></a>
Defines the type of recommendation job. Specify `Default` to initiate an instance recommendation and `Advanced` to initiate a load test. If left unspecified, Amazon SageMaker Inference Recommender will run an instance recommendation (`DEFAULT`) job.
Type: String
Valid Values: `Default | Advanced`
Required: Yes

 ** [OutputConfig](#API_CreateInferenceRecommendationsJob_RequestSyntax) **   <a name="sagemaker-CreateInferenceRecommendationsJob-request-OutputConfig"></a>
Provides information about the output artifacts and the KMS key to use for Amazon S3 server-side encryption.
Type: [RecommendationJobOutputConfig](API_RecommendationJobOutputConfig.md) object
Required: No

 ** [RoleArn](#API_CreateInferenceRecommendationsJob_RequestSyntax) **   <a name="sagemaker-CreateInferenceRecommendationsJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [StoppingConditions](#API_CreateInferenceRecommendationsJob_RequestSyntax) **   <a name="sagemaker-CreateInferenceRecommendationsJob-request-StoppingConditions"></a>
A set of conditions for stopping a recommendation job. If any of the conditions are met, the job is automatically stopped.
Type: [RecommendationJobStoppingConditions](API_RecommendationJobStoppingConditions.md) object
Required: No

 ** [Tags](#API_CreateInferenceRecommendationsJob_RequestSyntax) **   <a name="sagemaker-CreateInferenceRecommendationsJob-request-Tags"></a>
The metadata that you apply to AWS resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the AWS General Reference.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateInferenceRecommendationsJob_ResponseSyntax"></a>

```
{
   "JobArn": "string"
}
```

## Response Elements
<a name="API_CreateInferenceRecommendationsJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobArn](#API_CreateInferenceRecommendationsJob_ResponseSyntax) **   <a name="sagemaker-CreateInferenceRecommendationsJob-response-JobArn"></a>
The Amazon Resource Name (ARN) of the recommendation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:inference-recommendations-job/.*`

## Errors
<a name="API_CreateInferenceRecommendationsJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateInferenceRecommendationsJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
