---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SetLoadBalancerPoliciesForBackendServer.html
---

# SetLoadBalancerPoliciesForBackendServer
<a name="API_SetLoadBalancerPoliciesForBackendServer"></a>

Replaces the set of policies associated with the specified port on which the EC2 instance is listening with a new set of policies. At this time, only the back-end server authentication policy type can be applied to the instance ports; this policy type is composed of multiple public key policies.

Each time you use `SetLoadBalancerPoliciesForBackendServer` to enable the policies, use the `PolicyNames` parameter to list the policies that you want to enable.

You can use [DescribeLoadBalancers](API_DescribeLoadBalancers.md) or [DescribeLoadBalancerPolicies](API_DescribeLoadBalancerPolicies.md) to verify that the policy is associated with the EC2 instance.

For more information about enabling back-end instance authentication, see [Configure back-end instance authentication](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.html#configure_backendauth_clt) in the *User Guide for Classic Load Balancers*. For more information about Proxy Protocol, see [Configure proxy protocol support](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-proxy-protocol.html) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_SetLoadBalancerPoliciesForBackendServer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** InstancePort **
The port number associated with the EC2 instance.
Type: Integer
Required: Yes

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

 **PolicyNames.member.N**
The names of the policies. If the list is empty, then all current polices are removed from the EC2 instance.
Type: Array of strings
Required: Yes

## Errors
<a name="API_SetLoadBalancerPoliciesForBackendServer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** PolicyNotFound **
One or more of the specified policies do not exist.
HTTP Status Code: 400

## Examples
<a name="API_SetLoadBalancerPoliciesForBackendServer_Examples"></a>

### Replace policies
<a name="API_SetLoadBalancerPoliciesForBackendServer_Example_1"></a>

This example replaces the policies that are currently associated with the specified port with the specified policies.

#### Sample Request
<a name="API_SetLoadBalancerPoliciesForBackendServer_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=SetLoadBalancerPoliciesForBackendServer
&LoadBalancerName=my-loadbalancer
&InstancePort=80
&PolicyNames.member.1=EnableProxyProtocol
&PolicyNames.member.2=my-policy2
&PolicyNames.member.3=my-policy3
&Version=2012-06-01
&AUTHPARAMS
```

## See Also
<a name="API_SetLoadBalancerPoliciesForBackendServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer)
