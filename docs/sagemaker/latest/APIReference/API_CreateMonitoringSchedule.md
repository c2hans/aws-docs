---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateMonitoringSchedule.html
---

# CreateMonitoringSchedule
<a name="API_CreateMonitoringSchedule"></a>

Creates a schedule that regularly starts Amazon SageMaker AI Processing Jobs to monitor the data captured for an Amazon SageMaker AI Endpoint.

## Request Syntax
<a name="API_CreateMonitoringSchedule_RequestSyntax"></a>

```
{
   "MonitoringScheduleConfig": {
      "MonitoringJobDefinition": {
         "BaselineConfig": {
            "BaseliningJobName": "{{string}}",
            "ConstraintsResource": {
               "S3Uri": "{{string}}"
            },
            "StatisticsResource": {
               "S3Uri": "{{string}}"
            }
         },
         "Environment": {
            "{{string}}" : "{{string}}"
         },
         "MonitoringAppSpecification": {
            "ContainerArguments": [ "{{string}}" ],
            "ContainerEntrypoint": [ "{{string}}" ],
            "ImageUri": "{{string}}",
            "PostAnalyticsProcessorSourceUri": "{{string}}",
            "RecordPreprocessorSourceUri": "{{string}}"
         },
         "MonitoringInputs": [
            {
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
            }
         ],
         "MonitoringOutputConfig": {
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
         "MonitoringResources": {
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
         }
      },
      "MonitoringJobDefinitionName": "{{string}}",
      "MonitoringType": "{{string}}",
      "ScheduleConfig": {
         "DataAnalysisEndTime": "{{string}}",
         "DataAnalysisStartTime": "{{string}}",
         "ScheduleExpression": "{{string}}"
      }
   },
   "MonitoringScheduleName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateMonitoringSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MonitoringScheduleConfig](#API_CreateMonitoringSchedule_RequestSyntax) **   <a name="sagemaker-CreateMonitoringSchedule-request-MonitoringScheduleConfig"></a>
The configuration object that specifies the monitoring schedule and defines the monitoring job.
Type: [MonitoringScheduleConfig](API_MonitoringScheduleConfig.md) object
Required: Yes

 ** [MonitoringScheduleName](#API_CreateMonitoringSchedule_RequestSyntax) **   <a name="sagemaker-CreateMonitoringSchedule-request-MonitoringScheduleName"></a>
The name of the monitoring schedule. The name must be unique within an AWS Region within an AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [Tags](#API_CreateMonitoringSchedule_RequestSyntax) **   <a name="sagemaker-CreateMonitoringSchedule-request-Tags"></a>
(Optional) An array of key-value pairs. For more information, see [Using Cost Allocation Tags]( https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL) in the * AWS Billing and Cost Management User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateMonitoringSchedule_ResponseSyntax"></a>

```
{
   "MonitoringScheduleArn": "string"
}
```

## Response Elements
<a name="API_CreateMonitoringSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonitoringScheduleArn](#API_CreateMonitoringSchedule_ResponseSyntax) **   <a name="sagemaker-CreateMonitoringSchedule-response-MonitoringScheduleArn"></a>
The Amazon Resource Name (ARN) of the monitoring schedule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

## Errors
<a name="API_CreateMonitoringSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateMonitoringSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateMonitoringSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateMonitoringSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateMonitoringSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateMonitoringSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateMonitoringSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateMonitoringSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateMonitoringSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateMonitoringSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateMonitoringSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateMonitoringSchedule)
