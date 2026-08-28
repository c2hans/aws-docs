---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRunObservabilityAlarmSummary.html
---

# TestRunObservabilityAlarmSummary
<a name="API_TestRunObservabilityAlarmSummary"></a>

Summary information about an observability alarm snapshot captured for a test run.

## Contents
<a name="API_TestRunObservabilityAlarmSummary_Contents"></a>

 ** accountId **   <a name="ngresiliencehub-Type-TestRunObservabilityAlarmSummary-accountId"></a>
The account ID that owns the CloudWatch alarm.
Type: String
Required: Yes

 ** alarmArn **   <a name="ngresiliencehub-Type-TestRunObservabilityAlarmSummary-alarmArn"></a>
The ARN of the CloudWatch alarm.
Type: String
Length Constraints: Minimum length of 31. Maximum length of 1024.
Pattern: `arn:aws[a-zA-Z-]*:cloudwatch:[a-z]{2}(-[a-z]+)+-\d{1}:\d{12}:alarm:.+`
Required: Yes

 ** alarmName **   <a name="ngresiliencehub-Type-TestRunObservabilityAlarmSummary-alarmName"></a>
The name of the CloudWatch alarm.
Type: String
Required: Yes

 ** region **   <a name="ngresiliencehub-Type-TestRunObservabilityAlarmSummary-region"></a>
The Region of the CloudWatch alarm.
Type: String
Required: Yes

## See Also
<a name="API_TestRunObservabilityAlarmSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRunObservabilityAlarmSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRunObservabilityAlarmSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRunObservabilityAlarmSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
