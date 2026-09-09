---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringScheduleSummary.html
---

# MonitoringScheduleSummary
<a name="API_MonitoringScheduleSummary"></a>

Summarizes the monitoring schedule.

## Contents
<a name="API_MonitoringScheduleSummary_Contents"></a>

 ** MonitoringScheduleArn **   <a name="sagemaker-Type-MonitoringScheduleSummary-MonitoringScheduleArn"></a>
The Amazon Resource Name (ARN) of the monitoring schedule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** MonitoringScheduleName **   <a name="sagemaker-Type-MonitoringScheduleSummary-MonitoringScheduleName"></a>
The name of the monitoring schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** MonitoringScheduleStatus **   <a name="sagemaker-Type-MonitoringScheduleSummary-MonitoringScheduleStatus"></a>
The status of the monitoring schedule.
Type: String
Valid Values: `Pending | Failed | Scheduled | Stopped`
Required: Yes

 ** EndpointName **   <a name="sagemaker-Type-MonitoringScheduleSummary-EndpointName"></a>
The name of the endpoint using the monitoring schedule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** MonitoringJobDefinitionName **   <a name="sagemaker-Type-MonitoringScheduleSummary-MonitoringJobDefinitionName"></a>
The name of the monitoring job definition that the schedule is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** MonitoringType **   <a name="sagemaker-Type-MonitoringScheduleSummary-MonitoringType"></a>
The type of the monitoring job definition that the schedule is for.
Type: String
Valid Values: `DataQuality | ModelQuality | ModelBias | ModelExplainability`
Required: No

## See Also
<a name="API_MonitoringScheduleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringScheduleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringScheduleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringScheduleSummary)
