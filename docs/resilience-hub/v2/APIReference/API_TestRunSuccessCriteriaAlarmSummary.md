---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRunSuccessCriteriaAlarmSummary.html
---

# TestRunSuccessCriteriaAlarmSummary
<a name="API_TestRunSuccessCriteriaAlarmSummary"></a>

Summary information about a success criteria alarm snapshot captured for a test run.

## Contents
<a name="API_TestRunSuccessCriteriaAlarmSummary_Contents"></a>

 ** accountId **   <a name="ngresiliencehub-Type-TestRunSuccessCriteriaAlarmSummary-accountId"></a>
The account ID that owns the CloudWatch alarm.
Type: String
Required: Yes

 ** alarmArn **   <a name="ngresiliencehub-Type-TestRunSuccessCriteriaAlarmSummary-alarmArn"></a>
The ARN of the CloudWatch alarm.
Type: String
Length Constraints: Minimum length of 31. Maximum length of 1024.
Pattern: `arn:aws[a-zA-Z-]*:cloudwatch:[a-z]{2}(-[a-z]+)+-\d{1}:\d{12}:alarm:.+`
Required: Yes

 ** alarmName **   <a name="ngresiliencehub-Type-TestRunSuccessCriteriaAlarmSummary-alarmName"></a>
The name of the CloudWatch alarm.
Type: String
Required: Yes

 ** region **   <a name="ngresiliencehub-Type-TestRunSuccessCriteriaAlarmSummary-region"></a>
The Region of the CloudWatch alarm.
Type: String
Required: Yes

 ** outcome **   <a name="ngresiliencehub-Type-TestRunSuccessCriteriaAlarmSummary-outcome"></a>
The evaluation outcome of the source. Absent while the source has not yet been evaluated; set to the terminal outcome afterwards.
Type: String
Valid Values: `PASSED | FAILED | ERROR`
Required: No

 ** outcomeReason **   <a name="ngresiliencehub-Type-TestRunSuccessCriteriaAlarmSummary-outcomeReason"></a>
A human-readable reason for the outcome.
Type: String
Required: No

## See Also
<a name="API_TestRunSuccessCriteriaAlarmSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRunSuccessCriteriaAlarmSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRunSuccessCriteriaAlarmSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRunSuccessCriteriaAlarmSummary)
