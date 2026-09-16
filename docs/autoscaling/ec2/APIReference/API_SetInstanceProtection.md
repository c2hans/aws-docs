---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SetInstanceProtection.html
---

# SetInstanceProtection
<a name="API_SetInstanceProtection"></a>

Updates the instance protection settings of the specified instances. This operation cannot be called on instances in a warm pool.

For more information, see [Use instance scale-in protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html) in the *Amazon EC2 Auto Scaling User Guide*.

If you exceed your maximum limit of instance IDs, which is 50 per Auto Scaling group, the call fails.

## Request Parameters
<a name="API_SetInstanceProtection_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **InstanceIds.member.N**
One or more instance IDs. You can specify up to 50 instances.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** ProtectedFromScaleIn **
Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.
Type: Boolean
Required: Yes

## Errors
<a name="API_SetInstanceProtection_Errors"></a>

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
<a name="API_SetInstanceProtection_Examples"></a>

### Example
<a name="API_SetInstanceProtection_Example_1"></a>

This example illustrates one usage of SetInstanceProtection.

#### Sample Request
<a name="API_SetInstanceProtection_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=SetInstanceProtection
&AutoScalingGroupName=my-asg
&InstanceIds.member.1=i-1234567890abcdef0
&ProtectedFromScaleIn=false
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_SetInstanceProtection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/SetInstanceProtection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/SetInstanceProtection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/SetInstanceProtection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/SetInstanceProtection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/SetInstanceProtection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/SetInstanceProtection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/SetInstanceProtection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/SetInstanceProtection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/SetInstanceProtection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/SetInstanceProtection)
