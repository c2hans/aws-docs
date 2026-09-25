---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_OrganizationalUnitReference.html
---

# OrganizationalUnitReference
<a name="API_OrganizationalUnitReference"></a>

A reference to an AWS Organizations organizational unit (OU), with optional display metadata.

## Contents
<a name="API_OrganizationalUnitReference_Contents"></a>

 ** ouId **   <a name="networksecuritymanager-Type-OrganizationalUnitReference-ouId"></a>
The ID of the AWS Organizations organizational unit (OU).
Type: String
Length Constraints: Minimum length of 16. Maximum length of 68.
Pattern: `(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: Yes

 ** name **   <a name="networksecuritymanager-Type-OrganizationalUnitReference-name"></a>
The display name of the organizational unit.
Type: String
Required: No

## See Also
<a name="API_OrganizationalUnitReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/OrganizationalUnitReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/OrganizationalUnitReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/OrganizationalUnitReference)
