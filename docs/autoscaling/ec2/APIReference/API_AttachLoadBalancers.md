---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancers.html
---

# AttachLoadBalancers
<a name="API_AttachLoadBalancers"></a>

**Note**
This API operation is superseded by [AttachTrafficSources](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html), which can attach multiple traffic sources types. We recommend using `AttachTrafficSources` to simplify how you manage traffic sources. However, we continue to support `AttachLoadBalancers`. You can use both the original `AttachLoadBalancers` API operation and `AttachTrafficSources` on the same Auto Scaling group.

Attaches one or more Classic Load Balancers to the specified Auto Scaling group. Amazon EC2 Auto Scaling registers the running instances with these Classic Load Balancers.

To describe the load balancers for an Auto Scaling group, call the [DescribeLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancers.html) API. To detach a load balancer from the Auto Scaling group, call the [DetachLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancers.html) API.

This operation is additive and does not detach existing Classic Load Balancers or target groups from the Auto Scaling group.

For more information, see [Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_AttachLoadBalancers_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **LoadBalancerNames.member.N**
The names of the load balancers. You can specify up to 10 load balancers.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

## Errors
<a name="API_AttachLoadBalancers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InstanceRefreshInProgress **
The request failed because an active instance refresh already exists for the specified Auto Scaling group.
HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ServiceLinkedRoleFailure **
The service-linked role is not yet ready for use.
HTTP Status Code: 500

## Examples
<a name="API_AttachLoadBalancers_Examples"></a>

### Example
<a name="API_AttachLoadBalancers_Example_1"></a>

This example illustrates one usage of AttachLoadBalancers.

#### Sample Request
<a name="API_AttachLoadBalancers_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=AttachLoadBalancers
&AutoScalingGroupName=my-asg
&LoadBalancerNames.member.1=my-lb
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_AttachLoadBalancers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/AttachLoadBalancers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/AttachLoadBalancers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/AttachLoadBalancers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/AttachLoadBalancers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/AttachLoadBalancers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/AttachLoadBalancers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/AttachLoadBalancers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/AttachLoadBalancers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/AttachLoadBalancers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/AttachLoadBalancers)
