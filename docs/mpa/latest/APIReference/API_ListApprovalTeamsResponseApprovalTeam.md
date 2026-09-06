---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListApprovalTeamsResponseApprovalTeam.html
---

# ListApprovalTeamsResponseApprovalTeam
<a name="API_ListApprovalTeamsResponseApprovalTeam"></a>

Contains details for an approval team

## Contents
<a name="API_ListApprovalTeamsResponseApprovalTeam_Contents"></a>

 ** ApprovalStrategy **   <a name="mpa-Type-ListApprovalTeamsResponseApprovalTeam-ApprovalStrategy"></a>
An `ApprovalStrategyResponse` object. Contains details for how an approval team grants approval.
Type: [ApprovalStrategyResponse](API_ApprovalStrategyResponse.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Arn **   <a name="mpa-Type-ListApprovalTeamsResponseApprovalTeam-Arn"></a>
Amazon Resource Name (ARN) for the team.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`
Required: No

 ** CreationTime **   <a name="mpa-Type-ListApprovalTeamsResponseApprovalTeam-CreationTime"></a>
Timestamp when the team was created.
Type: Timestamp
Required: No

 ** Description **   <a name="mpa-Type-ListApprovalTeamsResponseApprovalTeam-Description"></a>
Description for the team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Name **   <a name="mpa-Type-ListApprovalTeamsResponseApprovalTeam-Name"></a>
Name of the team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9._-]+`
Required: No

 ** NumberOfApprovers **   <a name="mpa-Type-ListApprovalTeamsResponseApprovalTeam-NumberOfApprovers"></a>
Total number of approvers in the team.
Type: Integer
Required: No

 ** Status **   <a name="mpa-Type-ListApprovalTeamsResponseApprovalTeam-Status"></a>
Status for the team. For more information, see [Team health](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html) in the *Multi-party approval User Guide*.
Type: String
Valid Values: `ACTIVE | INACTIVE | DELETING | PENDING`
Required: No

 ** StatusCode **   <a name="mpa-Type-ListApprovalTeamsResponseApprovalTeam-StatusCode"></a>
Status code for the team. For more information, see [Team health](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html) in the *Multi-party approval User Guide*.
Type: String
Valid Values: `VALIDATING | PENDING_ACTIVATION | FAILED_VALIDATION | FAILED_ACTIVATION | UPDATE_PENDING_APPROVAL | UPDATE_PENDING_ACTIVATION | UPDATE_FAILED_APPROVAL | UPDATE_FAILED_ACTIVATION | UPDATE_FAILED_VALIDATION | DELETE_PENDING_APPROVAL | DELETE_FAILED_APPROVAL | DELETE_FAILED_VALIDATION`
Required: No

 ** StatusMessage **   <a name="mpa-Type-ListApprovalTeamsResponseApprovalTeam-StatusMessage"></a>
Message describing the status for the team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## See Also
<a name="API_ListApprovalTeamsResponseApprovalTeam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/ListApprovalTeamsResponseApprovalTeam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/ListApprovalTeamsResponseApprovalTeam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/ListApprovalTeamsResponseApprovalTeam)
