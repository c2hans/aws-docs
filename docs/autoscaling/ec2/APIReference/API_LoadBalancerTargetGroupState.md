---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LoadBalancerTargetGroupState.html
---

# LoadBalancerTargetGroupState
<a name="API_LoadBalancerTargetGroupState"></a>

Describes the state of a target group.

## Contents
<a name="API_LoadBalancerTargetGroupState_Contents"></a>

 ** LoadBalancerTargetGroupARN **
The Amazon Resource Name (ARN) of the target group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 511.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** State **
The state of the target group.
+  `Adding` - The Auto Scaling instances are being registered with the target group.
+  `Added` - All Auto Scaling instances are registered with the target group.
+  `InService` - At least one Auto Scaling instance passed an `ELB` health check.
+  `Removing` - The Auto Scaling instances are being deregistered from the target group. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances.
+  `Removed` - All Auto Scaling instances are deregistered from the target group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_LoadBalancerTargetGroupState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/LoadBalancerTargetGroupState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/LoadBalancerTargetGroupState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/LoadBalancerTargetGroupState)
