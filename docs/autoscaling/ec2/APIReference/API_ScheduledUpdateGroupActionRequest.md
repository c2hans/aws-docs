---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ScheduledUpdateGroupActionRequest.html
---

# ScheduledUpdateGroupActionRequest
<a name="API_ScheduledUpdateGroupActionRequest"></a>

Describes information used for one or more scheduled scaling action updates in a [BatchPutScheduledUpdateGroupAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BatchPutScheduledUpdateGroupAction.html) operation.

## Contents
<a name="API_ScheduledUpdateGroupActionRequest_Contents"></a>

 ** ScheduledActionName **
The name of the scaling action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** DesiredCapacity **
The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
Type: Integer
Required: No

 ** EndTime **
The date and time for the recurring schedule to end, in UTC.
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
The recurring schedule for the action, in Unix cron syntax format. This format consists of five fields separated by white spaces: [Minute] [Hour] [Day\_of\_Month] [Month\_of\_Year] [Day\_of\_Week]. The value must be in quotes (for example, `"30 0 1 1,6,12 *"`). For more information about this format, see [Crontab](http://crontab.org).
When `StartTime` and `EndTime` are specified with `Recurrence`, they form the boundaries of when the recurring action starts and stops.
Cron expressions use Universal Coordinated Time (UTC) by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** StartTime **
The date and time for the action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and in quotes (for example, `"2019-06-01T00:00:00Z"`).
If you specify `Recurrence` and `StartTime`, Amazon EC2 Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.
If you try to schedule the action in the past, Amazon EC2 Auto Scaling returns an error message.
Type: Timestamp
Required: No

 ** TimeZone **
Specifies the time zone for a cron expression. If a time zone is not provided, UTC is used by default.
Valid values are the canonical names of the IANA time zones, derived from the IANA Time Zone Database (such as `Etc/GMT+9` or `Pacific/Tahiti`). For more information, see [https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_ScheduledUpdateGroupActionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/ScheduledUpdateGroupActionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/ScheduledUpdateGroupActionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/ScheduledUpdateGroupActionRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
