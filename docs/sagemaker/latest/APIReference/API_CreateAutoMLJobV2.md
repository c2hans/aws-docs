---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html
---

# CreateAutoMLJobV2
<a name="API_CreateAutoMLJobV2"></a>

Creates an Autopilot job also referred to as Autopilot experiment or AutoML job V2.

An AutoML job in SageMaker AI is a fully automated process that allows you to build machine learning models with minimal effort and machine learning expertise. When initiating an AutoML job, you provide your data and optionally specify parameters tailored to your use case. SageMaker AI then automates the entire model development lifecycle, including data preprocessing, model training, tuning, and evaluation. AutoML jobs are designed to simplify and accelerate the model building process by automating various tasks and exploring different combinations of machine learning algorithms, data preprocessing techniques, and hyperparameter values. The output of an AutoML job comprises one or more trained models ready for deployment and inference. Additionally, SageMaker AI AutoML jobs generate a candidate model leaderboard, allowing you to select the best-performing model for deployment.

For more information about AutoML jobs, see [https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) in the SageMaker AI developer guide.

AutoML jobs V2 support various problem types such as regression, binary, and multiclass classification with tabular data, text and image classification, time-series forecasting, and fine-tuning of large language models (LLMs) for text generation.

**Note**
 [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) and [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html) are new versions of [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html) and [DescribeAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html) which offer backward compatibility.
 `CreateAutoMLJobV2` can manage tabular problem types identical to those of its previous version `CreateAutoMLJob`, as well as time-series forecasting, non-tabular problem types such as image or text classification, and text generation (LLMs fine-tuning).
