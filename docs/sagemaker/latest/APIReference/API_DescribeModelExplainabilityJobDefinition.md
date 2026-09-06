---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelExplainabilityJobDefinition.html
---

# DescribeModelExplainabilityJobDefinition
<a name="API_DescribeModelExplainabilityJobDefinition"></a>

Returns a description of a model explainability job definition.

## Request Syntax
<a name="API_DescribeModelExplainabilityJobDefinition_RequestSyntax"></a>

```
{
   "JobDefinitionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeModelExplainabilityJobDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobDefinitionName](#API_DescribeModelExplainabilityJobDefinition_RequestSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-request-JobDefinitionName"></a>
The name of the model explainability job definition. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeModelExplainabilityJobDefinition_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "JobDefinitionArn": "string",
   "JobDefinitionName": "string",
   "JobResources": {
      "ClusterConfig": {
         "InstanceCount": number,
         "InstanceType": "string",
         "VolumeKmsKeyId": "string",
         "VolumeSizeInGB": number
      }
   },
   "ModelExplainabilityAppSpecification": {
      "ConfigUri": "string",
      "Environment": {
         "string" : "string"
      },
      "ImageUri": "string"
   },
   "ModelExplainabilityBaselineConfig": {
      "BaseliningJobName": "string",
      "ConstraintsResource": {
         "S3Uri": "string"
      }
   },
   "ModelExplainabilityJobInput": {
      "BatchTransformInput": {
         "DataCapturedDestinationS3Uri": "string",
         "DatasetFormat": {
            "Csv": {
               "Header": boolean
            },
            "Json": {
               "Line": boolean
            },
            "Parquet": {
            }
         },
         "EndTimeOffset": "string",
         "ExcludeFeaturesAttribute": "string",
         "FeaturesAttribute": "string",
         "InferenceAttribute": "string",
         "LocalPath": "string",
         "ProbabilityAttribute": "string",
         "ProbabilityThresholdAttribute": number,
         "S3DataDistributionType": "string",
         "S3InputMode": "string",
         "StartTimeOffset": "string"
      },
      "EndpointInput": {
         "EndpointName": "string",
         "EndTimeOffset": "string",
         "ExcludeFeaturesAttribute": "string",
         "FeaturesAttribute": "string",
         "InferenceAttribute": "string",
         "LocalPath": "string",
         "ProbabilityAttribute": "string",
         "ProbabilityThresholdAttribute": number,
         "S3DataDistributionType": "string",
         "S3InputMode": "string",
         "StartTimeOffset": "string"
      }
   },
   "ModelExplainabilityJobOutputConfig": {
      "KmsKeyId": "string",
      "MonitoringOutputs": [
         {
            "S3Output": {
               "LocalPath": "string",
               "S3UploadMode": "string",
               "S3Uri": "string"
            }
         }
      ]
   },
   "NetworkConfig": {
      "EnableInterContainerTrafficEncryption": boolean,
      "EnableNetworkIsolation": boolean,
      "VpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "Subnets": [ "string" ]
      }
   },
   "RoleArn": "string",
   "StoppingCondition": {
      "MaxRuntimeInSeconds": number
   }
}
```

## Response Elements
<a name="API_DescribeModelExplainabilityJobDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-CreationTime"></a>
The time at which the model explainability job was created.
Type: Timestamp

 ** [JobDefinitionArn](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-JobDefinitionArn"></a>
The Amazon Resource Name (ARN) of the model explainability job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

 ** [JobDefinitionName](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-JobDefinitionName"></a>
The name of the explainability job definition. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [JobResources](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-JobResources"></a>
Identifies the resources to deploy for a monitoring job.
Type: [MonitoringResources](API_MonitoringResources.md) object

 ** [ModelExplainabilityAppSpecification](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-ModelExplainabilityAppSpecification"></a>
Configures the model explainability job to run a specified Docker container image.
Type: [ModelExplainabilityAppSpecification](API_ModelExplainabilityAppSpecification.md) object

 ** [ModelExplainabilityBaselineConfig](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-ModelExplainabilityBaselineConfig"></a>
The baseline configuration for a model explainability job.
Type: [ModelExplainabilityBaselineConfig](API_ModelExplainabilityBaselineConfig.md) object

 ** [ModelExplainabilityJobInput](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-ModelExplainabilityJobInput"></a>
Inputs for the model explainability job.
Type: [ModelExplainabilityJobInput](API_ModelExplainabilityJobInput.md) object

 ** [ModelExplainabilityJobOutputConfig](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-ModelExplainabilityJobOutputConfig"></a>
The output configuration for monitoring jobs.
Type: [MonitoringOutputConfig](API_MonitoringOutputConfig.md) object

 ** [NetworkConfig](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-NetworkConfig"></a>
Networking options for a model explainability job.
Type: [MonitoringNetworkConfig](API_MonitoringNetworkConfig.md) object

 ** [RoleArn](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [StoppingCondition](#API_DescribeModelExplainabilityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelExplainabilityJobDefinition-response-StoppingCondition"></a>
A time limit for how long the monitoring job is allowed to run before stopping.
Type: [MonitoringStoppingCondition](API_MonitoringStoppingCondition.md) object

## Errors
<a name="API_DescribeModelExplainabilityJobDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeModelExplainabilityJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeModelExplainabilityJobDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeModelExplainabilityJobDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeModelExplainabilityJobDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeModelExplainabilityJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeModelExplainabilityJobDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeModelExplainabilityJobDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeModelExplainabilityJobDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeModelExplainabilityJobDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeModelExplainabilityJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeModelExplainabilityJobDefinition)
