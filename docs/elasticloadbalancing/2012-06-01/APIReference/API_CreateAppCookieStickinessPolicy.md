---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateAppCookieStickinessPolicy.html
---

# CreateAppCookieStickinessPolicy
<a name="API_CreateAppCookieStickinessPolicy"></a>

Generates a stickiness policy with sticky session lifetimes that follow that of an application-generated cookie. This policy can be associated only with HTTP/HTTPS listeners.

This policy is similar to the policy created by [CreateLBCookieStickinessPolicy](API_CreateLBCookieStickinessPolicy.md), except that the lifetime of the special Elastic Load Balancing cookie, `AWSELB`, follows the lifetime of the application-generated cookie specified in the policy configuration. The load balancer only inserts a new stickiness cookie when the application response includes a new application cookie.

If the application cookie is explicitly removed or expires, the session stops being sticky until a new application cookie is issued.

For more information, see [Application-controlled session stickiness](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-application) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_CreateAppCookieStickinessPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CookieName **
The name of the application cookie used for stickiness.
Type: String
Required: Yes

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

 ** PolicyName **
The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.
Type: String
Required: Yes

## Errors
<a name="API_CreateAppCookieStickinessPolicy_Errors"></a>

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
<a name="API_CreateAppCookieStickinessPolicy_Examples"></a>

### Generate a stickiness policy
<a name="API_CreateAppCookieStickinessPolicy_Example_1"></a>

This example generates a stickiness policy that follows the sticky session lifetimes of the application-generated cookie.

#### Sample Request
<a name="API_CreateAppCookieStickinessPolicy_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateAppCookieStickinessPolicy
&LoadBalancerName=my-loadbalancer
&PolicyName=my-app-sticky-policy
&CookieName=my-app-cookie
&Version=2012-06-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateAppCookieStickinessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy)
