---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LoadBalancerState.html
---

# LoadBalancerState
<a name="API_LoadBalancerState"></a>

Describes the state of a Classic Load Balancer.

## Contents
<a name="API_LoadBalancerState_Contents"></a>

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** State **
One of the following load balancer states:
+  `Adding` - The Auto Scaling instances are being registered with the load balancer.
+  `Added` - All Auto Scaling instances are registered with the load balancer.
+  `InService` - At least one Auto Scaling instance passed an `ELB` health check.
+  `Removing` - The Auto Scaling instances are being deregistered from the load balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances.
+  `Removed` - All Auto Scaling instances are deregistered from the load balancer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_LoadBalancerState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/LoadBalancerState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/LoadBalancerState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/LoadBalancerState)
