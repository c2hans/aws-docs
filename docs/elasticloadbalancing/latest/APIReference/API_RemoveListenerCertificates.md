---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RemoveListenerCertificates.html
---

# RemoveListenerCertificates
<a name="API_RemoveListenerCertificates"></a>

Removes the specified certificate from the certificate list for the specified HTTPS or TLS listener.

You can't remove the default certificate for a listener. To replace the default certificate, call [ModifyListener](API_ModifyListener.md).

To list the certificates for your listener, use [DescribeListenerCertificates](API_DescribeListenerCertificates.md).

## Request Parameters
<a name="API_RemoveListenerCertificates_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Certificates.member.N**
The certificate to remove. You can specify one certificate per call. Set `CertificateArn` to the certificate ARN but do not set `IsDefault`.
Type: Array of [Certificate](API_Certificate.md) objects
Required: Yes

 ** ListenerArn **
The Amazon Resource Name (ARN) of the listener.
Type: String
Required: Yes

## Errors
<a name="API_RemoveListenerCertificates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ListenerNotFound **
The specified listener does not exist.
HTTP Status Code: 400

 ** OperationNotPermitted **
This operation is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_RemoveListenerCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates)
