---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_MutualAuthenticationAttributes.html
---

# MutualAuthenticationAttributes

Information about the mutual authentication attributes of a listener.

## Contents
<a name="API_MutualAuthenticationAttributes_Contents"></a>

 ** AdvertiseTrustStoreCaNames **
Indicates whether trust store CA certificate names are advertised.
Type: String
Valid Values: `on | off`
Required: No

 ** ClientCertificateIdentityFilters.member.N **
[Network Load Balancers] The client certificate identity filters. The load balancer admits a connection only if the client certificate matches at least one filter. If you don't specify any filters, the load balancer admits every client certificate that passes trust store validation and revocation checks.
You can specify filters only when the mode is `verify`. You can specify up to 100 filters per listener.
Type: Array of [ClientCertificateIdentityFilter](API_ClientCertificateIdentityFilter.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** IgnoreClientCertificateExpiry **
Indicates whether expired client certificates are ignored.
Type: Boolean
Required: No

 ** Mode **
The client certificate handling method. The default value is `off`.
[Application Load Balancers] The possible values are `off`, `passthrough`, and `verify`.
[Network Load Balancers] The possible values are `off` and `verify`.
Type: String
Required: No

 ** TrustStoreArn **
The Amazon Resource Name (ARN) of the trust store.
Type: String
Required: No

 ** TrustStoreAssociationStatus **
Indicates a shared trust stores association status.
Type: String
Valid Values: `active | removed`
Required: No

## See Also
<a name="API_MutualAuthenticationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/MutualAuthenticationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/MutualAuthenticationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/MutualAuthenticationAttributes)
