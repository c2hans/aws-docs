---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationResourceDetailedStatusFilters.html
---

# OrganizationResourceDetailedStatusFilters
<a name="API_OrganizationResourceDetailedStatusFilters"></a>

Status filter object to filter results based on specific member account ID or status type for an organization conformance pack.

## Contents
<a name="API_OrganizationResourceDetailedStatusFilters_Contents"></a>

 ** AccountId **   <a name="config-Type-OrganizationResourceDetailedStatusFilters-AccountId"></a>
The 12-digit account ID of the member account within an organization.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** Status **   <a name="config-Type-OrganizationResourceDetailedStatusFilters-Status"></a>
Indicates deployment status for conformance pack in a member account. When management account calls `PutOrganizationConformancePack` action for the first time, conformance pack status is created in the member account. When management account calls `PutOrganizationConformancePack` action for the second time, conformance pack status is updated in the member account. Conformance pack status is deleted when the management account deletes `OrganizationConformancePack` and disables service access for `config-multiaccountsetup.amazonaws.com`.
 AWS Config sets the state of the conformance pack to:
+  `CREATE_SUCCESSFUL` when conformance pack has been created in the member account.
+  `CREATE_IN_PROGRESS` when conformance pack is being created in the member account.
+  `CREATE_FAILED` when conformance pack creation has failed in the member account.
+  `DELETE_FAILED` when conformance pack deletion has failed in the member account.
+  `DELETE_IN_PROGRESS` when conformance pack is being deleted in the member account.
+  `DELETE_SUCCESSFUL` when conformance pack has been deleted in the member account.
+  `UPDATE_SUCCESSFUL` when conformance pack has been updated in the member account.
+  `UPDATE_IN_PROGRESS` when conformance pack is being updated in the member account.
+  `UPDATE_FAILED` when conformance pack deletion has failed in the member account.
Type: String
Valid Values: `CREATE_SUCCESSFUL | CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_SUCCESSFUL | DELETE_FAILED | DELETE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: No

## See Also
<a name="API_OrganizationResourceDetailedStatusFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationResourceDetailedStatusFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationResourceDetailedStatusFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationResourceDetailedStatusFilters)
