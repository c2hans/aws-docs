---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancers.html
---

# DetachLoadBalancers
<a name="API_DetachLoadBalancers"></a>

**Note**
This API operation is superseded by [DetachTrafficSources](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachTrafficSources.html), which can detach multiple traffic sources types. We recommend using `DetachTrafficSources` to simplify how you manage traffic sources. However, we continue to support `DetachLoadBalancers`. You can use both the original `DetachLoadBalancers` API operation and `DetachTrafficSources` on the same Auto Scaling group.

Detaches one or more Classic Load Balancers from the specified Auto Scaling group.

This operation detaches only Classic Load Balancers. If you have Application Load Balancers, Network Load Balancers, or Gateway Load Balancers, use the [DetachLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancerTargetGroups.html) API instead.

When you detach a load balancer, it enters the `Removing` state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the load balancer using the [DescribeLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancers.html) API call. The instances remain running.

## Request Parameters
<a name="API_DetachLoadBalancers_RequestParameters"></a>

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
<a name="API_DetachLoadBalancers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DetachLoadBalancers_Examples"></a>

### Example
<a name="API_DetachLoadBalancers_Example_1"></a>

This example illustrates one usage of DetachLoadBalancers.

#### Sample Request
<a name="API_DetachLoadBalancers_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DetachLoadBalancers
&AutoScalingGroupName=my-asg
&LoadBalancerNames.member.1=my-lb
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_DetachLoadBalancers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DetachLoadBalancers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DetachLoadBalancers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DetachLoadBalancers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DetachLoadBalancers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DetachLoadBalancers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DetachLoadBalancers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DetachLoadBalancers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DetachLoadBalancers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DetachLoadBalancers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DetachLoadBalancers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
