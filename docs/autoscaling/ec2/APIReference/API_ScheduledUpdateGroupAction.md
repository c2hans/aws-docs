---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ScheduledUpdateGroupAction.html
---

# ScheduledUpdateGroupAction
<a name="API_ScheduledUpdateGroupAction"></a>

Describes a scheduled scaling action.

## Contents
<a name="API_ScheduledUpdateGroupAction_Contents"></a>

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** DesiredCapacity **
The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
Type: Integer
Required: No

 ** EndTime **
The date and time in UTC for the recurring schedule to end. For example, `"2019-06-01T00:00:00Z"`.
Type: Timestamp
Required: No

 ** MaxSize **
The maximum size of the Auto Scaling group.
Type: Integer
Required: No

 ** MinSize **
The minimum size of the Auto Scaling group.
Type: Integer
Required: No

 ** Recurrence **
The recurring schedule for the action, in Unix cron syntax format.
When `StartTime` and `EndTime` are specified with `Recurrence`, they form the boundaries of when the recurring action starts and stops.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ScheduledActionARN **
The Amazon Resource Name (ARN) of the scheduled action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ScheduledActionName **
The name of the scheduled action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** StartTime **
The date and time in UTC for this action to start. For example, `"2019-06-01T00:00:00Z"`.
Type: Timestamp
Required: No

 ** Time **
This property is no longer used.
Type: Timestamp
Required: No

 ** TimeZone **
The time zone for the cron expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_ScheduledUpdateGroupAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/ScheduledUpdateGroupAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/ScheduledUpdateGroupAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/ScheduledUpdateGroupAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
