---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutLifecycleHook.html
---

# PutLifecycleHook
<a name="API_PutLifecycleHook"></a>

Creates or updates a lifecycle hook for the specified Auto Scaling group.

Lifecycle hooks let you create solutions that are aware of events in the Auto Scaling instance lifecycle, and then perform a custom action on instances when the corresponding lifecycle event occurs.

This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:

1. (Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.

1. (Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.

1. (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.

1.  **Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.**

1. If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state using the [RecordLifecycleActionHeartbeat](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RecordLifecycleActionHeartbeat.html) API call.

1. If you finish before the timeout period ends, send a callback by using the [CompleteLifecycleAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html) API call.

For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.

If you exceed your maximum limit of lifecycle hooks, which by default is 50 per Auto Scaling group, the call fails.

You can view the lifecycle hooks for an Auto Scaling group using the [DescribeLifecycleHooks](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLifecycleHooks.html) API call. If you are no longer using a lifecycle hook, you can delete it by calling the [DeleteLifecycleHook](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteLifecycleHook.html) API.

## Request Parameters
<a name="API_PutLifecycleHook_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** DefaultResult **
The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The default value is `ABANDON`.
Valid values: `CONTINUE` \| `ABANDON`
Type: String
Required: No

 ** HeartbeatTimeout **
The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from `30` to `7200` seconds. The default value is `3600` seconds (1 hour).
Type: Integer
Required: No

 ** LifecycleHookName **
The name of the lifecycle hook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: Yes

 ** LifecycleTransition **
The lifecycle transition. For Auto Scaling groups, there are two major lifecycle transitions.
+ To create a lifecycle hook for scale-out events, specify `autoscaling:EC2_INSTANCE_LAUNCHING`.
+ To create a lifecycle hook for scale-in events, specify `autoscaling:EC2_INSTANCE_TERMINATING`.
Required for new lifecycle hooks, but optional when updating existing hooks.
Type: String
Required: No

 ** NotificationMetadata **
Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Pattern: `[\u0009\u000A\u000D\u0020-\u007e]+`
Required: No

 ** NotificationTargetARN **
The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in a wait state for the lifecycle hook. You can specify either an Amazon SNS topic or an Amazon SQS queue.
If you specify an empty string, this overrides the current ARN.
This operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key-value pair format when sending notifications to an Amazon SNS topic.
When you specify a notification target, Amazon EC2 Auto Scaling sends it a test message. Test messages contain the following additional key-value pair: `"Event": "autoscaling:TEST_NOTIFICATION"`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** RoleARN **
The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.
Valid only if the notification target is an Amazon SNS topic or an Amazon SQS queue. Required for new lifecycle hooks, but optional when updating existing hooks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Errors
<a name="API_PutLifecycleHook_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceeded **
You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see [DescribeAccountLimits](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html).
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_PutLifecycleHook_Examples"></a>

### Example
<a name="API_PutLifecycleHook_Example_1"></a>

This example illustrates one usage of PutLifecycleHook.

#### Sample Request
<a name="API_PutLifecycleHook_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=PutLifecycleHook
&LifecycleHookName=my-launch-lifecycle-hook
&HeartbeatTimeout=300
&AutoScalingGroupName=my-asg
&LifecycleTransition=autoscaling:EC2_INSTANCE_LAUNCHING
&DefaultResult=CONTINUE
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_PutLifecycleHook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/PutLifecycleHook)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/PutLifecycleHook)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/PutLifecycleHook)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/PutLifecycleHook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/PutLifecycleHook)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/PutLifecycleHook)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/PutLifecycleHook)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/PutLifecycleHook)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/PutLifecycleHook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/PutLifecycleHook)
