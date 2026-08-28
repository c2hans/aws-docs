---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_PrivateKeyFlagsV4.html
---

# PrivateKeyFlagsV4
<a name="API_PrivateKeyFlagsV4"></a>

Private key flags for v4 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, if an alternate signature algorithm should be used, and if certificates are renewed using the same private key.

## Contents
<a name="API_PrivateKeyFlagsV4_Contents"></a>

 ** ClientVersion **   <a name="PcaConnectorAd-Type-PrivateKeyFlagsV4-ClientVersion"></a>
Defines the minimum client compatibility.
Type: String
Valid Values: `WINDOWS_SERVER_2012 | WINDOWS_SERVER_2012_R2 | WINDOWS_SERVER_2016`
Required: Yes

 ** ExportableKey **   <a name="PcaConnectorAd-Type-PrivateKeyFlagsV4-ExportableKey"></a>
Allows the private key to be exported.
Type: Boolean
Required: No

 ** RequireAlternateSignatureAlgorithm **   <a name="PcaConnectorAd-Type-PrivateKeyFlagsV4-RequireAlternateSignatureAlgorithm"></a>
Requires the PKCS \#1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.
Type: Boolean
Required: No

 ** RequireSameKeyRenewal **   <a name="PcaConnectorAd-Type-PrivateKeyFlagsV4-RequireSameKeyRenewal"></a>
Renew certificate using the same private key.
Type: Boolean
Required: No

 ** StrongKeyProtectionRequired **   <a name="PcaConnectorAd-Type-PrivateKeyFlagsV4-StrongKeyProtectionRequired"></a>
Require user input when using the private key for enrollment.
Type: Boolean
Required: No

 ** UseLegacyProvider **   <a name="PcaConnectorAd-Type-PrivateKeyFlagsV4-UseLegacyProvider"></a>
Specifies the cryptographic service provider category used to generate private keys. Set to TRUE to use Legacy Cryptographic Service Providers and FALSE to use Key Storage Providers.
Type: Boolean
Required: No

## See Also
<a name="API_PrivateKeyFlagsV4_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/PrivateKeyFlagsV4)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/PrivateKeyFlagsV4)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/PrivateKeyFlagsV4)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
