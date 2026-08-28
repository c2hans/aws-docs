---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_SuccessCriteriaAlarmSummary.html
---

# SuccessCriteriaAlarmSummary
<a name="API_SuccessCriteriaAlarmSummary"></a>

Summary information about a configured success criteria alarm.

## Contents
<a name="API_SuccessCriteriaAlarmSummary_Contents"></a>

 ** accountId **   <a name="ngresiliencehub-Type-SuccessCriteriaAlarmSummary-accountId"></a>
The account ID that owns the CloudWatch alarm.
Type: String
Required: Yes

 ** alarmArn **   <a name="ngresiliencehub-Type-SuccessCriteriaAlarmSummary-alarmArn"></a>
The ARN of the CloudWatch alarm.
Type: String
Length Constraints: Minimum length of 31. Maximum length of 1024.
Pattern: `arn:aws[a-zA-Z-]*:cloudwatch:[a-z]{2}(-[a-z]+)+-\d{1}:\d{12}:alarm:.+`
Required: Yes

 ** alarmName **   <a name="ngresiliencehub-Type-SuccessCriteriaAlarmSummary-alarmName"></a>
The name of the CloudWatch alarm.
Type: String
Required: Yes

 ** region **   <a name="ngresiliencehub-Type-SuccessCriteriaAlarmSummary-region"></a>
The Region of the CloudWatch alarm.
Type: String
Required: Yes

 ** createdAt **   <a name="ngresiliencehub-Type-SuccessCriteriaAlarmSummary-createdAt"></a>
The timestamp when the source was configured.
Type: Timestamp
Required: No

## See Also
<a name="API_SuccessCriteriaAlarmSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/SuccessCriteriaAlarmSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/SuccessCriteriaAlarmSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/SuccessCriteriaAlarmSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