Find guidelines about how to migrate a `CreateAutoMLJob` to `CreateAutoMLJobV2` in [Migrate a CreateAutoMLJob to CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html#autopilot-create-experiment-api-migrate-v1-v2).

For the list of available problem types supported by `CreateAutoMLJobV2`, see [AutoMLProblemTypeConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeConfig.html).

You can find the best-performing model after you run an AutoML job V2 by calling [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html).

## Request Syntax
<a name="API_CreateAutoMLJobV2_RequestSyntax"></a>

```
{
   "AutoMLComputeConfig": {
      "EmrServerlessComputeConfig": {
         "ExecutionRoleARN": "{{string}}"
      }
   },
   "AutoMLJobInputDataConfig": [
      {
         "ChannelType": "{{string}}",
         "CompressionType": "{{string}}",
         "ContentType": "{{string}}",
         "DataSource": {
            "S3DataSource": {
               "S3DataType": "{{string}}",
               "S3Uri": "{{string}}"
            }
         }
      }
   ],
   "AutoMLJobName": "{{string}}",
   "AutoMLJobObjective": {
      "MetricName": "{{string}}"
   },
   "AutoMLProblemTypeConfig": { ... },
   "DataSplitConfig": {
      "ValidationFraction": {{number}}
   },
   "ModelDeployConfig": {
      "AutoGenerateEndpointName": {{boolean}},
      "EndpointName": "{{string}}"
   },
   "OutputDataConfig": {
      "KmsKeyId": "{{string}}",
      "S3OutputPath": "{{string}}"
   },
   "RoleArn": "{{string}}",
   "SecurityConfig": {
      "EnableInterContainerTrafficEncryption": {{boolean}},
      "VolumeKmsKeyId": "{{string}}",
      "VpcConfig": {
         "SecurityGroupIds": [ "{{string}}" ],
         "Subnets": [ "{{string}}" ]
      }
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
<a name="API_CreateAutoMLJobV2_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoMLComputeConfig](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-AutoMLComputeConfig"></a>
Specifies the compute configuration for the AutoML job V2.
Type: [AutoMLComputeConfig](API_AutoMLComputeConfig.md) object
Required: No

 ** [AutoMLJobInputDataConfig](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-AutoMLJobInputDataConfig"></a>
An array of channel objects describing the input data and their location. Each channel is a named input source. Similar to the [InputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-InputDataConfig) attribute in the `CreateAutoMLJob` input parameters. The supported formats depend on the problem type:
+ For tabular problem types: `S3Prefix`, `ManifestFile`.
+ For image classification: `S3Prefix`, `ManifestFile`, `AugmentedManifestFile`.
+ For text classification: `S3Prefix`.
+ For time-series forecasting: `S3Prefix`.
+ For text generation (LLMs fine-tuning): `S3Prefix`.
Type: Array of [AutoMLJobChannel](API_AutoMLJobChannel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** [AutoMLJobName](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-AutoMLJobName"></a>
Identifies an Autopilot job. The name must be unique to your account and is case insensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

 ** [AutoMLJobObjective](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-AutoMLJobObjective"></a>
Specifies a metric to minimize or maximize as the objective of a job. If not specified, the default objective metric depends on the problem type. For the list of default values per problem type, see [AutoMLJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html).
+ For tabular problem types: You must either provide both the `AutoMLJobObjective` and indicate the type of supervised learning problem in `AutoMLProblemTypeConfig` (`TabularJobConfig.ProblemType`), or none at all.
+ For text generation problem types (LLMs fine-tuning): Fine-tuning language models in Autopilot does not require setting the `AutoMLJobObjective` field. Autopilot fine-tunes LLMs without requiring multiple candidates to be trained and evaluated. Instead, using your dataset, Autopilot directly fine-tunes your target model to enhance a default objective metric, the cross-entropy loss. After fine-tuning a language model, you can evaluate the quality of its generated text using different metrics. For a list of the available metrics, see [Metrics for fine-tuning LLMs in Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-metrics.html).
Type: [AutoMLJobObjective](API_AutoMLJobObjective.md) object
Required: No

 ** [AutoMLProblemTypeConfig](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-AutoMLProblemTypeConfig"></a>
Defines the configuration settings of one of the supported problem types.
Type: [AutoMLProblemTypeConfig](API_AutoMLProblemTypeConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [DataSplitConfig](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-DataSplitConfig"></a>
This structure specifies how to split the data into train and validation datasets.
The validation and training datasets must contain the same headers. For jobs created by calling `CreateAutoMLJob`, the validation dataset must be less than 2 GB in size.
This attribute must not be set for the time-series forecasting problem type, as Autopilot automatically splits the input dataset into training and validation sets.
Type: [AutoMLDataSplitConfig](API_AutoMLDataSplitConfig.md) object
Required: No

 ** [ModelDeployConfig](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-ModelDeployConfig"></a>
Specifies how to generate the endpoint name for an automatic one-click Autopilot model deployment.
Type: [ModelDeployConfig](API_ModelDeployConfig.md) object
Required: No

 ** [OutputDataConfig](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-OutputDataConfig"></a>
Provides information about encryption and the Amazon S3 output path needed to store artifacts from an AutoML job.
Type: [AutoMLOutputDataConfig](API_AutoMLOutputDataConfig.md) object
Required: Yes

 ** [RoleArn](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-RoleArn"></a>
The ARN of the role that is used to access the data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [SecurityConfig](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-SecurityConfig"></a>
The security configuration for traffic encryption or Amazon VPC settings.
Type: [AutoMLSecurityConfig](API_AutoMLSecurityConfig.md) object
Required: No

 ** [Tags](#API_CreateAutoMLJobV2_RequestSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, such as by purpose, owner, or environment. For more information, see [Tagging AWSResources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html). Tag keys must be unique per resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAutoMLJobV2_ResponseSyntax"></a>

```
{
   "AutoMLJobArn": "string"
}
```

## Response Elements
<a name="API_CreateAutoMLJobV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoMLJobArn](#API_CreateAutoMLJobV2_ResponseSyntax) **   <a name="sagemaker-CreateAutoMLJobV2-response-AutoMLJobArn"></a>
The unique ARN assigned to the AutoMLJob when it is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`

## Errors
<a name="API_CreateAutoMLJobV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateAutoMLJobV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateAutoMLJobV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateAutoMLJobV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateAutoMLJobV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateAutoMLJobV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateAutoMLJobV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateAutoMLJobV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateAutoMLJobV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateAutoMLJobV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateAutoMLJobV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateAutoMLJobV2)
