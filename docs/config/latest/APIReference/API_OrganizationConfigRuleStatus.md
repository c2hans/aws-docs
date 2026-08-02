---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConfigRuleStatus.html
---

# OrganizationConfigRuleStatus
<a name="API_OrganizationConfigRuleStatus"></a>

Returns the status for an organization AWS Config rule in an organization.

## Contents
<a name="API_OrganizationConfigRuleStatus_Contents"></a>

 ** OrganizationConfigRuleName **   <a name="config-Type-OrganizationConfigRuleStatus-OrganizationConfigRuleName"></a>
The name that you assign to organization AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

 ** OrganizationRuleStatus **   <a name="config-Type-OrganizationConfigRuleStatus-OrganizationRuleStatus"></a>
Indicates deployment status of an organization AWS Config rule. When management account calls PutOrganizationConfigRule action for the first time, AWS Config rule status is created in all the member accounts. When management account calls PutOrganizationConfigRule action for the second time, AWS Config rule status is updated in all the member accounts. Additionally, AWS Config rule status is updated when one or more member accounts join or leave an organization. AWS Config rule status is deleted when the management account deletes OrganizationConfigRule in all the member accounts and disables service access for `config-multiaccountsetup.amazonaws.com`.
 AWS Config sets the state of the rule to:
+  `CREATE_SUCCESSFUL` when an organization AWS Config rule has been successfully created in all the member accounts.
+  `CREATE_IN_PROGRESS` when an organization AWS Config rule creation is in progress.
+  `CREATE_FAILED` when an organization AWS Config rule creation failed in one or more member accounts within that organization.
+  `DELETE_FAILED` when an organization AWS Config rule deletion failed in one or more member accounts within that organization.
+  `DELETE_IN_PROGRESS` when an organization AWS Config rule deletion is in progress.
+  `DELETE_SUCCESSFUL` when an organization AWS Config rule has been successfully deleted from all the member accounts.
+  `UPDATE_SUCCESSFUL` when an organization AWS Config rule has been successfully updated in all the member accounts.
+  `UPDATE_IN_PROGRESS` when an organization AWS Config rule update is in progress.
+  `UPDATE_FAILED` when an organization AWS Config rule update failed in one or more member accounts within that organization.
Type: String
Valid Values: `CREATE_SUCCESSFUL | CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_SUCCESSFUL | DELETE_FAILED | DELETE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: Yes

 ** ErrorCode **   <a name="config-Type-OrganizationConfigRuleStatus-ErrorCode"></a>
An error code that is returned when organization AWS Config rule creation or deletion has failed.
Type: String
Required: No

 ** ErrorMessage **   <a name="config-Type-OrganizationConfigRuleStatus-ErrorMessage"></a>
An error message indicating that organization AWS Config rule creation or deletion failed due to an error.
Type: String
Required: No

 ** LastUpdateTime **   <a name="config-Type-OrganizationConfigRuleStatus-LastUpdateTime"></a>
The timestamp of the last update.
Type: Timestamp
Required: No

## See Also
<a name="API_OrganizationConfigRuleStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationConfigRuleStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationConfigRuleStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationConfigRuleStatus)
