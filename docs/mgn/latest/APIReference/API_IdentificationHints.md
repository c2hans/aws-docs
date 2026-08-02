---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_IdentificationHints.html
---

# IdentificationHints
<a name="API_IdentificationHints"></a>

Identification hints.

## Contents
<a name="API_IdentificationHints_Contents"></a>

 ** awsInstanceID **   <a name="mgn-Type-IdentificationHints-awsInstanceID"></a>
AWS Instance ID identification hint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

 ** fqdn **   <a name="mgn-Type-IdentificationHints-fqdn"></a>
FQDN address identification hint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** hostname **   <a name="mgn-Type-IdentificationHints-hostname"></a>
Hostname identification hint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** vmPath **   <a name="mgn-Type-IdentificationHints-vmPath"></a>
vCenter VM path identification hint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** vmWareUuid **   <a name="mgn-Type-IdentificationHints-vmWareUuid"></a>
vmWare UUID identification hint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_IdentificationHints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/IdentificationHints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/IdentificationHints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/IdentificationHints)
