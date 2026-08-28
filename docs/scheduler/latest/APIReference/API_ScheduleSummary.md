---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ScheduleSummary.html
---

# ScheduleSummary
<a name="API_ScheduleSummary"></a>

The details of a schedule.

## Contents
<a name="API_ScheduleSummary_Contents"></a>

 ** Arn **   <a name="scheduler-Type-ScheduleSummary-Arn"></a>
The Amazon Resource Name (ARN) of the schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]+)?:scheduler:[a-z0-9\-]+:\d{12}:schedule\/[0-9a-zA-Z-_.]+\/[0-9a-zA-Z-_.]+`
Required: No

 ** CreationDate **   <a name="scheduler-Type-ScheduleSummary-CreationDate"></a>
The time at which the schedule was created.
Type: Timestamp
Required: No

 ** GroupName **   <a name="scheduler-Type-ScheduleSummary-GroupName"></a>
The name of the schedule group associated with this schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`
Required: No

 ** LastModificationDate **   <a name="scheduler-Type-ScheduleSummary-LastModificationDate"></a>
The time at which the schedule was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="scheduler-Type-ScheduleSummary-Name"></a>
The name of the schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`
Required: No

 ** State **   <a name="scheduler-Type-ScheduleSummary-State"></a>
Specifies whether the schedule is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** Target **   <a name="scheduler-Type-ScheduleSummary-Target"></a>
The schedule's target details.
Type: [TargetSummary](API_TargetSummary.md) object
Required: No

## See Also
<a name="API_ScheduleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/ScheduleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/ScheduleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/ScheduleSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EventBridge Scheduler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query scheduler` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
