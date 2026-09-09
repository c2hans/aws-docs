---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelBiasJobDefinition.html
---

# DescribeModelBiasJobDefinition
<a name="API_DescribeModelBiasJobDefinition"></a>

Returns a description of a model bias job definition.

## Request Syntax
<a name="API_DescribeModelBiasJobDefinition_RequestSyntax"></a>

```
{
   "JobDefinitionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeModelBiasJobDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobDefinitionName](#API_DescribeModelBiasJobDefinition_RequestSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-request-JobDefinitionName"></a>
The name of the model bias job definition. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeModelBiasJobDefinition_ResponseSyntax"></a>

```
{
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
   "ModelBiasAppSpecification": {
      "ConfigUri": "string",
      "Environment": {
         "string" : "string"
      },
      "ImageUri": "string"
   },
   "ModelBiasBaselineConfig": {
      "BaseliningJobName": "string",
      "ConstraintsResource": {
         "S3Uri": "string"
      }
   },
   "ModelBiasJobInput": {
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
      },
      "GroundTruthS3Input": {
         "S3Uri": "string"
      }
   },
   "ModelBiasJobOutputConfig": {
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
<a name="API_DescribeModelBiasJobDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobDefinitionArn](#API_DescribeModelBiasJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-response-JobDefinitionArn"></a>
The Amazon Resource Name (ARN) of the model bias job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

 ** [JobDefinitionName](#API_DescribeModelBiasJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-response-JobDefinitionName"></a>
The name of the bias job definition. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [JobResources](#API_DescribeModelBiasJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-response-JobResources"></a>
Identifies the resources to deploy for a monitoring job.
Type: [MonitoringResources](API_MonitoringResources.md) object

 ** [ModelBiasAppSpecification](#API_DescribeModelBiasJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-response-ModelBiasAppSpecification"></a>
Configures the model bias job to run a specified Docker container image.
Type: [ModelBiasAppSpecification](API_ModelBiasAppSpecification.md) object

 ** [ModelBiasBaselineConfig](#API_DescribeModelBiasJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-response-ModelBiasBaselineConfig"></a>
The baseline configuration for a model bias job.
Type: [ModelBiasBaselineConfig](API_ModelBiasBaselineConfig.md) object

 ** [ModelBiasJobInput](#API_DescribeModelBiasJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-response-ModelBiasJobInput"></a>
Inputs for the model bias job.
Type: [ModelBiasJobInput](API_ModelBiasJobInput.md) object

 ** [ModelBiasJobOutputConfig](#API_DescribeModelBiasJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-response-ModelBiasJobOutputConfig"></a>
The output configuration for monitoring jobs.
Type: [MonitoringOutputConfig](API_MonitoringOutputConfig.md) object

 ** [NetworkConfig](#API_DescribeModelBiasJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-response-NetworkConfig"></a>
Networking options for a model bias job.
Type: [MonitoringNetworkConfig](API_MonitoringNetworkConfig.md) object

 ** [RoleArn](#API_DescribeModelBiasJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [StoppingCondition](#API_DescribeModelBiasJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelBiasJobDefinition-response-StoppingCondition"></a>
A time limit for how long the monitoring job is allowed to run before stopping.
Type: [MonitoringStoppingCondition](API_MonitoringStoppingCondition.md) object

## Errors
<a name="API_DescribeModelBiasJobDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeModelBiasJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeModelBiasJobDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeModelBiasJobDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeModelBiasJobDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeModelBiasJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeModelBiasJobDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeModelBiasJobDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeModelBiasJobDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeModelBiasJobDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeModelBiasJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeModelBiasJobDefinition)
