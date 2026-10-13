---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringSchedule.html
---

# MonitoringSchedule
<a name="API_MonitoringSchedule"></a>

A schedule for a model monitoring job. For information about model monitor, see [Amazon SageMaker Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html).

## Contents
<a name="API_MonitoringSchedule_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-MonitoringSchedule-CreationTime"></a>
The time that the monitoring schedule was created.
Type: Timestamp
Required: No

 ** EndpointName **   <a name="sagemaker-Type-MonitoringSchedule-EndpointName"></a>
The endpoint that hosts the model being monitored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** FailureReason **   <a name="sagemaker-Type-MonitoringSchedule-FailureReason"></a>
If the monitoring schedule failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-MonitoringSchedule-LastModifiedTime"></a>
The last time the monitoring schedule was changed.
Type: Timestamp
Required: No

 ** LastMonitoringExecutionSummary **   <a name="sagemaker-Type-MonitoringSchedule-LastMonitoringExecutionSummary"></a>
Summary of information about the last monitoring job to run.
Type: [MonitoringExecutionSummary](API_MonitoringExecutionSummary.md) object
Required: No

 ** MonitoringScheduleArn **   <a name="sagemaker-Type-MonitoringSchedule-MonitoringScheduleArn"></a>
The Amazon Resource Name (ARN) of the monitoring schedule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** MonitoringScheduleConfig **   <a name="sagemaker-Type-MonitoringSchedule-MonitoringScheduleConfig"></a>
Configures the monitoring schedule and defines the monitoring job.
Type: [MonitoringScheduleConfig](API_MonitoringScheduleConfig.md) object
Required: No

 ** MonitoringScheduleName **   <a name="sagemaker-Type-MonitoringSchedule-MonitoringScheduleName"></a>
The name of the monitoring schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** MonitoringScheduleStatus **   <a name="sagemaker-Type-MonitoringSchedule-MonitoringScheduleStatus"></a>
The status of the monitoring schedule. This can be one of the following values.
+  `PENDING` - The schedule is pending being created.
+  `FAILED` - The schedule failed.
+  `SCHEDULED` - The schedule was successfully created.
+  `STOPPED` - The schedule was stopped.
Type: String
Valid Values: `Pending | Failed | Scheduled | Stopped`
Required: No

 ** MonitoringType **   <a name="sagemaker-Type-MonitoringSchedule-MonitoringType"></a>
The type of the monitoring job definition to schedule.
Type: String
Valid Values: `DataQuality | ModelQuality | ModelBias | ModelExplainability`
Required: No

 ** Tags **   <a name="sagemaker-Type-MonitoringSchedule-Tags"></a>
A list of the tags associated with the monitoring schedlue. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_MonitoringSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringSchedule)
