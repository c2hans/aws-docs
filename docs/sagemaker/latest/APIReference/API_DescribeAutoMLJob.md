---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html
---

# DescribeAutoMLJob
<a name="API_DescribeAutoMLJob"></a>

Returns information about an AutoML job created by calling [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html).

**Note**
AutoML jobs created by calling [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) cannot be described by `DescribeAutoMLJob`.

## Request Syntax
<a name="API_DescribeAutoMLJob_RequestSyntax"></a>

```
{
   "AutoMLJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAutoMLJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoMLJobName](#API_DescribeAutoMLJob_RequestSyntax) **   <a name="sagemaker-DescribeAutoMLJob-request-AutoMLJobName"></a>
Requests information about an AutoML job using its unique name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

## Response Syntax
<a name="API_DescribeAutoMLJob_ResponseSyntax"></a>

```
{
   "AutoMLJobArn": "string",
   "AutoMLJobArtifacts": {
      "CandidateDefinitionNotebookLocation": "string",
      "DataExplorationNotebookLocation": "string"
   },
   "AutoMLJobConfig": {
      "CandidateGenerationConfig": {
         "AlgorithmsConfig": [
            {
               "AutoMLAlgorithms": [ "string" ]
            }
         ],
         "FeatureSpecificationS3Uri": "string"
      },
      "CompletionCriteria": {
         "MaxAutoMLJobRuntimeInSeconds": number,
         "MaxCandidates": number,
         "MaxRuntimePerTrainingJobInSeconds": number
      },
      "DataSplitConfig": {
         "ValidationFraction": number
      },
      "Mode": "string",
      "SecurityConfig": {
         "EnableInterContainerTrafficEncryption": boolean,
         "VolumeKmsKeyId": "string",
         "VpcConfig": {
            "SecurityGroupIds": [ "string" ],
            "Subnets": [ "string" ]
         }
      }
   },
   "AutoMLJobName": "string",
   "AutoMLJobObjective": {
      "MetricName": "string"
   },
   "AutoMLJobSecondaryStatus": "string",
   "AutoMLJobStatus": "string",
   "BestCandidate": {
      "CandidateName": "string",
      "CandidateProperties": {
         "CandidateArtifactLocations": {
            "BacktestResults": "string",
            "Explainability": "string",
            "ModelInsights": "string"
         },
         "CandidateMetrics": [
            {
               "MetricName": "string",
               "Set": "string",
               "StandardMetricName": "string",
               "Value": number
            }
         ]
      },
      "CandidateStatus": "string",
      "CandidateSteps": [
         {
            "CandidateStepArn": "string",
            "CandidateStepName": "string",
            "CandidateStepType": "string"
         }
      ],
      "FailureReason": "string",
      "FinalAutoMLJobObjectiveMetric": {
         "MetricName": "string",
         "StandardMetricName": "string",
         "Type": "string",
         "Value": number
      },
      "InferenceContainerDefinitions": {
         "string" : [
            {
               "Environment": {
                  "string" : "string"
               },
               "Image": "string",
               "ModelDataUrl": "string"
            }
         ]
      },
      "InferenceContainers": [
         {
            "Environment": {
               "string" : "string"
            },
            "Image": "string",
            "ModelDataUrl": "string"
         }
      ],
      "ObjectiveStatus": "string"
   },
   "FailureReason": "string",
   "GenerateCandidateDefinitionsOnly": boolean,
   "InputDataConfig": [
      {
         "ChannelType": "string",
         "CompressionType": "string",
         "ContentType": "string",
         "DataSource": {
            "S3DataSource": {
               "S3DataType": "string",
               "S3Uri": "string"
            }
         },
         "SampleWeightAttributeName": "string",
         "TargetAttributeName": "string"
      }
   ],
   "ModelDeployConfig": {
      "AutoGenerateEndpointName": boolean,
      "EndpointName": "string"
   },
   "ModelDeployResult": {
      "EndpointName": "string"
   },
   "OutputDataConfig": {
      "KmsKeyId": "string",
      "S3OutputPath": "string"
   },
   "PartialFailureReasons": [
      {
         "PartialFailureMessage": "string"
      }
   ],
   "ProblemType": "string",
   "ResolvedAttributes": {
      "AutoMLJobObjective": {
         "MetricName": "string"
      },
      "CompletionCriteria": {
         "MaxAutoMLJobRuntimeInSeconds": number,
         "MaxCandidates": number,
         "MaxRuntimePerTrainingJobInSeconds": number
      },
      "ProblemType": "string"
   },
   "RoleArn": "string"
}
```

## Response Elements
<a name="API_DescribeAutoMLJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoMLJobArn](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-AutoMLJobArn"></a>
Returns the ARN of the AutoML job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`

 ** [AutoMLJobArtifacts](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-AutoMLJobArtifacts"></a>
Returns information on the job's artifacts found in `AutoMLJobArtifacts`.
Type: [AutoMLJobArtifacts](API_AutoMLJobArtifacts.md) object

 ** [AutoMLJobConfig](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-AutoMLJobConfig"></a>
Returns the configuration for the AutoML job.
Type: [AutoMLJobConfig](API_AutoMLJobConfig.md) object

 ** [AutoMLJobName](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-AutoMLJobName"></a>
Returns the name of the AutoML job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`

 ** [AutoMLJobObjective](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-AutoMLJobObjective"></a>
Returns the job's objective.
Type: [AutoMLJobObjective](API_AutoMLJobObjective.md) object

 ** [AutoMLJobSecondaryStatus](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-AutoMLJobSecondaryStatus"></a>
Returns the secondary status of the AutoML job.
Type: String
Valid Values: `Starting | MaxCandidatesReached | Failed | Stopped | MaxAutoMLJobRuntimeReached | Stopping | CandidateDefinitionsGenerated | Completed | ExplainabilityError | DeployingModel | ModelDeploymentError | GeneratingModelInsightsReport | ModelInsightsError | AnalyzingData | FeatureEngineering | ModelTuning | GeneratingExplainabilityReport | TrainingModels | PreTraining`

 ** [AutoMLJobStatus](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-AutoMLJobStatus"></a>
Returns the status of the AutoML job.
Type: String
Valid Values: `Completed | InProgress | Failed | Stopped | Stopping`

 ** [BestCandidate](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-BestCandidate"></a>
The best model candidate selected by SageMaker AI Autopilot using both the best objective metric and lowest [InferenceLatency](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html) for an experiment.
Type: [AutoMLCandidate](API_AutoMLCandidate.md) object

 ** [FailureReason](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-FailureReason"></a>
Returns the failure reason for an AutoML job, when applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [GenerateCandidateDefinitionsOnly](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-GenerateCandidateDefinitionsOnly"></a>
Indicates whether the output for an AutoML job generates candidate definitions only.
Type: Boolean

 ** [InputDataConfig](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-InputDataConfig"></a>
Returns the input data configuration for the AutoML job.
Type: Array of [AutoMLChannel](API_AutoMLChannel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [ModelDeployConfig](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-ModelDeployConfig"></a>
Indicates whether the model was deployed automatically to an endpoint and the name of that endpoint if deployed automatically.
Type: [ModelDeployConfig](API_ModelDeployConfig.md) object

 ** [ModelDeployResult](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-ModelDeployResult"></a>
Provides information about endpoint for the model deployment.
Type: [ModelDeployResult](API_ModelDeployResult.md) object

 ** [OutputDataConfig](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-OutputDataConfig"></a>
Returns the job's output data config.
Type: [AutoMLOutputDataConfig](API_AutoMLOutputDataConfig.md) object

 ** [PartialFailureReasons](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-PartialFailureReasons"></a>
Returns a list of reasons for partial failures within an AutoML job.
Type: Array of [AutoMLPartialFailureReason](API_AutoMLPartialFailureReason.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [ProblemType](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-ProblemType"></a>
Returns the job's problem type.
Type: String
Valid Values: `BinaryClassification | MulticlassClassification | Regression`

 ** [ResolvedAttributes](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-ResolvedAttributes"></a>
Contains `ProblemType`, `AutoMLJobObjective`, and `CompletionCriteria`. If you do not provide these values, they are inferred.
Type: [ResolvedAttributes](API_ResolvedAttributes.md) object

 ** [RoleArn](#API_DescribeAutoMLJob_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJob-response-RoleArn"></a>
The ARN of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

## Errors
<a name="API_DescribeAutoMLJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAutoMLJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeAutoMLJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeAutoMLJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeAutoMLJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeAutoMLJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeAutoMLJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeAutoMLJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeAutoMLJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeAutoMLJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeAutoMLJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeAutoMLJob)
