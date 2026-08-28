---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ScheduleGroupSummary.html
---

# ScheduleGroupSummary
<a name="API_ScheduleGroupSummary"></a>

The details of a schedule group.

## Contents
<a name="API_ScheduleGroupSummary_Contents"></a>

 ** Arn **   <a name="scheduler-Type-ScheduleGroupSummary-Arn"></a>
The Amazon Resource Name (ARN) of the schedule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]+)?:scheduler:[a-z0-9\-]+:\d{12}:schedule-group\/[0-9a-zA-Z-_.]+`
Required: No

 ** CreationDate **   <a name="scheduler-Type-ScheduleGroupSummary-CreationDate"></a>
The time at which the schedule group was created.
Type: Timestamp
Required: No

 ** LastModificationDate **   <a name="scheduler-Type-ScheduleGroupSummary-LastModificationDate"></a>
The time at which the schedule group was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="scheduler-Type-ScheduleGroupSummary-Name"></a>
The name of the schedule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`
Required: No

 ** State **   <a name="scheduler-Type-ScheduleGroupSummary-State"></a>
Specifies the state of the schedule group.
Type: String
Valid Values: `ACTIVE | DELETING`
Required: No

## See Also
<a name="API_ScheduleGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/ScheduleGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/ScheduleGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/ScheduleGroupSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EventBridge Scheduler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query scheduler` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
