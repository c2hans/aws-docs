---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyAttributesV2.html
---

# PrivateKeyAttributesV2
<a name="API_PrivateKeyAttributesV2"></a>

Defines the attributes of the private key.

## Contents
<a name="API_PrivateKeyAttributesV2_Contents"></a>

 ** KeySpec **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV2-KeySpec"></a>
Defines the purpose of the private key. Set it to "KEY\_EXCHANGE" or "SIGNATURE" value.
Type: String
Valid Values: `KEY_EXCHANGE | SIGNATURE`
Required: Yes

 ** MinimalKeyLength **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV2-MinimalKeyLength"></a>
Set the minimum key length of the private key.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** CryptoProviders **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV2-CryptoProviders"></a>
Defines the cryptographic providers used to generate the private key.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_PrivateKeyAttributesV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/PrivateKeyAttributesV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/PrivateKeyAttributesV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/PrivateKeyAttributesV2)
