---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AlarmMuteRuleSummary.html
---

# AlarmMuteRuleSummary
<a name="API_AlarmMuteRuleSummary"></a>

Summary information about an alarm mute rule, including its name, status, and configuration details.

## Contents
<a name="API_AlarmMuteRuleSummary_Contents"></a>

 ** AlarmMuteRuleArn **   <a name="ACW-Type-AlarmMuteRuleSummary-AlarmMuteRuleArn"></a>
The Amazon Resource Name (ARN) of the alarm mute rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** ExpireDate **   <a name="ACW-Type-AlarmMuteRuleSummary-ExpireDate"></a>
The date and time when the mute rule expires and is no longer evaluated. This field is only present if an expiration date was configured.
Type: Timestamp
Required: No

 ** LastUpdatedTimestamp **   <a name="ACW-Type-AlarmMuteRuleSummary-LastUpdatedTimestamp"></a>
The date and time when the mute rule was last updated.
Type: Timestamp
Required: No

 ** MuteType **   <a name="ACW-Type-AlarmMuteRuleSummary-MuteType"></a>
Indicates whether the mute rule is one-time or recurring. Valid values are `ONE_TIME` or `RECURRING`.
Type: String
Required: No

 ** Status **   <a name="ACW-Type-AlarmMuteRuleSummary-Status"></a>
The current status of the alarm mute rule. Valid values are `SCHEDULED`, `ACTIVE`, or `EXPIRED`.
Type: String
Valid Values: `SCHEDULED | ACTIVE | EXPIRED`
Required: No

## See Also
<a name="API_AlarmMuteRuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AlarmMuteRuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AlarmMuteRuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AlarmMuteRuleSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
