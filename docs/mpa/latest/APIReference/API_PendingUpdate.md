---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_PendingUpdate.html
---

# PendingUpdate
<a name="API_PendingUpdate"></a>

Contains details for the pending updates for an approval team, if applicable.

## Contents
<a name="API_PendingUpdate_Contents"></a>

 ** ApprovalStrategy **   <a name="mpa-Type-PendingUpdate-ApprovalStrategy"></a>
An `ApprovalStrategyResponse` object. Contains details for how the team grants approval.
Type: [ApprovalStrategyResponse](API_ApprovalStrategyResponse.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Approvers **   <a name="mpa-Type-PendingUpdate-Approvers"></a>
An array of `GetApprovalTeamResponseApprover ` objects. Contains details for the approvers in the team.
Type: Array of [GetApprovalTeamResponseApprover](API_GetApprovalTeamResponseApprover.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** Description **   <a name="mpa-Type-PendingUpdate-Description"></a>
Description for the team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** NumberOfApprovers **   <a name="mpa-Type-PendingUpdate-NumberOfApprovers"></a>
Total number of approvers in the team.
Type: Integer
Required: No

 ** Status **   <a name="mpa-Type-PendingUpdate-Status"></a>
Status for the team. For more information, see [Team health](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html) in the *Multi-party approval User Guide*.
Type: String
Valid Values: `ACTIVE | INACTIVE | DELETING | PENDING`
Required: No

 ** StatusCode **   <a name="mpa-Type-PendingUpdate-StatusCode"></a>
Status code for the update. For more information, see [Team health](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html) in the *Multi-party approval User Guide*.
Type: String
Valid Values: `VALIDATING | PENDING_ACTIVATION | FAILED_VALIDATION | FAILED_ACTIVATION | UPDATE_PENDING_APPROVAL | UPDATE_PENDING_ACTIVATION | UPDATE_FAILED_APPROVAL | UPDATE_FAILED_ACTIVATION | UPDATE_FAILED_VALIDATION | DELETE_PENDING_APPROVAL | DELETE_FAILED_APPROVAL | DELETE_FAILED_VALIDATION`
Required: No

 ** StatusMessage **   <a name="mpa-Type-PendingUpdate-StatusMessage"></a>
Message describing the status for the team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** UpdateInitiationTime **   <a name="mpa-Type-PendingUpdate-UpdateInitiationTime"></a>
Timestamp when the update request was initiated.
Type: Timestamp
Required: No

 ** VersionId **   <a name="mpa-Type-PendingUpdate-VersionId"></a>
Version ID for the team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_PendingUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/PendingUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/PendingUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/PendingUpdate)
