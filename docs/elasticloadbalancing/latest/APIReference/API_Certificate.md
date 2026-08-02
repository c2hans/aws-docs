---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Certificate.html
---

# Certificate
<a name="API_Certificate"></a>

Information about an SSL server certificate.

## Contents
<a name="API_Certificate_Contents"></a>

 ** CertificateArn **
The Amazon Resource Name (ARN) of the certificate.
Type: String
Required: No

 ** IsDefault **
Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.
Type: Boolean
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/Certificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/Certificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/Certificate)
