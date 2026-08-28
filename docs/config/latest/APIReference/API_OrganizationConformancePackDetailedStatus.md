---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConformancePackDetailedStatus.html
---

# OrganizationConformancePackDetailedStatus
<a name="API_OrganizationConformancePackDetailedStatus"></a>

Organization conformance pack creation or deletion status in each member account. This includes the name of the conformance pack, the status, error code and error message when the conformance pack creation or deletion failed.

## Contents
<a name="API_OrganizationConformancePackDetailedStatus_Contents"></a>

 ** AccountId **   <a name="config-Type-OrganizationConformancePackDetailedStatus-AccountId"></a>
The 12-digit account ID of a member account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** ConformancePackName **   <a name="config-Type-OrganizationConformancePackDetailedStatus-ConformancePackName"></a>
The name of conformance pack deployed in the member account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Status **   <a name="config-Type-OrganizationConformancePackDetailedStatus-Status"></a>
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
Required: Yes

 ** ErrorCode **   <a name="config-Type-OrganizationConformancePackDetailedStatus-ErrorCode"></a>
An error code that is returned when conformance pack creation or deletion failed in the member account.
Type: String
Required: No

 ** ErrorMessage **   <a name="config-Type-OrganizationConformancePackDetailedStatus-ErrorMessage"></a>
An error message indicating that conformance pack account creation or deletion has failed due to an error in the member account.
Type: String
Required: No

 ** LastUpdateTime **   <a name="config-Type-OrganizationConformancePackDetailedStatus-LastUpdateTime"></a>
The timestamp of the last status update.
Type: Timestamp
Required: No

## See Also
<a name="API_OrganizationConformancePackDetailedStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationConformancePackDetailedStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationConformancePackDetailedStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationConformancePackDetailedStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
