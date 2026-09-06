---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyFlagsV3.html
---

# PrivateKeyFlagsV3
<a name="API_PrivateKeyFlagsV3"></a>

Private key flags for v3 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, and if an alternate signature algorithm should be used.

## Contents
<a name="API_PrivateKeyFlagsV3_Contents"></a>

 ** ClientVersion **   <a name="PcaConnectorAd-Type-PrivateKeyFlagsV3-ClientVersion"></a>
Defines the minimum client compatibility.
Type: String
Valid Values: `WINDOWS_SERVER_2008 | WINDOWS_SERVER_2008_R2 | WINDOWS_SERVER_2012 | WINDOWS_SERVER_2012_R2 | WINDOWS_SERVER_2016`
Required: Yes

 ** ExportableKey **   <a name="PcaConnectorAd-Type-PrivateKeyFlagsV3-ExportableKey"></a>
Allows the private key to be exported.
Type: Boolean
Required: No

 ** RequireAlternateSignatureAlgorithm **   <a name="PcaConnectorAd-Type-PrivateKeyFlagsV3-RequireAlternateSignatureAlgorithm"></a>
Reguires the PKCS \#1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.
Type: Boolean
Required: No

 ** StrongKeyProtectionRequired **   <a name="PcaConnectorAd-Type-PrivateKeyFlagsV3-StrongKeyProtectionRequired"></a>
Requirer user input when using the private key for enrollment.
Type: Boolean
Required: No

## See Also
<a name="API_PrivateKeyFlagsV3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/PrivateKeyFlagsV3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/PrivateKeyFlagsV3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/PrivateKeyFlagsV3)
