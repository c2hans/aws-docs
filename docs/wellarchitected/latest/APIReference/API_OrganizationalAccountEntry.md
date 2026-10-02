---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_OrganizationalAccountEntry.html
---

# OrganizationalAccountEntry
<a name="API_OrganizationalAccountEntry"></a>

**Important**
This is not available during the preview release.

An individual account entry in the organizational monitoring boundary, with its associated regions.

## Contents
<a name="API_OrganizationalAccountEntry_Contents"></a>

 ** accountId **   <a name="wellarchitected-Type-OrganizationalAccountEntry-accountId"></a>
The AWS account ID to include in the monitoring boundary.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** regions **   <a name="wellarchitected-Type-OrganizationalAccountEntry-regions"></a>
The list of regions to monitor for this account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-z]{2}-[a-z]+-\d{1}`
Required: Yes

## See Also
<a name="API_OrganizationalAccountEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/OrganizationalAccountEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/OrganizationalAccountEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/OrganizationalAccountEntry)
