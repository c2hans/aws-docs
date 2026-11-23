---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_OrganizationScope.html
---

# OrganizationScope

 Defines the scope for organization-level rules when previewing matching actions.

## Contents
<a name="API_automation_OrganizationScope_Contents"></a>

 ** accountIds **   <a name="computeoptimizer-Type-automation_OrganizationScope-accountIds"></a>
List of AWS account IDs to include in the organization scope.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `[0-9]{12}`
Required: No

 ** excludedAccountIds **   <a name="computeoptimizer-Type-automation_OrganizationScope-excludedAccountIds"></a>
The AWS account IDs to exclude from the preview scope.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `[0-9]{12}`
Required: No

 ** excludedOrganizationalUnitIds **   <a name="computeoptimizer-Type-automation_OrganizationScope-excludedOrganizationalUnitIds"></a>
The organizational unit (OU) or organization root IDs to exclude from the preview scope. The preview doesn't include accounts in the specified OUs or their child OUs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 150 items.
Length Constraints: Minimum length of 1. Maximum length of 68.
Pattern: `(r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

 ** organizationalUnitIds **   <a name="computeoptimizer-Type-automation_OrganizationScope-organizationalUnitIds"></a>
The organizational unit (OU) or organization root IDs to include in the preview scope. The preview includes accounts in the specified OUs and their child OUs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 150 items.
Length Constraints: Minimum length of 1. Maximum length of 68.
Pattern: `(r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

## See Also
<a name="API_automation_OrganizationScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/OrganizationScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/OrganizationScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/OrganizationScope)
