---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_MemberAccountStatus.html
---

# MemberAccountStatus
<a name="API_MemberAccountStatus"></a>

Organization AWS Config rule creation or deletion status in each member account. This includes the name of the rule, the status, error code and error message when the rule creation or deletion failed.

## Contents
<a name="API_MemberAccountStatus_Contents"></a>

 ** AccountId **   <a name="config-Type-MemberAccountStatus-AccountId"></a>
The 12-digit account ID of a member account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** ConfigRuleName **   <a name="config-Type-MemberAccountStatus-ConfigRuleName"></a>
The name of AWS Config rule deployed in the member account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** MemberAccountRuleStatus **   <a name="config-Type-MemberAccountStatus-MemberAccountRuleStatus"></a>
Indicates deployment status for AWS Config rule in the member account. When management account calls `PutOrganizationConfigRule` action for the first time, AWS Config rule status is created in the member account. When management account calls `PutOrganizationConfigRule` action for the second time, AWS Config rule status is updated in the member account. AWS Config rule status is deleted when the management account deletes `OrganizationConfigRule` and disables service access for `config-multiaccountsetup.amazonaws.com`.
 AWS Config sets the state of the rule to:
+  `CREATE_SUCCESSFUL` when AWS Config rule has been created in the member account.
+  `CREATE_IN_PROGRESS` when AWS Config rule is being created in the member account.
+  `CREATE_FAILED` when AWS Config rule creation has failed in the member account.
+  `DELETE_FAILED` when AWS Config rule deletion has failed in the member account.
+  `DELETE_IN_PROGRESS` when AWS Config rule is being deleted in the member account.
+  `DELETE_SUCCESSFUL` when AWS Config rule has been deleted in the member account.
+  `UPDATE_SUCCESSFUL` when AWS Config rule has been updated in the member account.
+  `UPDATE_IN_PROGRESS` when AWS Config rule is being updated in the member account.
+  `UPDATE_FAILED` when AWS Config rule deletion has failed in the member account.
Type: String
Valid Values: `CREATE_SUCCESSFUL | CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_SUCCESSFUL | DELETE_FAILED | DELETE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: Yes

 ** ErrorCode **   <a name="config-Type-MemberAccountStatus-ErrorCode"></a>
An error code that is returned when AWS Config rule creation or deletion failed in the member account.
Type: String
Required: No

 ** ErrorMessage **   <a name="config-Type-MemberAccountStatus-ErrorMessage"></a>
An error message indicating that AWS Config rule account creation or deletion has failed due to an error in the member account.
Type: String
Required: No

 ** LastUpdateTime **   <a name="config-Type-MemberAccountStatus-LastUpdateTime"></a>
The timestamp of the last status update.
Type: Timestamp
Required: No

## See Also
<a name="API_MemberAccountStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/MemberAccountStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/MemberAccountStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/MemberAccountStatus)
