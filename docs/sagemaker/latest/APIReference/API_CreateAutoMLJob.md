---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html
---

# CreateAutoMLJob
<a name="API_CreateAutoMLJob"></a>

Creates an Autopilot job also referred to as Autopilot experiment or AutoML job.

An AutoML job in SageMaker AI is a fully automated process that allows you to build machine learning models with minimal effort and machine learning expertise. When initiating an AutoML job, you provide your data and optionally specify parameters tailored to your use case. SageMaker AI then automates the entire model development lifecycle, including data preprocessing, model training, tuning, and evaluation. AutoML jobs are designed to simplify and accelerate the model building process by automating various tasks and exploring different combinations of machine learning algorithms, data preprocessing techniques, and hyperparameter values. The output of an AutoML job comprises one or more trained models ready for deployment and inference. Additionally, SageMaker AI AutoML jobs generate a candidate model leaderboard, allowing you to select the best-performing model for deployment.

For more information about AutoML jobs, see [https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) in the SageMaker AI developer guide.

**Note**
We recommend using the new versions [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) and [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html), which offer backward compatibility.
 `CreateAutoMLJobV2` can manage tabular problem types identical to those of its previous version `CreateAutoMLJob`, as well as time-series forecasting, non-tabular problem types such as image or text classification, and text generation (LLMs fine-tuning).
Find guidelines about how to migrate a `CreateAutoMLJob` to `CreateAutoMLJobV2` in [Migrate a CreateAutoMLJob to CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html#autopilot-create-experiment-api-migrate-v1-v2).

You can find the best-performing model after you run an AutoML job by calling [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html) (recommended) or [DescribeAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html).

## Request Syntax
<a name="API_CreateAutoMLJob_RequestSyntax"></a>

```
{
   "AutoMLJobConfig": {
      "CandidateGenerationConfig": {
         "AlgorithmsConfig": [
            {
               "AutoMLAlgorithms": [ "{{string}}" ]
            }
         ],
         "FeatureSpecificationS3Uri": "{{string}}"
      },
      "CompletionCriteria": {
         "MaxAutoMLJobRuntimeInSeconds": {{number}},
         "MaxCandidates": {{number}},
         "MaxRuntimePerTrainingJobInSeconds": {{number}}
      },
      "DataSplitConfig": {
         "ValidationFraction": {{number}}
      },
      "Mode": "{{string}}",
      "SecurityConfig": {
         "EnableInterContainerTrafficEncryption": {{boolean}},
         "VolumeKmsKeyId": "{{string}}",
         "VpcConfig": {
            "SecurityGroupIds": [ "{{string}}" ],
            "Subnets": [ "{{string}}" ]
         }
      }
   },
   "AutoMLJobName": "{{string}}",
   "AutoMLJobObjective": {
      "MetricName": "{{string}}"
   },
   "GenerateCandidateDefinitionsOnly": {{boolean}},
   "InputDataConfig": [
      {
         "ChannelType": "{{string}}",
         "CompressionType": "{{string}}",
         "ContentType": "{{string}}",
         "DataSource": {
            "S3DataSource": {
               "S3DataType": "{{string}}",
               "S3Uri": "{{string}}"
            }
         },
         "SampleWeightAttributeName": "{{string}}",
         "TargetAttributeName": "{{string}}"
      }
   ],
   "ModelDeployConfig": {
      "AutoGenerateEndpointName": {{boolean}},
      "EndpointName": "{{string}}"
   },
   "OutputDataConfig": {
      "KmsKeyId": "{{string}}",
      "S3OutputPath": "{{string}}"
   },
   "ProblemType": "{{string}}",
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
<a name="API_CreateAutoMLJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoMLJobConfig](#API_CreateAutoMLJob_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJob-request-AutoMLJobConfig"></a>
A collection of settings used to configure an AutoML job.
Type: [AutoMLJobConfig](API_AutoMLJobConfig.md) object
Required: No

 ** [AutoMLJobName](#API_CreateAutoMLJob_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJob-request-AutoMLJobName"></a>
Identifies an Autopilot job. The name must be unique to your account and is case insensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

 ** [AutoMLJobObjective](#API_CreateAutoMLJob_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJob-request-AutoMLJobObjective"></a>
Specifies a metric to minimize or maximize as the objective of a job. If not specified, the default objective metric depends on the problem type. See [AutoMLJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html) for the default values.
Type: [AutoMLJobObjective](API_AutoMLJobObjective.md) object
Required: No

 ** [GenerateCandidateDefinitionsOnly](#API_CreateAutoMLJob_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJob-request-GenerateCandidateDefinitionsOnly"></a>
Generates possible candidates without training the models. A candidate is a combination of data preprocessors, algorithms, and algorithm parameter settings.
Type: Boolean
Required: No

 ** [InputDataConfig](#API_CreateAutoMLJob_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJob-request-InputDataConfig"></a>
An array of channel objects that describes the input data and its location. Each channel is a named input source. Similar to `InputDataConfig` supported by [HyperParameterTrainingJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html). Format(s) supported: CSV, Parquet. A minimum of 500 rows is required for the training dataset. There is not a minimum number of rows required for the validation dataset.
Type: Array of [AutoMLChannel](API_AutoMLChannel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** [ModelDeployConfig](#API_CreateAutoMLJob_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJob-request-ModelDeployConfig"></a>
Specifies how to generate the endpoint name for an automatic one-click Autopilot model deployment.
Type: [ModelDeployConfig](API_ModelDeployConfig.md) object
Required: No

 ** [OutputDataConfig](#API_CreateAutoMLJob_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJob-request-OutputDataConfig"></a>
Provides information about encryption and the Amazon S3 output path needed to store artifacts from an AutoML job. Format(s) supported: CSV.
Type: [AutoMLOutputDataConfig](API_AutoMLOutputDataConfig.md) object
Required: Yes

 ** [ProblemType](#API_CreateAutoMLJob_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJob-request-ProblemType"></a>
Defines the type of supervised learning problem available for the candidates. For more information, see [ SageMaker Autopilot problem types](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-problem-types).
Type: String
Valid Values: `BinaryClassification | MulticlassClassification | Regression`
Required: No

 ** [RoleArn](#API_CreateAutoMLJob_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJob-request-RoleArn"></a>
The ARN of the role that is used to access the data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Tags](#API_CreateAutoMLJob_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJob-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWSResources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html). Tag keys must be unique per resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAutoMLJob_ResponseSyntax"></a>

```
{
   "AutoMLJobArn": "string"
}
```

## Response Elements
<a name="API_CreateAutoMLJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoMLJobArn](#API_CreateAutoMLJob_ResponseSyntax) **   <a name="sagemaker-CreateAutoMLJob-response-AutoMLJobArn"></a>
The unique ARN assigned to the AutoML job when it is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`

## Errors
<a name="API_CreateAutoMLJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateAutoMLJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateAutoMLJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateAutoMLJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateAutoMLJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateAutoMLJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateAutoMLJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateAutoMLJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateAutoMLJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateAutoMLJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateAutoMLJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateAutoMLJob)
