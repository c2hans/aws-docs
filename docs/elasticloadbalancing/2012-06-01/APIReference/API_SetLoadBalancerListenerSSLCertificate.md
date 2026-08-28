---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SetLoadBalancerListenerSSLCertificate.html
---

# SetLoadBalancerListenerSSLCertificate
<a name="API_SetLoadBalancerListenerSSLCertificate"></a>

Sets the certificate that terminates the specified listener's SSL connections. The specified certificate replaces any prior certificate that was used on the same load balancer and port.

For more information about updating your SSL certificate, see [Replace the SSL certificate for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-update-ssl-cert.html) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_SetLoadBalancerListenerSSLCertificate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

 ** LoadBalancerPort **
The port that uses the specified SSL certificate.
Type: Integer
Required: Yes

 ** SSLCertificateId **
The Amazon Resource Name (ARN) of the SSL certificate.
Type: String
Required: Yes

## Errors
<a name="API_SetLoadBalancerListenerSSLCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CertificateNotFound **
The specified ARN does not refer to a valid SSL certificate in AWS Identity and Access Management (IAM) or AWS Certificate Manager (ACM). Note that if you recently uploaded the certificate to IAM, this error might indicate that the certificate is not fully available yet.
HTTP Status Code: 400

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** ListenerNotFound **
The load balancer does not have a listener configured at the specified port.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** UnsupportedProtocol **
The specified protocol or signature version is not supported.
HTTP Status Code: 400

## Examples
<a name="API_SetLoadBalancerListenerSSLCertificate_Examples"></a>

### Update the SSL certificate
<a name="API_SetLoadBalancerListenerSSLCertificate_Example_1"></a>

This example replaces the existing SSL certificate for the specified HTTPS load balancer.

#### Sample Request
<a name="API_SetLoadBalancerListenerSSLCertificate_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=SetLoadBalancerListenerSSLCertificate
&LoadBalancerName=my-loadbalancer
&SSLCertificateId=arn:aws:iam::123456789012:server-certificate/my-new-server-cert
&LoadBalancerPort=443
&Version=2012-06-01
&AUTHPARAMS
```

## See Also
<a name="API_SetLoadBalancerListenerSSLCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
