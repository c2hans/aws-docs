---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AddListenerCertificates.html
---

# AddListenerCertificates
<a name="API_AddListenerCertificates"></a>

Adds the specified SSL server certificate to the certificate list for the specified HTTPS or TLS listener.

If the certificate in already in the certificate list, the call is successful but the certificate is not added again.

To get the certificate list for a listener, use [DescribeListenerCertificates](API_DescribeListenerCertificates.md). To remove certificates from the certificate list for a listener, use [RemoveListenerCertificates](API_RemoveListenerCertificates.md). To replace the default certificate for a listener, use [ModifyListener](API_ModifyListener.md).

For more information, see [SSL certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/https-listener-certificates.html) in the *Application Load Balancers Guide* or [Server certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/tls-listener-certificates.html) in the *Network Load Balancers Guide*.

## Request Parameters
<a name="API_AddListenerCertificates_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Certificates.member.N**
The certificate to add. You can specify one certificate per call. Set `CertificateArn` to the certificate ARN but do not set `IsDefault`.
Type: Array of [Certificate](API_Certificate.md) objects
Required: Yes

 ** ListenerArn **
The Amazon Resource Name (ARN) of the listener.
Type: String
Required: Yes

## Response Elements
<a name="API_AddListenerCertificates_ResponseElements"></a>

The following element is returned by the service.

 **Certificates.member.N**
Information about the certificates in the certificate list.
Type: Array of [Certificate](API_Certificate.md) objects

## Errors
<a name="API_AddListenerCertificates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CertificateNotFound **
The specified certificate does not exist.
HTTP Status Code: 400

 ** ListenerNotFound **
The specified listener does not exist.
HTTP Status Code: 400

 ** TooManyCertificates **
You've reached the limit on the number of certificates per load balancer.
HTTP Status Code: 400

## See Also
<a name="API_AddListenerCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/AddListenerCertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/AddListenerCertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/AddListenerCertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/AddListenerCertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/AddListenerCertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/AddListenerCertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/AddListenerCertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/AddListenerCertificates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/AddListenerCertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/AddListenerCertificates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
