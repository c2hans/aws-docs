---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScheduledUpdateGroupAction.html
---

# PutScheduledUpdateGroupAction
<a name="API_PutScheduledUpdateGroupAction"></a>

Creates or updates a scheduled scaling action for an Auto Scaling group.

For more information, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) in the *Amazon EC2 Auto Scaling User Guide*.

You can view the scheduled actions for an Auto Scaling group using the [DescribeScheduledActions](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScheduledActions.html) API call. If you are no longer using a scheduled action, you can delete it by calling the [DeleteScheduledAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteScheduledAction.html) API.

If you try to schedule your action in the past, Amazon EC2 Auto Scaling returns an error message.

## Request Parameters
<a name="API_PutScheduledUpdateGroupAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** DesiredCapacity **
The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain. It can scale beyond this capacity if you add more scaling conditions.
You must specify at least one of the following properties: `MaxSize`, `MinSize`, or `DesiredCapacity`.
Type: Integer
Required: No

 ** EndTime **
The date and time for the recurring schedule to end, in UTC. For example, `"2021-06-01T00:00:00Z"`.
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
The recurring schedule for this action. This format consists of five fields separated by white spaces: [Minute] [Hour] [Day\_of\_Month] [Month\_of\_Year] [Day\_of\_Week]. The value must be in quotes (for example, `"30 0 1 1,6,12 *"`). For more information about this format, see [Crontab](http://crontab.org).
When `StartTime` and `EndTime` are specified with `Recurrence`, they form the boundaries of when the recurring action starts and stops.
Cron expressions use Universal Coordinated Time (UTC) by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ScheduledActionName **
The name of this scaling action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** StartTime **
The date and time for this action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and in quotes (for example, `"2021-06-01T00:00:00Z"`).
If you specify `Recurrence` and `StartTime`, Amazon EC2 Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.
Type: Timestamp
Required: No

 ** Time **
This property is no longer used.
Type: Timestamp
Required: No

 ** TimeZone **
Specifies the time zone for a cron expression. If a time zone is not provided, UTC is used by default.
Valid values are the canonical names of the IANA time zones, derived from the IANA Time Zone Database (such as `Etc/GMT+9` or `Pacific/Tahiti`). For more information, see [https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Errors
<a name="API_PutScheduledUpdateGroupAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExists **
You already have an Auto Scaling group or launch configuration with this name.
 ** message **

HTTP Status Code: 400

 ** LimitExceeded **
You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see [DescribeAccountLimits](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html).
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_PutScheduledUpdateGroupAction_Examples"></a>

### Example 1: Schedule based on a specific date and time
<a name="API_PutScheduledUpdateGroupAction_Example_1"></a>

This example illustrates one usage of PutScheduledUpdateGroupAction.

#### Sample Request
<a name="API_PutScheduledUpdateGroupAction_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=PutScheduledUpdateGroupAction
&AutoScalingGroupName=my-asg
&ScheduledActionName=scale-out
&StartTime=2020-05-25T08:00:00Z
&DesiredCapacity=3
&Version=2011-01-01
&AUTHPARAMS
```

### Example 2: Recurring Schedule
<a name="API_PutScheduledUpdateGroupAction_Example_2"></a>

This example illustrates one usage of PutScheduledUpdateGroupAction.

#### Sample Request
<a name="API_PutScheduledUpdateGroupAction_Example_2_Request"></a>

```
https://autoscaling.amazonaws.com/?Action="PutScheduledUpdateGroupAction
&AutoScalingGroupName=my-asg
&ScheduledActionName=scale-out-schedule-year
&Recurrence="30 0 1 1,6,12 *"
&DesiredCapacity=3
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_PutScheduledUpdateGroupAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/PutScheduledUpdateGroupAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/PutScheduledUpdateGroupAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/PutScheduledUpdateGroupAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/PutScheduledUpdateGroupAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/PutScheduledUpdateGroupAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/PutScheduledUpdateGroupAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/PutScheduledUpdateGroupAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/PutScheduledUpdateGroupAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/PutScheduledUpdateGroupAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/PutScheduledUpdateGroupAction)
