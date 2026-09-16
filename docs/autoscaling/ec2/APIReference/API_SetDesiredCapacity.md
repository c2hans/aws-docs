---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SetDesiredCapacity.html
---

# SetDesiredCapacity
<a name="API_SetDesiredCapacity"></a>

Sets the size of the specified Auto Scaling group.

If a scale-in activity occurs as a result of a new `DesiredCapacity` value that is lower than the current size of the group, the Auto Scaling group uses its termination policy to determine which instances to terminate.

For more information, see [Manual scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-manually.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_SetDesiredCapacity_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** DesiredCapacity **
The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain.
Type: Integer
Required: Yes

 ** HonorCooldown **
Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before initiating a scaling activity to set your Auto Scaling group to its new capacity. By default, Amazon EC2 Auto Scaling does not honor the cooldown period during manual scaling activities.
Type: Boolean
Required: No

## Errors
<a name="API_SetDesiredCapacity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ScalingActivityInProgress **
The operation can't be performed because there are scaling activities in progress.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_SetDesiredCapacity_Examples"></a>

### Example
<a name="API_SetDesiredCapacity_Example_1"></a>

This example illustrates one usage of SetDesiredCapacity.

#### Sample Request
<a name="API_SetDesiredCapacity_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=SetDesiredCapacity
&AutoScalingGroupName=my-asg
&HonorCooldown=false
&DesiredCapacity=2
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_SetDesiredCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/SetDesiredCapacity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/SetDesiredCapacity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/SetDesiredCapacity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/SetDesiredCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/SetDesiredCapacity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/SetDesiredCapacity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/SetDesiredCapacity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/SetDesiredCapacity)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/SetDesiredCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/SetDesiredCapacity)
