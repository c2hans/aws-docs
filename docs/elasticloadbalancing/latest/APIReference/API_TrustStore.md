---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TrustStore.html
---

# TrustStore
<a name="API_TrustStore"></a>

Information about a trust store.

## Contents
<a name="API_TrustStore_Contents"></a>

 ** Name **
The name of the trust store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([a-zA-Z0-9]+-)*[a-zA-Z0-9]+$`
Required: No

 ** NumberOfCaCertificates **
The number of ca certificates in the trust store.
Type: Integer
Required: No

 ** Status **
The current status of the trust store.
Type: String
Valid Values: `ACTIVE | CREATING`
Required: No

 ** TotalRevokedEntries **
The number of revoked certificates in the trust store.
Type: Long
Required: No

 ** TrustStoreArn **
The Amazon Resource Name (ARN) of the trust store.
Type: String
Required: No

## See Also
<a name="API_TrustStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/TrustStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/TrustStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/TrustStore)
