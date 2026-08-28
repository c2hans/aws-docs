---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelExplainabilityJobDefinition.html
---

# CreateModelExplainabilityJobDefinition
<a name="API_CreateModelExplainabilityJobDefinition"></a>

Creates the definition for a model explainability job.

## Request Syntax
<a name="API_CreateModelExplainabilityJobDefinition_RequestSyntax"></a>

```
{
   "JobDefinitionName": "{{string}}",
   "JobResources": {
      "ClusterConfig": {
         "InstanceCount": {{number}},
         "InstanceType": "{{string}}",
         "VolumeKmsKeyId": "{{string}}",
         "VolumeSizeInGB": {{number}}
      }
   },
   "ModelExplainabilityAppSpecification": {
      "ConfigUri": "{{string}}",
      "Environment": {
         "{{string}}" : "{{string}}"
      },
      "ImageUri": "{{string}}"
   },
   "ModelExplainabilityBaselineConfig": {
      "BaseliningJobName": "{{string}}",
      "ConstraintsResource": {
         "S3Uri": "{{string}}"
      }
   },
   "ModelExplainabilityJobInput": {
      "BatchTransformInput": {
         "DataCapturedDestinationS3Uri": "{{string}}",
         "DatasetFormat": {
            "Csv": {
               "Header": {{boolean}}
            },
            "Json": {
               "Line": {{boolean}}
            },
            "Parquet": {
            }
         },
         "EndTimeOffset": "{{string}}",
         "ExcludeFeaturesAttribute": "{{string}}",
         "FeaturesAttribute": "{{string}}",
         "InferenceAttribute": "{{string}}",
         "LocalPath": "{{string}}",
         "ProbabilityAttribute": "{{string}}",
         "ProbabilityThresholdAttribute": {{number}},
         "S3DataDistributionType": "{{string}}",
         "S3InputMode": "{{string}}",
         "StartTimeOffset": "{{string}}"
      },
      "EndpointInput": {
         "EndpointName": "{{string}}",
         "EndTimeOffset": "{{string}}",
         "ExcludeFeaturesAttribute": "{{string}}",
         "FeaturesAttribute": "{{string}}",
         "InferenceAttribute": "{{string}}",
         "LocalPath": "{{string}}",
         "ProbabilityAttribute": "{{string}}",
         "ProbabilityThresholdAttribute": {{number}},
         "S3DataDistributionType": "{{string}}",
         "S3InputMode": "{{string}}",
         "StartTimeOffset": "{{string}}"
      }
   },
   "ModelExplainabilityJobOutputConfig": {
      "KmsKeyId": "{{string}}",
      "MonitoringOutputs": [
         {
            "S3Output": {
               "LocalPath": "{{string}}",
               "S3UploadMode": "{{string}}",
               "S3Uri": "{{string}}"
            }
         }
      ]
   },
   "NetworkConfig": {
      "EnableInterContainerTrafficEncryption": {{boolean}},
      "EnableNetworkIsolation": {{boolean}},
      "VpcConfig": {
         "SecurityGroupIds": [ "{{string}}" ],
         "Subnets": [ "{{string}}" ]
      }
   },
   "RoleArn": "{{string}}",
   "StoppingCondition": {
      "MaxRuntimeInSeconds": {{number}}
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
<a name="API_CreateModelExplainabilityJobDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobDefinitionName](#API_CreateModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-request-JobDefinitionName"></a>
 The name of the model explainability job definition. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [JobResources](#API_CreateModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-request-JobResources"></a>
Identifies the resources to deploy for a monitoring job.
Type: [MonitoringResources](API_MonitoringResources.md) object
Required: Yes

 ** [ModelExplainabilityAppSpecification](#API_CreateModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-request-ModelExplainabilityAppSpecification"></a>
Configures the model explainability job to run a specified Docker container image.
Type: [ModelExplainabilityAppSpecification](API_ModelExplainabilityAppSpecification.md) object
Required: Yes

 ** [ModelExplainabilityBaselineConfig](#API_CreateModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-request-ModelExplainabilityBaselineConfig"></a>
The baseline configuration for a model explainability job.
Type: [ModelExplainabilityBaselineConfig](API_ModelExplainabilityBaselineConfig.md) object
Required: No

 ** [ModelExplainabilityJobInput](#API_CreateModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-request-ModelExplainabilityJobInput"></a>
Inputs for the model explainability job.
Type: [ModelExplainabilityJobInput](API_ModelExplainabilityJobInput.md) object
Required: Yes

 ** [ModelExplainabilityJobOutputConfig](#API_CreateModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-request-ModelExplainabilityJobOutputConfig"></a>
The output configuration for monitoring jobs.
Type: [MonitoringOutputConfig](API_MonitoringOutputConfig.md) object
Required: Yes

 ** [NetworkConfig](#API_CreateModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-request-NetworkConfig"></a>
Networking options for a model explainability job.
Type: [MonitoringNetworkConfig](API_MonitoringNetworkConfig.md) object
Required: No

 ** [RoleArn](#API_CreateModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-request-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [StoppingCondition](#API_CreateModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-request-StoppingCondition"></a>
A time limit for how long the monitoring job is allowed to run before stopping.
Type: [MonitoringStoppingCondition](API_MonitoringStoppingCondition.md) object
Required: No

 ** [Tags](#API_CreateModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-request-Tags"></a>
(Optional) An array of key-value pairs. For more information, see [ Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL) in the * AWS Billing and Cost Management User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateModelExplainabilityJobDefinition_ResponseSyntax"></a>

```
{
   "JobDefinitionArn": "string"
}
```

## Response Elements
<a name="API_CreateModelExplainabilityJobDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobDefinitionArn](#API_CreateModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-CreateModelExplainabilityJobDefinition-response-JobDefinitionArn"></a>
The Amazon Resource Name (ARN) of the model explainability job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

## Errors
<a name="API_CreateModelExplainabilityJobDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateModelExplainabilityJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
