---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_OrganizationalUnitEntry.html
---

# OrganizationalUnitEntry
<a name="API_OrganizationalUnitEntry"></a>

**Important**
This is not available during the preview release.

An organizational unit or root entry in the organizational monitoring boundary, with its associated regions.

## Contents
<a name="API_OrganizationalUnitEntry_Contents"></a>

 ** organizationalUnitId **   <a name="wellarchitected-Type-OrganizationalUnitEntry-organizationalUnitId"></a>
The AWS Organizations organizational unit ID or root ID. Must match the pattern `r-[a-z0-9]{4,32}` for roots or `ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}` for OUs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 68.
Pattern: `(r-[a-z0-9]{4,32}|ou-[a-z0-9]{4,32}-[a-z0-9]{8,32})`
Required: Yes

 ** regions **   <a name="wellarchitected-Type-OrganizationalUnitEntry-regions"></a>
The list of regions to monitor for this organizational unit or root.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-z]{2}-[a-z]+-\d{1}`
Required: Yes

## See Also
<a name="API_OrganizationalUnitEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/OrganizationalUnitEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/OrganizationalUnitEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/OrganizationalUnitEntry)
