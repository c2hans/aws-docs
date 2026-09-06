---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeMonitoringSchedule.html
---

# DescribeMonitoringSchedule
<a name="API_DescribeMonitoringSchedule"></a>

Describes the schedule for a monitoring job.

## Request Syntax
<a name="API_DescribeMonitoringSchedule_RequestSyntax"></a>

```
{
   "MonitoringScheduleName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMonitoringSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MonitoringScheduleName](#API_DescribeMonitoringSchedule_RequestSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-request-MonitoringScheduleName"></a>
Name of a previously created monitoring schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeMonitoringSchedule_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "EndpointName": "string",
   "FailureReason": "string",
   "LastModifiedTime": number,
   "LastMonitoringExecutionSummary": {
      "CreationTime": number,
      "EndpointName": "string",
      "FailureReason": "string",
      "LastModifiedTime": number,
      "MonitoringExecutionStatus": "string",
      "MonitoringJobDefinitionName": "string",
      "MonitoringScheduleName": "string",
      "MonitoringType": "string",
      "ProcessingJobArn": "string",
      "ScheduledTime": number
   },
   "MonitoringScheduleArn": "string",
   "MonitoringScheduleConfig": {
      "MonitoringJobDefinition": {
         "BaselineConfig": {
            "BaseliningJobName": "string",
            "ConstraintsResource": {
               "S3Uri": "string"
            },
            "StatisticsResource": {
               "S3Uri": "string"
            }
         },
         "Environment": {
            "string" : "string"
         },
         "MonitoringAppSpecification": {
            "ContainerArguments": [ "string" ],
            "ContainerEntrypoint": [ "string" ],
            "ImageUri": "string",
            "PostAnalyticsProcessorSourceUri": "string",
            "RecordPreprocessorSourceUri": "string"
         },
         "MonitoringInputs": [
            {
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
            }
         ],
         "MonitoringOutputConfig": {
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
         "MonitoringResources": {
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
      },
      "MonitoringJobDefinitionName": "string",
      "MonitoringType": "string",
      "ScheduleConfig": {
         "DataAnalysisEndTime": "string",
         "DataAnalysisStartTime": "string",
         "ScheduleExpression": "string"
      }
   },
   "MonitoringScheduleName": "string",
   "MonitoringScheduleStatus": "string",
   "MonitoringType": "string"
}
```

## Response Elements
<a name="API_DescribeMonitoringSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-response-CreationTime"></a>
The time at which the monitoring job was created.
Type: Timestamp

 ** [EndpointName](#API_DescribeMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-response-EndpointName"></a>
 The name of the endpoint for the monitoring job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [FailureReason](#API_DescribeMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-response-FailureReason"></a>
A string, up to one KB in size, that contains the reason a monitoring job failed, if it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastModifiedTime](#API_DescribeMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-response-LastModifiedTime"></a>
The time at which the monitoring job was last modified.
Type: Timestamp

 ** [LastMonitoringExecutionSummary](#API_DescribeMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-response-LastMonitoringExecutionSummary"></a>
Describes metadata on the last execution to run, if there was one.
Type: [MonitoringExecutionSummary](API_MonitoringExecutionSummary.md) object

 ** [MonitoringScheduleArn](#API_DescribeMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-response-MonitoringScheduleArn"></a>
The Amazon Resource Name (ARN) of the monitoring schedule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

 ** [MonitoringScheduleConfig](#API_DescribeMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-response-MonitoringScheduleConfig"></a>
The configuration object that specifies the monitoring schedule and defines the monitoring job.
Type: [MonitoringScheduleConfig](API_MonitoringScheduleConfig.md) object

 ** [MonitoringScheduleName](#API_DescribeMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-response-MonitoringScheduleName"></a>
Name of the monitoring schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [MonitoringScheduleStatus](#API_DescribeMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-response-MonitoringScheduleStatus"></a>
The status of an monitoring job.
Type: String
Valid Values: `Pending | Failed | Scheduled | Stopped`

 ** [MonitoringType](#API_DescribeMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-DescribeMonitoringSchedule-response-MonitoringType"></a>
The type of the monitoring job that this schedule runs. This is one of the following values.
+  `DATA_QUALITY` - The schedule is for a data quality monitoring job.
+  `MODEL_QUALITY` - The schedule is for a model quality monitoring job.
+  `MODEL_BIAS` - The schedule is for a bias monitoring job.
+  `MODEL_EXPLAINABILITY` - The schedule is for an explainability monitoring job.
Type: String
Valid Values: `DataQuality | ModelQuality | ModelBias | ModelExplainability`

## Errors
<a name="API_DescribeMonitoringSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeMonitoringSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeMonitoringSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeMonitoringSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeMonitoringSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeMonitoringSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeMonitoringSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeMonitoringSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeMonitoringSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeMonitoringSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeMonitoringSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeMonitoringSchedule)
