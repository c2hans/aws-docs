---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_StatusDetailFilters.html
---

# StatusDetailFilters
<a name="API_StatusDetailFilters"></a>

Status filter object to filter results based on specific member account ID or status type for an organization AWS Config rule.

## Contents
<a name="API_StatusDetailFilters_Contents"></a>

 ** AccountId **   <a name="config-Type-StatusDetailFilters-AccountId"></a>
The 12-digit account ID of the member account within an organization.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** MemberAccountRuleStatus **   <a name="config-Type-StatusDetailFilters-MemberAccountRuleStatus"></a>
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
Required: No

## See Also
<a name="API_StatusDetailFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/StatusDetailFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/StatusDetailFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/StatusDetailFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
