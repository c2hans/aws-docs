---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Activity.html
---

# Activity
<a name="API_Activity"></a>

Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

## Contents
<a name="API_Activity_Contents"></a>

 ** ActivityId **
The ID of the activity.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Cause **
The reason the activity began.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** StartTime **
The start time of the activity.
Type: Timestamp
Required: Yes

 ** StatusCode **
The current status of the activity.
Type: String
Valid Values: `PendingSpotBidPlacement | WaitingForSpotInstanceRequestId | WaitingForSpotInstanceId | WaitingForInstanceId | PreInService | InProgress | WaitingForELBConnectionDraining | MidLifecycleAction | WaitingForInstanceWarmup | Successful | Failed | Cancelled | WaitingForConnectionDraining | WaitingForInPlaceUpdateToStart | WaitingForInPlaceUpdateToFinalize | InPlaceUpdateInProgress`
Required: Yes

 ** AutoScalingGroupARN **
The Amazon Resource Name (ARN) of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** AutoScalingGroupState **
The state of the Auto Scaling group, which is either `InService` or `Deleted`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** Description **
A friendly, more verbose description of the activity.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Details **
The details about the activity.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** EndTime **
The end time of the activity.
Type: Timestamp
Required: No

 ** Progress **
A value between 0 and 100 that indicates the progress of the activity.
Type: Integer
Required: No

 ** StatusMessage **
A friendly, more verbose description of the activity status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_Activity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/Activity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/Activity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/Activity)
