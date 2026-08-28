---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LifecycleHook.html
---

# LifecycleHook
<a name="API_LifecycleHook"></a>

Describes a lifecycle hook. A lifecycle hook lets you create solutions that are aware of events in the Auto Scaling instance lifecycle, and then perform a custom action on instances when the corresponding lifecycle event occurs.

## Contents
<a name="API_LifecycleHook_Contents"></a>

 ** AutoScalingGroupName **
The name of the Auto Scaling group for the lifecycle hook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** DefaultResult **
The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs.
Valid values: `CONTINUE` \| `ABANDON`
Type: String
Required: No

 ** GlobalTimeout **
The maximum time, in seconds, that an instance can remain in a wait state. The maximum is 172800 seconds (48 hours) or 100 times `HeartbeatTimeout`, whichever is smaller.
Type: Integer
Required: No

 ** HeartbeatTimeout **
The maximum time, in seconds, that can elapse before the lifecycle hook times out. If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the `DefaultResult` property.
Type: Integer
Required: No

 ** LifecycleHookName **
The name of the lifecycle hook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: No

 ** LifecycleTransition **
The lifecycle transition.
Valid values: `autoscaling:EC2_INSTANCE_LAUNCHING` \| `autoscaling:EC2_INSTANCE_TERMINATING`
Type: String
Required: No

 ** NotificationMetadata **
Additional information that is included any time Amazon EC2 Auto Scaling sends a message to the notification target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Pattern: `[\u0009\u000A\u000D\u0020-\u007e]+`
Required: No

 ** NotificationTargetARN **
The ARN of the target that Amazon EC2 Auto Scaling sends notifications to when an instance is in a wait state for the lifecycle hook.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** RoleARN **
The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target (an Amazon SNS topic or an Amazon SQS queue).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_LifecycleHook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/LifecycleHook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/LifecycleHook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/LifecycleHook)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
