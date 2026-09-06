---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LifecycleHookSpecification.html
---

# LifecycleHookSpecification
<a name="API_LifecycleHookSpecification"></a>

Describes information used to specify a lifecycle hook for an Auto Scaling group.

Lifecycle hooks let you create solutions that are aware of events in the Auto Scaling instance lifecycle, and then perform a custom action on instances when the corresponding lifecycle event occurs.

This step is a part of the procedure for creating a lifecycle hook for an Auto Scaling group:

1. (Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.

1. (Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.

1. (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.

1.  **Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.**

1. If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state by using the [RecordLifecycleActionHeartbeat](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RecordLifecycleActionHeartbeat.html) API call.

1. If you finish before the timeout period ends, send a callback by using the [CompleteLifecycleAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html) API call.

For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Contents
<a name="API_LifecycleHookSpecification_Contents"></a>

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
Type: String
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

 ** NotificationMetadata **
Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Pattern: `[\u0009\u000A\u000D\u0020-\u007e]+`
Required: No

 ** NotificationTargetARN **
The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling sends notifications to when an instance is in a wait state for the lifecycle hook. You can specify an Amazon SNS topic or an Amazon SQS queue.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** RoleARN **
The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target. For information about creating this role, see [Prepare to add a lifecycle hook to your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/prepare-for-lifecycle-notifications.html) in the *Amazon EC2 Auto Scaling User Guide*.
Valid only if the notification target is an Amazon SNS topic or an Amazon SQS queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_LifecycleHookSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/LifecycleHookSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/LifecycleHookSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/LifecycleHookSpecification)
