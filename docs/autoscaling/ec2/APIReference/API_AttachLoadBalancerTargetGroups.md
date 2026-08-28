---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancerTargetGroups.html
---

# AttachLoadBalancerTargetGroups
<a name="API_AttachLoadBalancerTargetGroups"></a>

**Note**
This API operation is superseded by [AttachTrafficSources](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html), which can attach multiple traffic sources types. We recommend using `AttachTrafficSources` to simplify how you manage traffic sources. However, we continue to support `AttachLoadBalancerTargetGroups`. You can use both the original `AttachLoadBalancerTargetGroups` API operation and `AttachTrafficSources` on the same Auto Scaling group.

Attaches one or more target groups to the specified Auto Scaling group.

This operation is used with the following load balancer types:
+ Application Load Balancer - Operates at the application layer (layer 7) and supports HTTP and HTTPS.
+ Network Load Balancer - Operates at the transport layer (layer 4) and supports TCP, TLS, and UDP.
+ Gateway Load Balancer - Operates at the network layer (layer 3).

To describe the target groups for an Auto Scaling group, call the [DescribeLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancerTargetGroups.html) API. To detach the target group from the Auto Scaling group, call the [DetachLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancerTargetGroups.html) API.

This operation is additive and does not detach existing target groups or Classic Load Balancers from the Auto Scaling group.

For more information, see [Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_AttachLoadBalancerTargetGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **TargetGroupARNs.member.N**
The Amazon Resource Names (ARNs) of the target groups. You can specify up to 10 target groups. To get the ARN of a target group, use the Elastic Load Balancing [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html) API operation.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 511.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

## Errors
<a name="API_AttachLoadBalancerTargetGroups_Errors"></a>

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
<a name="API_AttachLoadBalancerTargetGroups_Examples"></a>

### Example
<a name="API_AttachLoadBalancerTargetGroups_Example_1"></a>

This example illustrates one usage of AttachLoadBalancerTargetGroups.

#### Sample Request
<a name="API_AttachLoadBalancerTargetGroups_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=AttachLoadBalancerTargetGroups
&AutoScalingGroupName=my-asg
&TargetGroupARNs.member.1=arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/1234567890123456
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_AttachLoadBalancerTargetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
