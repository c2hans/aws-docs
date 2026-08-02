---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TrustStoreRevocation.html
---

# TrustStoreRevocation
<a name="API_TrustStoreRevocation"></a>

Information about a revocation file in use by a trust store.

## Contents
<a name="API_TrustStoreRevocation_Contents"></a>

 ** NumberOfRevokedEntries **
The number of revoked certificates.
Type: Long
Required: No

 ** RevocationId **
The revocation ID of the revocation file.
Type: Long
Required: No

 ** RevocationType **
The type of revocation file.
Type: String
Valid Values: `CRL`
Required: No

 ** TrustStoreArn **
The Amazon Resource Name (ARN) of the trust store.
Type: String
Required: No

## See Also
<a name="API_TrustStoreRevocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/TrustStoreRevocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/TrustStoreRevocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/TrustStoreRevocation)
