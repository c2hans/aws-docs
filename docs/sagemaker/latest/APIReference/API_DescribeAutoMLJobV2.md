---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html
---

# DescribeAutoMLJobV2
<a name="API_DescribeAutoMLJobV2"></a>

Returns information about an AutoML job created by calling [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) or [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html).

## Request Syntax
<a name="API_DescribeAutoMLJobV2_RequestSyntax"></a>

```
{
   "AutoMLJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAutoMLJobV2_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoMLJobName](#API_DescribeAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-request-AutoMLJobName"></a>
Requests information about an AutoML job V2 using its unique name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

## Response Syntax
<a name="API_DescribeAutoMLJobV2_ResponseSyntax"></a>

```
{
   "AutoMLComputeConfig": {
      "EmrServerlessComputeConfig": {
         "ExecutionRoleARN": "string"
      }
   },
   "AutoMLJobArn": "string",
   "AutoMLJobArtifacts": {
      "CandidateDefinitionNotebookLocation": "string",
      "DataExplorationNotebookLocation": "string"
   },
   "AutoMLJobInputDataConfig": [
      {
         "ChannelType": "string",
         "CompressionType": "string",
         "ContentType": "string",
         "DataSource": {
            "S3DataSource": {
               "S3DataType": "string",
               "S3Uri": "string"
            }
         }
      }
   ],
   "AutoMLJobName": "string",
   "AutoMLJobObjective": {
      "MetricName": "string"
   },
   "AutoMLJobSecondaryStatus": "string",
   "AutoMLJobStatus": "string",
   "AutoMLProblemTypeConfig": { ... },
   "AutoMLProblemTypeConfigName": "string",
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
   "DataSplitConfig": {
      "ValidationFraction": number
   },
   "FailureReason": "string",
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
   "ResolvedAttributes": {
      "AutoMLJobObjective": {
         "MetricName": "string"
      },
      "AutoMLProblemTypeResolvedAttributes": { ... },
      "CompletionCriteria": {
         "MaxAutoMLJobRuntimeInSeconds": number,
         "MaxCandidates": number,
         "MaxRuntimePerTrainingJobInSeconds": number
      }
   },
   "RoleArn": "string",
   "SecurityConfig": {
      "EnableInterContainerTrafficEncryption": boolean,
      "VolumeKmsKeyId": "string",
      "VpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "Subnets": [ "string" ]
      }
   }
}
```

## Response Elements
<a name="API_DescribeAutoMLJobV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoMLComputeConfig](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-AutoMLComputeConfig"></a>
The compute configuration used for the AutoML job V2.
Type: [AutoMLComputeConfig](API_AutoMLComputeConfig.md) object

 ** [AutoMLJobArn](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-AutoMLJobArn"></a>
Returns the Amazon Resource Name (ARN) of the AutoML job V2.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`

 ** [AutoMLJobArtifacts](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-AutoMLJobArtifacts"></a>
The artifacts that are generated during an AutoML job.
Type: [AutoMLJobArtifacts](API_AutoMLJobArtifacts.md) object

 ** [AutoMLJobInputDataConfig](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-AutoMLJobInputDataConfig"></a>
Returns an array of channel objects describing the input data and their location.
Type: Array of [AutoMLJobChannel](API_AutoMLJobChannel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [AutoMLJobName](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-AutoMLJobName"></a>
Returns the name of the AutoML job V2.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`

 ** [AutoMLJobObjective](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-AutoMLJobObjective"></a>
Returns the job's objective.
Type: [AutoMLJobObjective](API_AutoMLJobObjective.md) object

 ** [AutoMLJobSecondaryStatus](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-AutoMLJobSecondaryStatus"></a>
Returns the secondary status of the AutoML job V2.
Type: String
Valid Values: `Starting | MaxCandidatesReached | Failed | Stopped | MaxAutoMLJobRuntimeReached | Stopping | CandidateDefinitionsGenerated | Completed | ExplainabilityError | DeployingModel | ModelDeploymentError | GeneratingModelInsightsReport | ModelInsightsError | AnalyzingData | FeatureEngineering | ModelTuning | GeneratingExplainabilityReport | TrainingModels | PreTraining`

 ** [AutoMLJobStatus](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-AutoMLJobStatus"></a>
Returns the status of the AutoML job V2.
Type: String
Valid Values: `Completed | InProgress | Failed | Stopped | Stopping`

 ** [AutoMLProblemTypeConfig](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-AutoMLProblemTypeConfig"></a>
Returns the configuration settings of the problem type set for the AutoML job V2.
Type: [AutoMLProblemTypeConfig](API_AutoMLProblemTypeConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [AutoMLProblemTypeConfigName](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-AutoMLProblemTypeConfigName"></a>
Returns the name of the problem type configuration set for the AutoML job V2.
Type: String
Valid Values: `ImageClassification | TextClassification | TimeSeriesForecasting | Tabular | TextGeneration`

 ** [BestCandidate](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-BestCandidate"></a>
Information about the candidate produced by an AutoML training job V2, including its status, steps, and other properties.
Type: [AutoMLCandidate](API_AutoMLCandidate.md) object

 ** [DataSplitConfig](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-DataSplitConfig"></a>
Returns the configuration settings of how the data are split into train and validation datasets.
Type: [AutoMLDataSplitConfig](API_AutoMLDataSplitConfig.md) object

 ** [FailureReason](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-FailureReason"></a>
Returns the reason for the failure of the AutoML job V2, when applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [ModelDeployConfig](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-ModelDeployConfig"></a>
Indicates whether the model was deployed automatically to an endpoint and the name of that endpoint if deployed automatically.
Type: [ModelDeployConfig](API_ModelDeployConfig.md) object

 ** [ModelDeployResult](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-ModelDeployResult"></a>
Provides information about endpoint for the model deployment.
Type: [ModelDeployResult](API_ModelDeployResult.md) object

 ** [OutputDataConfig](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-OutputDataConfig"></a>
Returns the job's output data config.
Type: [AutoMLOutputDataConfig](API_AutoMLOutputDataConfig.md) object

 ** [PartialFailureReasons](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-PartialFailureReasons"></a>
Returns a list of reasons for partial failures within an AutoML job V2.
Type: Array of [AutoMLPartialFailureReason](API_AutoMLPartialFailureReason.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [ResolvedAttributes](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-ResolvedAttributes"></a>
Returns the resolved attributes used by the AutoML job V2.
Type: [AutoMLResolvedAttributes](API_AutoMLResolvedAttributes.md) object

 ** [RoleArn](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-RoleArn"></a>
The ARN of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [SecurityConfig](#API_DescribeAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-DescribeAutoMLJobV2-response-SecurityConfig"></a>
Returns the security configuration for traffic encryption or Amazon VPC settings.
Type: [AutoMLSecurityConfig](API_AutoMLSecurityConfig.md) object

## Errors
<a name="API_DescribeAutoMLJobV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAutoMLJobV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeAutoMLJobV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeAutoMLJobV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeAutoMLJobV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeAutoMLJobV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeAutoMLJobV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeAutoMLJobV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeAutoMLJobV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeAutoMLJobV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeAutoMLJobV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeAutoMLJobV2)
