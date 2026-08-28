---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInstanceEventWindow.html
---

# CreateInstanceEventWindow
<a name="API_CreateInstanceEventWindow"></a>

Creates an event window in which scheduled events for the associated Amazon EC2 instances can run.

You can define either a set of time ranges or a cron expression when creating the event window, but not both. All event window times are in UTC.

You can create up to 200 event windows per AWS Region.

When you create the event window, targets (instance IDs, Dedicated Host IDs, or tags) are not yet associated with it. To ensure that the event window can be used, you must associate one or more targets with it by using the [AssociateInstanceEventWindow](API_AssociateInstanceEventWindow.md) API.

**Important**
Event windows are applicable only for scheduled events that stop, reboot, or terminate instances.
Event windows are *not* applicable for:
Expedited scheduled events and network maintenance events.
Unscheduled maintenance such as AutoRecovery and unplanned reboots.

For more information, see [Define event windows for scheduled events](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateInstanceEventWindow_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CronExpression**
The cron expression for the event window, for example, `* 0-4,20-23 * * 1,5`. If you specify a cron expression, you can't specify a time range.
Constraints:
+ Only hour and day of the week values are supported.
+ For day of the week values, you can specify either integers `0` through `6`, or alternative single values `SUN` through `SAT`.
+ The minute, month, and year must be specified by `*`.
+ The hour value must be one or a multiple range, for example, `0-4` or `0-4,20-23`.
+ Each hour range must be >= 2 hours, for example, `0-2` or `20-23`.
+ The event window must be >= 4 hours. The combined total time ranges in the event window must be >= 4 hours.
For more information about cron expressions, see [cron](https://en.wikipedia.org/wiki/Cron) on the *Wikipedia website*.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Name**
The name of the event window.
Type: String
Required: No

 **TagSpecification.N**
The tags to apply to the event window.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TimeRange.N**
The time range for the event window. If you specify a time range, you can't specify a cron expression.
Type: Array of [InstanceEventWindowTimeRangeRequest](API_InstanceEventWindowTimeRangeRequest.md) objects
Required: No

## Response Elements
<a name="API_CreateInstanceEventWindow_ResponseElements"></a>

The following elements are returned by the service.

 **instanceEventWindow**
Information about the event window.
Type: [InstanceEventWindow](API_InstanceEventWindow.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateInstanceEventWindow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateInstanceEventWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateInstanceEventWindow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateInstanceEventWindow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateInstanceEventWindow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateInstanceEventWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateInstanceEventWindow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateInstanceEventWindow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateInstanceEventWindow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateInstanceEventWindow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateInstanceEventWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateInstanceEventWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
