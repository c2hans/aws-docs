---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SetLoadBalancerPoliciesOfListener.html
---

# SetLoadBalancerPoliciesOfListener
<a name="API_SetLoadBalancerPoliciesOfListener"></a>

Replaces the current set of policies for the specified load balancer port with the specified set of policies.

To enable back-end server authentication, use [SetLoadBalancerPoliciesForBackendServer](API_SetLoadBalancerPoliciesForBackendServer.md).

For more information about setting policies, see [Update the SSL negotiation configuration](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html), [Duration-based session stickiness](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-duration), and [Application-controlled session stickiness](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-application) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_SetLoadBalancerPoliciesOfListener_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

 ** LoadBalancerPort **
The external port of the load balancer.
Type: Integer
Required: Yes

 **PolicyNames.member.N**
The names of the policies. This list must include all policies to be enabled. If you omit a policy that is currently enabled, it is disabled. If the list is empty, all current policies are disabled.
Type: Array of strings
Required: Yes

## Errors
<a name="API_SetLoadBalancerPoliciesOfListener_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** ListenerNotFound **
The load balancer does not have a listener configured at the specified port.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** PolicyNotFound **
One or more of the specified policies do not exist.
HTTP Status Code: 400

## Examples
<a name="API_SetLoadBalancerPoliciesOfListener_Examples"></a>

### Replace policies
<a name="API_SetLoadBalancerPoliciesOfListener_Example_1"></a>

This example replaces the policies that are currently associated with the specified port with the specified policy. Note that this is the only policy that is enabled after this call. To ensure that any currently enabled policies remain enabled, add them to the PolicyNames list.

#### Sample Request
<a name="API_SetLoadBalancerPoliciesOfListener_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=SetLoadBalancerPoliciesOfListener
&LoadBalancerName=my-loadbalancer
&LoadBalancerPort=443
&PolicyNames.member.1=my-SSLNegotiation-policy
&Version=2012-06-01
&AUTHPARAMS
```

## See Also
<a name="API_SetLoadBalancerPoliciesOfListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener)
