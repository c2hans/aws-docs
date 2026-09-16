---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html
---

# CompleteLifecycleAction
<a name="API_CompleteLifecycleAction"></a>

Completes the lifecycle action for the specified token or instance with the specified result.

This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:

1. (Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.

1. (Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.

1. (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.

1. Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.

1. If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state.

1.  **If you finish before the timeout period ends, send a callback by using the [CompleteLifecycleAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html) API call.**

For more information, see [Complete a lifecycle action](https://docs.aws.amazon.com/autoscaling/ec2/userguide/completing-lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_CompleteLifecycleAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** InstanceId **
The ID of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LifecycleActionResult **
The action for the group to take. You can specify either `CONTINUE` or `ABANDON`.
Type: String
Required: Yes

 ** LifecycleActionToken **
A universally unique identifier (UUID) that identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** LifecycleHookName **
The name of the lifecycle hook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: Yes

## Errors
<a name="API_CompleteLifecycleAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_CompleteLifecycleAction_Examples"></a>

### Example
<a name="API_CompleteLifecycleAction_Example_1"></a>

This example illustrates one usage of CompleteLifecycleAction.

#### Sample Request
<a name="API_CompleteLifecycleAction_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=CompleteLifecycleAction
&AutoScalingGroupName=my-asg
&LifecycleHookName=my-lifecycle-hook
&LifecycleActionResult=CONTINUE
&LifecycleActionToken=bcd2f1b8-9a78-44d3-8a7a-4dd07EXAMPLE
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_CompleteLifecycleAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/CompleteLifecycleAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/CompleteLifecycleAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/CompleteLifecycleAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/CompleteLifecycleAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/CompleteLifecycleAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/CompleteLifecycleAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/CompleteLifecycleAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/CompleteLifecycleAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/CompleteLifecycleAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/CompleteLifecycleAction)
