---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateDataQualityJobDefinition.html
---

# CreateDataQualityJobDefinition
<a name="API_CreateDataQualityJobDefinition"></a>

Creates a definition for a job that monitors data quality and drift. For information about model monitor, see [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html).

## Request Syntax
<a name="API_CreateDataQualityJobDefinition_RequestSyntax"></a>

```
{
   "DataQualityAppSpecification": {
      "ContainerArguments": [ "{{string}}" ],
      "ContainerEntrypoint": [ "{{string}}" ],
      "Environment": {
         "{{string}}" : "{{string}}"
      },
      "ImageUri": "{{string}}",
      "PostAnalyticsProcessorSourceUri": "{{string}}",
      "RecordPreprocessorSourceUri": "{{string}}"
   },
   "DataQualityBaselineConfig": {
      "BaseliningJobName": "{{string}}",
      "ConstraintsResource": {
         "S3Uri": "{{string}}"
      },
      "StatisticsResource": {
         "S3Uri": "{{string}}"
      }
   },
   "DataQualityJobInput": {
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
   "DataQualityJobOutputConfig": {
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
   "JobDefinitionName": "{{string}}",
   "JobResources": {
      "ClusterConfig": {
         "InstanceCount": {{number}},
         "InstanceType": "{{string}}",
         "VolumeKmsKeyId": "{{string}}",
         "VolumeSizeInGB": {{number}}
      }
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
<a name="API_CreateDataQualityJobDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataQualityAppSpecification](#API_CreateDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-request-DataQualityAppSpecification"></a>
Specifies the container that runs the monitoring job.
Type: [DataQualityAppSpecification](API_DataQualityAppSpecification.md) object
Required: Yes

 ** [DataQualityBaselineConfig](#API_CreateDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-request-DataQualityBaselineConfig"></a>
Configures the constraints and baselines for the monitoring job.
Type: [DataQualityBaselineConfig](API_DataQualityBaselineConfig.md) object
Required: No

 ** [DataQualityJobInput](#API_CreateDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-request-DataQualityJobInput"></a>
A list of inputs for the monitoring job. Currently endpoints are supported as monitoring inputs.
Type: [DataQualityJobInput](API_DataQualityJobInput.md) object
Required: Yes

 ** [DataQualityJobOutputConfig](#API_CreateDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-request-DataQualityJobOutputConfig"></a>
The output configuration for monitoring jobs.
Type: [MonitoringOutputConfig](API_MonitoringOutputConfig.md) object
Required: Yes

 ** [JobDefinitionName](#API_CreateDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-request-JobDefinitionName"></a>
The name for the monitoring job definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [JobResources](#API_CreateDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-request-JobResources"></a>
Identifies the resources to deploy for a monitoring job.
Type: [MonitoringResources](API_MonitoringResources.md) object
Required: Yes

 ** [NetworkConfig](#API_CreateDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-request-NetworkConfig"></a>
Specifies networking configuration for the monitoring job.
Type: [MonitoringNetworkConfig](API_MonitoringNetworkConfig.md) object
Required: No

 ** [RoleArn](#API_CreateDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-request-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [StoppingCondition](#API_CreateDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-request-StoppingCondition"></a>
A time limit for how long the monitoring job is allowed to run before stopping.
Type: [MonitoringStoppingCondition](API_MonitoringStoppingCondition.md) object
Required: No

 ** [Tags](#API_CreateDataQualityJobDefinition_RequestSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-request-Tags"></a>
(Optional) An array of key-value pairs. For more information, see [ Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL) in the * AWS Billing and Cost Management User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateDataQualityJobDefinition_ResponseSyntax"></a>

```
{
   "JobDefinitionArn": "string"
}
```

## Response Elements
<a name="API_CreateDataQualityJobDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobDefinitionArn](#API_CreateDataQualityJobDefinition_ResponseSyntax) **   <a name="sagemaker-CreateDataQualityJobDefinition-response-JobDefinitionArn"></a>
The Amazon Resource Name (ARN) of the job definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

## Errors
<a name="API_CreateDataQualityJobDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateDataQualityJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateDataQualityJobDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateDataQualityJobDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateDataQualityJobDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateDataQualityJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateDataQualityJobDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateDataQualityJobDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateDataQualityJobDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateDataQualityJobDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateDataQualityJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateDataQualityJobDefinition)
