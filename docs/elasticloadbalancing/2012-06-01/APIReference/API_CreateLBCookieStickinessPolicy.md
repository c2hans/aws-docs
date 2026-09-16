---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLBCookieStickinessPolicy.html
---

# CreateLBCookieStickinessPolicy
<a name="API_CreateLBCookieStickinessPolicy"></a>

Generates a stickiness policy with sticky session lifetimes controlled by the lifetime of the browser (user-agent) or a specified expiration period. This policy can be associated only with HTTP/HTTPS listeners.

When a load balancer implements this policy, the load balancer uses a special cookie to track the instance for each request. When the load balancer receives a request, it first checks to see if this cookie is present in the request. If so, the load balancer sends the request to the application server specified in the cookie. If not, the load balancer sends the request to a server that is chosen based on the existing load-balancing algorithm.

A cookie is inserted into the response for binding subsequent requests from the same user to that server. The validity of the cookie is based on the cookie expiration time, which is specified in the policy configuration.

For more information, see [Duration-based session stickiness](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-duration) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_CreateLBCookieStickinessPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CookieExpirationPeriod **
The time period, in seconds, after which the cookie should be considered stale. If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.
Type: Long
Required: No

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

 ** PolicyName **
The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.
Type: String
Required: Yes

## Errors
<a name="API_CreateLBCookieStickinessPolicy_Errors"></a>

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

 ** TooManyPolicies **
The quota for the number of policies for this load balancer has been reached.
HTTP Status Code: 400

## Examples
<a name="API_CreateLBCookieStickinessPolicy_Examples"></a>

### Generate a stickiness policy
<a name="API_CreateLBCookieStickinessPolicy_Example_1"></a>

This example generates a stickiness policy with sticky session lifetimes controlled by the specified expiration period.

#### Sample Request
<a name="API_CreateLBCookieStickinessPolicy_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLBCookieStickinessPolicy
&LoadBalancerName=my-loadbalancer
&PolicyName=my-duration-sticky-policy
&CookieExpirationPeriod=60
&Version=2012-06-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateLBCookieStickinessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy)
