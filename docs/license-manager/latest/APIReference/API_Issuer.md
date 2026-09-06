---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_Issuer.html
---

# Issuer
<a name="API_Issuer"></a>

Details about the issuer of a license.

## Contents
<a name="API_Issuer_Contents"></a>

 ** Name **   <a name="licensemanager-Type-Issuer-Name"></a>
Issuer name.
Type: String
Required: Yes

 ** SignKey **   <a name="licensemanager-Type-Issuer-SignKey"></a>
Asymmetric KMS key from AWS Key Management Service. The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.
Type: String
Required: No

## See Also
<a name="API_Issuer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/Issuer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/Issuer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/Issuer)
