---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_OrganizationConfiguration.html
---

# OrganizationConfiguration

Configuration settings that define the scope of an organization-wide automation rule. Each organizational unit (OU) list can contain up to 150 OUs or organization roots, and each account list can contain up to 50 accounts. Each included OU or organization root must have an effective organization rule mode of `AnyAllowed`. Exclusions take precedence over inclusions. An account that is in an included OU and is also excluded is excluded. The rule doesn't apply to the management account when the account is reached through an OU or the organization root.

## Contents
<a name="API_automation_OrganizationConfiguration_Contents"></a>

 ** accountIds **   <a name="computeoptimizer-Type-automation_OrganizationConfiguration-accountIds"></a>
The specific AWS account IDs where the organization rule should be applied. You can specify up to 50 account IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `[0-9]{12}`
Required: No

 ** excludedAccountIds **   <a name="computeoptimizer-Type-automation_OrganizationConfiguration-excludedAccountIds"></a>
The AWS account IDs to exclude from the organization rule scope. You can specify up to 50 account IDs. An excluded account remains excluded even if it is in an included OU.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `[0-9]{12}`
Required: No

 ** excludedOrganizationalUnitIds **   <a name="computeoptimizer-Type-automation_OrganizationConfiguration-excludedOrganizationalUnitIds"></a>
The organizational unit (OU) or organization root IDs to exclude from the organization rule scope. The rule doesn't apply to accounts in the specified OUs or their child OUs. You can specify up to 150 IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 150 items.
Length Constraints: Minimum length of 1. Maximum length of 68.
Pattern: `(r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

 ** organizationalUnitIds **   <a name="computeoptimizer-Type-automation_OrganizationConfiguration-organizationalUnitIds"></a>
The organizational unit (OU) or organization root IDs to include in the organization rule scope. The rule applies to accounts in the specified OUs and their child OUs. You can specify up to 150 IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 150 items.
Length Constraints: Minimum length of 1. Maximum length of 68.
Pattern: `(r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

 ** ruleApplyOrder **   <a name="computeoptimizer-Type-automation_OrganizationConfiguration-ruleApplyOrder"></a>
Specifies when organization rules should be applied relative to account rules.
Type: String
Valid Values: `BeforeAccountRules | AfterAccountRules`
Required: No

## See Also
<a name="API_automation_OrganizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/OrganizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/OrganizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/OrganizationConfiguration)
