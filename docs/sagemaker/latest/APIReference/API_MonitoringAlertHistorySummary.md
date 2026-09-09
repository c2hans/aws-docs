---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringAlertHistorySummary.html
---

# MonitoringAlertHistorySummary
<a name="API_MonitoringAlertHistorySummary"></a>

Provides summary information of an alert's history.

## Contents
<a name="API_MonitoringAlertHistorySummary_Contents"></a>

 ** AlertStatus **   <a name="sagemaker-Type-MonitoringAlertHistorySummary-AlertStatus"></a>
The current alert status of an alert.
Type: String
Valid Values: `InAlert | OK`
Required: Yes

 ** MonitoringAlertName **   <a name="sagemaker-Type-MonitoringAlertHistorySummary-MonitoringAlertName"></a>
The name of a monitoring alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** MonitoringScheduleName **   <a name="sagemaker-Type-MonitoringAlertHistorySummary-MonitoringScheduleName"></a>
The name of a monitoring schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## See Also
<a name="API_MonitoringAlertHistorySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringAlertHistorySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringAlertHistorySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringAlertHistorySummary)
