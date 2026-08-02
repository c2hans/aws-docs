---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancerTargetGroups.html
---

# DetachLoadBalancerTargetGroups
<a name="API_DetachLoadBalancerTargetGroups"></a>

**Note**
This API operation is superseded by [DetachTrafficSources](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachTrafficSources.html), which can detach multiple traffic sources types. We recommend using `DetachTrafficSources` to simplify how you manage traffic sources. However, we continue to support `DetachLoadBalancerTargetGroups`. You can use both the original `DetachLoadBalancerTargetGroups` API operation and `DetachTrafficSources` on the same Auto Scaling group.

Detaches one or more target groups from the specified Auto Scaling group.

When you detach a target group, it enters the `Removing` state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the target group using the [DescribeLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancerTargetGroups.html) API call. The instances remain running.

**Note**
You can use this operation to detach target groups that were attached by using [AttachLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancerTargetGroups.html), but not for target groups that were attached by using [AttachTrafficSources](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html).

## Request Parameters
<a name="API_DetachLoadBalancerTargetGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **TargetGroupARNs.member.N**
The Amazon Resource Names (ARN) of the target groups. You can specify up to 10 target groups.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 511.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

## Errors
<a name="API_DetachLoadBalancerTargetGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## See Also
<a name="API_DetachLoadBalancerTargetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups)
