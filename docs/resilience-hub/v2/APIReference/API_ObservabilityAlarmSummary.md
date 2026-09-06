---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ObservabilityAlarmSummary.html
---

# ObservabilityAlarmSummary
<a name="API_ObservabilityAlarmSummary"></a>

Summary information about a configured observability alarm.

## Contents
<a name="API_ObservabilityAlarmSummary_Contents"></a>

 ** accountId **   <a name="ngresiliencehub-Type-ObservabilityAlarmSummary-accountId"></a>
The account ID that owns the CloudWatch alarm.
Type: String
Required: Yes

 ** alarmArn **   <a name="ngresiliencehub-Type-ObservabilityAlarmSummary-alarmArn"></a>
The ARN of the CloudWatch alarm.
Type: String
Length Constraints: Minimum length of 31. Maximum length of 1024.
Pattern: `arn:aws[a-zA-Z-]*:cloudwatch:[a-z]{2}(-[a-z]+)+-\d{1}:\d{12}:alarm:.+`
Required: Yes

 ** alarmName **   <a name="ngresiliencehub-Type-ObservabilityAlarmSummary-alarmName"></a>
The name of the CloudWatch alarm.
Type: String
Required: Yes

 ** region **   <a name="ngresiliencehub-Type-ObservabilityAlarmSummary-region"></a>
The Region of the CloudWatch alarm.
Type: String
Required: Yes

 ** createdAt **   <a name="ngresiliencehub-Type-ObservabilityAlarmSummary-createdAt"></a>
The timestamp when the source was configured.
Type: Timestamp
Required: No

## See Also
<a name="API_ObservabilityAlarmSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ObservabilityAlarmSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ObservabilityAlarmSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ObservabilityAlarmSummary)
