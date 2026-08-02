---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyAttributesV4.html
---

# PrivateKeyAttributesV4
<a name="API_PrivateKeyAttributesV4"></a>

Defines the attributes of the private key.

## Contents
<a name="API_PrivateKeyAttributesV4_Contents"></a>

 ** KeySpec **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV4-KeySpec"></a>
Defines the purpose of the private key. Set it to "KEY\_EXCHANGE" or "SIGNATURE" value.
Type: String
Valid Values: `KEY_EXCHANGE | SIGNATURE`
Required: Yes

 ** MinimalKeyLength **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV4-MinimalKeyLength"></a>
Set the minimum key length of the private key.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** Algorithm **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV4-Algorithm"></a>
Defines the algorithm used to generate the private key.
Type: String
Valid Values: `RSA | ECDH_P256 | ECDH_P384 | ECDH_P521`
Required: No

 ** CryptoProviders **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV4-CryptoProviders"></a>
Defines the cryptographic providers used to generate the private key.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** KeyUsageProperty **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV4-KeyUsageProperty"></a>
The key usage property defines the purpose of the private key contained in the certificate. You can specify specific purposes using property flags or all by using property type ALL.
Type: [KeyUsageProperty](API_KeyUsageProperty.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_PrivateKeyAttributesV4_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/PrivateKeyAttributesV4)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/PrivateKeyAttributesV4)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/PrivateKeyAttributesV4)
