---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeDataQualityJobDefinition.html
---

# DescribeDataQualityJobDefinition
<a name="API_DescribeDataQualityJobDefinition"></a>

Gets the details of a data quality monitoring job definition.

## Request Syntax
<a name="API_DescribeDataQualityJobDefinition_RequestSyntax"></a>

```
{
   "JobDefinitionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDataQualityJobDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobDefinitionName](#API_DescribeDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-request-JobDefinitionName"></a>
The name of the data quality monitoring job definition to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeDataQualityJobDefinition_ResponseSyntax"></a>

```
{
   "DataQualityAppSpecification": {
      "ContainerArguments": [ "string" ],
      "ContainerEntrypoint": [ "string" ],
      "Environment": {
         "string" : "string"
      },
      "ImageUri": "string",
      "PostAnalyticsProcessorSourceUri": "string",
      "RecordPreprocessorSourceUri": "string"
   },
   "DataQualityBaselineConfig": {
      "BaseliningJobName": "string",
      "ConstraintsResource": {
         "S3Uri": "string"
      },
      "StatisticsResource": {
         "S3Uri": "string"
      }
   },
   "DataQualityJobInput": {
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
   "DataQualityJobOutputConfig": {
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
<a name="API_DescribeDataQualityJobDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataQualityAppSpecification](#API_DescribeDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-response-DataQualityAppSpecification"></a>
Information about the container that runs the data quality monitoring job.
Type: [DataQualityAppSpecification](API_DataQualityAppSpecification.md) object

 ** [DataQualityBaselineConfig](#API_DescribeDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-response-DataQualityBaselineConfig"></a>
The constraints and baselines for the data quality monitoring job definition.
Type: [DataQualityBaselineConfig](API_DataQualityBaselineConfig.md) object

 ** [DataQualityJobInput](#API_DescribeDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-response-DataQualityJobInput"></a>
The list of inputs for the data quality monitoring job. Currently endpoints are supported.
Type: [DataQualityJobInput](API_DataQualityJobInput.md) object

 ** [DataQualityJobOutputConfig](#API_DescribeDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-response-DataQualityJobOutputConfig"></a>
The output configuration for monitoring jobs.
Type: [MonitoringOutputConfig](API_MonitoringOutputConfig.md) object

 ** [JobDefinitionArn](#API_DescribeDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-response-JobDefinitionArn"></a>
The Amazon Resource Name (ARN) of the data quality monitoring job definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

 ** [JobDefinitionName](#API_DescribeDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-response-JobDefinitionName"></a>
The name of the data quality monitoring job definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [JobResources](#API_DescribeDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-response-JobResources"></a>
Identifies the resources to deploy for a monitoring job.
Type: [MonitoringResources](API_MonitoringResources.md) object

 ** [NetworkConfig](#API_DescribeDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-response-NetworkConfig"></a>
The networking configuration for the data quality monitoring job.
Type: [MonitoringNetworkConfig](API_MonitoringNetworkConfig.md) object

 ** [RoleArn](#API_DescribeDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-response-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [StoppingCondition](#API_DescribeDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-DescribeDataQualityJobDefinition-response-StoppingCondition"></a>
A time limit for how long the monitoring job is allowed to run before stopping.
Type: [MonitoringStoppingCondition](API_MonitoringStoppingCondition.md) object

## Errors
<a name="API_DescribeDataQualityJobDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDataQualityJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeDataQualityJobDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeDataQualityJobDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeDataQualityJobDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeDataQualityJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeDataQualityJobDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeDataQualityJobDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeDataQualityJobDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeDataQualityJobDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeDataQualityJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeDataQualityJobDefinition)
