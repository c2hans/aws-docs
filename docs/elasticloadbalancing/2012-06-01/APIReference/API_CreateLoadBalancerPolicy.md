---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancerPolicy.html
---

# CreateLoadBalancerPolicy
<a name="API_CreateLoadBalancerPolicy"></a>

Creates a policy with the specified attributes for the specified load balancer.

Policies are settings that are saved for your load balancer and that can be applied to the listener or the application server, depending on the policy type.

## Request Parameters
<a name="API_CreateLoadBalancerPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

 **PolicyAttributes.member.N**
The policy attributes.
Type: Array of [PolicyAttribute](API_PolicyAttribute.md) objects
Required: No

 ** PolicyName **
The name of the load balancer policy to be created. This name must be unique within the set of policies for this load balancer.
Type: String
Required: Yes

 ** PolicyTypeName **
The name of the base policy type. To get the list of policy types, use [DescribeLoadBalancerPolicyTypes](API_DescribeLoadBalancerPolicyTypes.md).
Type: String
Required: Yes

## Errors
<a name="API_CreateLoadBalancerPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicatePolicyName **
A policy with the specified name already exists for this load balancer.
HTTP Status Code: 400

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** PolicyTypeNotFound **
One or more of the specified policy types do not exist.
HTTP Status Code: 400

 ** TooManyPolicies **
The quota for the number of policies for this load balancer has been reached.
HTTP Status Code: 400

## Examples
<a name="API_CreateLoadBalancerPolicy_Examples"></a>

### Enable proxy protocol
<a name="API_CreateLoadBalancerPolicy_Example_1"></a>

This example creates a policy that enables proxy protocol on the specified load balancer.

#### Sample Request
<a name="API_CreateLoadBalancerPolicy_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLoadBalancerPolicy
&LoadBalancerName=my-loadbalancer
&PolicyName=EnableProxyProtocol
&PolicyTypeName=ProxyProtocolPolicyType
&PolicyAttributes.member.1.AttributeName=ProxyProtocol
&PolicyAttributes.member.1.AttributeValue=true
&Version=2012-06-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateLoadBalancerPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy)
