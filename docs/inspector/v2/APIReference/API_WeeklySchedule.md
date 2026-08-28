---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_WeeklySchedule.html
---

# WeeklySchedule
<a name="API_WeeklySchedule"></a>

A weekly schedule.

## Contents
<a name="API_WeeklySchedule_Contents"></a>

 ** days **   <a name="inspector2-Type-WeeklySchedule-days"></a>
The weekly schedule's days.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 7 items.
Valid Values: `SUN | MON | TUE | WED | THU | FRI | SAT`
Required: Yes

 ** startTime **   <a name="inspector2-Type-WeeklySchedule-startTime"></a>
The weekly schedule's start time.
Type: [Time](API_Time.md) object
Required: Yes

## See Also
<a name="API_WeeklySchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/WeeklySchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/WeeklySchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/WeeklySchedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
