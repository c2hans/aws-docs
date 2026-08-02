---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RevocationContent.html
---

# RevocationContent
<a name="API_RevocationContent"></a>

Information about a revocation file.

## Contents
<a name="API_RevocationContent_Contents"></a>

 ** RevocationType **
The type of revocation file.
Type: String
Valid Values: `CRL`
Required: No

 ** S3Bucket **
The Amazon S3 bucket for the revocation file.
Type: String
Required: No

 ** S3Key **
The Amazon S3 path for the revocation file.
Type: String
Required: No

 ** S3ObjectVersion **
The Amazon S3 object version of the revocation file.
Type: String
Required: No

## See Also
<a name="API_RevocationContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/RevocationContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/RevocationContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/RevocationContent)
