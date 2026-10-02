---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_OrganizationalAggregationConfiguration.html
---

# OrganizationalAggregationConfiguration
<a name="API_OrganizationalAggregationConfiguration"></a>

**Important**
This is not available during the preview release.

The organizational monitoring boundary configuration. Contains organizational unit entries and individual account entries, each with their own region selections, that define the scope for organizational profile analysis.

## Contents
<a name="API_OrganizationalAggregationConfiguration_Contents"></a>

 ** accounts **   <a name="wellarchitected-Type-OrganizationalAggregationConfiguration-accounts"></a>
A list of individual account entries that define additional accounts to include. Each entry specifies an account ID and the regions to monitor within it.
Type: Array of [OrganizationalAccountEntry](API_OrganizationalAccountEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2500 items.
Required: No

 ** organizationalUnits **   <a name="wellarchitected-Type-OrganizationalAggregationConfiguration-organizationalUnits"></a>
A list of organizational unit or root entries that define the organizational scope. Each entry specifies an OU or root ID and the regions to monitor within it.
Type: Array of [OrganizationalUnitEntry](API_OrganizationalUnitEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2500 items.
Required: No

## See Also
<a name="API_OrganizationalAggregationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/OrganizationalAggregationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/OrganizationalAggregationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/OrganizationalAggregationConfiguration)
