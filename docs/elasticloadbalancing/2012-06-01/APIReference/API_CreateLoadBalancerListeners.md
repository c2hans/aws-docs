---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancerListeners.html
---

# CreateLoadBalancerListeners
<a name="API_CreateLoadBalancerListeners"></a>

Creates one or more listeners for the specified load balancer. If a listener with the specified port does not already exist, it is created; otherwise, the properties of the new listener must match the properties of the existing listener.

When updating load balancer listeners in the console, `CreateLoadBalancerListeners` will be logged.

For more information, see [Listeners for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_CreateLoadBalancerListeners_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Listeners.member.N**
The listeners.
Type: Array of [Listener](API_Listener.md) objects
Required: Yes

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

## Errors
<a name="API_CreateLoadBalancerListeners_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CertificateNotFound **
The specified ARN does not refer to a valid SSL certificate in AWS Identity and Access Management (IAM) or AWS Certificate Manager (ACM). Note that if you recently uploaded the certificate to IAM, this error might indicate that the certificate is not fully available yet.
HTTP Status Code: 400

 ** DuplicateListener **
A listener already exists for the specified load balancer name and port, but with a different instance port, protocol, or SSL certificate.
HTTP Status Code: 400

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** UnsupportedProtocol **
The specified protocol or signature version is not supported.
HTTP Status Code: 400

## Examples
<a name="API_CreateLoadBalancerListeners_Examples"></a>

### Create an HTTPS listener
<a name="API_CreateLoadBalancerListeners_Example_1"></a>

This example creates a listener for the specified load balancer using port 443 and the HTTPS protocol.

#### Sample Request
<a name="API_CreateLoadBalancerListeners_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLoadBalancerListeners
&LoadBalancerName=my-https-loadbalancer
&Listeners.member.1.Protocol=https
&Listeners.member.1.LoadBalancerPort=443
&Listeners.member.1.InstancePort=443
&Listeners.member.1.InstanceProtocol=https
&Listeners.member.1.SSLCertificateId=arn:aws:iam::123456789012:server-certificate/my-server-cert
&Version=2012-06-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateLoadBalancerListeners_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
