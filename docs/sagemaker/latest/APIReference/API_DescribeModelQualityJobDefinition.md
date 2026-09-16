---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelQualityJobDefinition.html
---

# DescribeModelQualityJobDefinition
<a name="API_DescribeModelQualityJobDefinition"></a>

Returns a description of a model quality job definition.

## Request Syntax
<a name="API_DescribeModelQualityJobDefinition_RequestSyntax"></a>

```
{
   "JobDefinitionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeModelQualityJobDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobDefinitionName](#API_DescribeModelQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-request-JobDefinitionName"></a>
The name of the model quality job. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeModelQualityJobDefinition_ResponseSyntax"></a>

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
   "ModelQualityAppSpecification": {
      "ContainerArguments": [ "string" ],
      "ContainerEntrypoint": [ "string" ],
      "Environment": {
         "string" : "string"
      },
      "ImageUri": "string",
      "PostAnalyticsProcessorSourceUri": "string",
      "ProblemType": "string",
      "RecordPreprocessorSourceUri": "string"
   },
   "ModelQualityBaselineConfig": {
      "BaseliningJobName": "string",
      "ConstraintsResource": {
         "S3Uri": "string"
      }
   },
   "ModelQualityJobInput": {
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
   "ModelQualityJobOutputConfig": {
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
<a name="API_DescribeModelQualityJobDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobDefinitionArn](#API_DescribeModelQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-response-JobDefinitionArn"></a>
The Amazon Resource Name (ARN) of the model quality job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

 ** [JobDefinitionName](#API_DescribeModelQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-response-JobDefinitionName"></a>
The name of the quality job definition. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [JobResources](#API_DescribeModelQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-response-JobResources"></a>
Identifies the resources to deploy for a monitoring job.
Type: [MonitoringResources](API_MonitoringResources.md) object

 ** [ModelQualityAppSpecification](#API_DescribeModelQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-response-ModelQualityAppSpecification"></a>
Configures the model quality job to run a specified Docker container image.
Type: [ModelQualityAppSpecification](API_ModelQualityAppSpecification.md) object

 ** [ModelQualityBaselineConfig](#API_DescribeModelQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-response-ModelQualityBaselineConfig"></a>
The baseline configuration for a model quality job.
Type: [ModelQualityBaselineConfig](API_ModelQualityBaselineConfig.md) object

 ** [ModelQualityJobInput](#API_DescribeModelQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-response-ModelQualityJobInput"></a>
Inputs for the model quality job.
Type: [ModelQualityJobInput](API_ModelQualityJobInput.md) object

 ** [ModelQualityJobOutputConfig](#API_DescribeModelQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-response-ModelQualityJobOutputConfig"></a>
The output configuration for monitoring jobs.
Type: [MonitoringOutputConfig](API_MonitoringOutputConfig.md) object

 ** [NetworkConfig](#API_DescribeModelQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-response-NetworkConfig"></a>
Networking options for a model quality job.
Type: [MonitoringNetworkConfig](API_MonitoringNetworkConfig.md) object

 ** [RoleArn](#API_DescribeModelQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-response-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [StoppingCondition](#API_DescribeModelQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeModelQualityJobDefinition-response-StoppingCondition"></a>
A time limit for how long the monitoring job is allowed to run before stopping.
Type: [MonitoringStoppingCondition](API_MonitoringStoppingCondition.md) object

## Errors
<a name="API_DescribeModelQualityJobDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeModelQualityJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeModelQualityJobDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeModelQualityJobDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeModelQualityJobDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeModelQualityJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeModelQualityJobDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeModelQualityJobDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeModelQualityJobDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeModelQualityJobDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeModelQualityJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeModelQualityJobDefinition)
