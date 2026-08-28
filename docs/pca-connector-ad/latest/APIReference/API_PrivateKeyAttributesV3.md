---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyAttributesV3.html
---

# PrivateKeyAttributesV3
<a name="API_PrivateKeyAttributesV3"></a>

Defines the attributes of the private key.

## Contents
<a name="API_PrivateKeyAttributesV3_Contents"></a>

 ** Algorithm **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV3-Algorithm"></a>
Defines the algorithm used to generate the private key.
Type: String
Valid Values: `RSA | ECDH_P256 | ECDH_P384 | ECDH_P521`
Required: Yes

 ** KeySpec **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV3-KeySpec"></a>
Defines the purpose of the private key. Set it to "KEY\_EXCHANGE" or "SIGNATURE" value.
Type: String
Valid Values: `KEY_EXCHANGE | SIGNATURE`
Required: Yes

 ** KeyUsageProperty **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV3-KeyUsageProperty"></a>
The key usage property defines the purpose of the private key contained in the certificate. You can specify specific purposes using property flags or all by using property type ALL.
Type: [KeyUsageProperty](API_KeyUsageProperty.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** MinimalKeyLength **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV3-MinimalKeyLength"></a>
Set the minimum key length of the private key.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** CryptoProviders **   <a name="PcaConnectorAd-Type-PrivateKeyAttributesV3-CryptoProviders"></a>
Defines the cryptographic providers used to generate the private key.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_PrivateKeyAttributesV3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/PrivateKeyAttributesV3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/PrivateKeyAttributesV3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/PrivateKeyAttributesV3)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
