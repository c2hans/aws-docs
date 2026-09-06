---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConformancePackStatus.html
---

# OrganizationConformancePackStatus
<a name="API_OrganizationConformancePackStatus"></a>

Returns the status for an organization conformance pack in an organization.

## Contents
<a name="API_OrganizationConformancePackStatus_Contents"></a>

 ** OrganizationConformancePackName **   <a name="config-Type-OrganizationConformancePackStatus-OrganizationConformancePackName"></a>
The name that you assign to organization conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

 ** Status **   <a name="config-Type-OrganizationConformancePackStatus-Status"></a>
Indicates deployment status of an organization conformance pack. When management account calls PutOrganizationConformancePack for the first time, conformance pack status is created in all the member accounts. When management account calls PutOrganizationConformancePack for the second time, conformance pack status is updated in all the member accounts. Additionally, conformance pack status is updated when one or more member accounts join or leave an organization. Conformance pack status is deleted when the management account deletes OrganizationConformancePack in all the member accounts and disables service access for `config-multiaccountsetup.amazonaws.com`.
 AWS Config sets the state of the conformance pack to:
+  `CREATE_SUCCESSFUL` when an organization conformance pack has been successfully created in all the member accounts.
+  `CREATE_IN_PROGRESS` when an organization conformance pack creation is in progress.
+  `CREATE_FAILED` when an organization conformance pack creation failed in one or more member accounts within that organization.
+  `DELETE_FAILED` when an organization conformance pack deletion failed in one or more member accounts within that organization.
+  `DELETE_IN_PROGRESS` when an organization conformance pack deletion is in progress.
+  `DELETE_SUCCESSFUL` when an organization conformance pack has been successfully deleted from all the member accounts.
+  `UPDATE_SUCCESSFUL` when an organization conformance pack has been successfully updated in all the member accounts.
+  `UPDATE_IN_PROGRESS` when an organization conformance pack update is in progress.
+  `UPDATE_FAILED` when an organization conformance pack update failed in one or more member accounts within that organization.
Type: String
Valid Values: `CREATE_SUCCESSFUL | CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_SUCCESSFUL | DELETE_FAILED | DELETE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: Yes

 ** ErrorCode **   <a name="config-Type-OrganizationConformancePackStatus-ErrorCode"></a>
An error code that is returned when organization conformance pack creation or deletion has failed in a member account.
Type: String
Required: No

 ** ErrorMessage **   <a name="config-Type-OrganizationConformancePackStatus-ErrorMessage"></a>
An error message indicating that organization conformance pack creation or deletion failed due to an error.
Type: String
Required: No

 ** LastUpdateTime **   <a name="config-Type-OrganizationConformancePackStatus-LastUpdateTime"></a>
The timestamp of the last update.
Type: Timestamp
Required: No

## See Also
<a name="API_OrganizationConformancePackStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationConformancePackStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationConformancePackStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationConformancePackStatus)
