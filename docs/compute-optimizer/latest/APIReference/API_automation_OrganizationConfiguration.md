---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_OrganizationConfiguration.html
---

# OrganizationConfiguration
<a name="API_automation_OrganizationConfiguration"></a>

Configuration settings for organization-wide automation rules.

## Contents
<a name="API_automation_OrganizationConfiguration_Contents"></a>

 ** accountIds **   <a name="computeoptimizer-Type-automation_OrganizationConfiguration-accountIds"></a>
List of specific AWS account IDs where the organization rule should be applied.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `[0-9]{12}`
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
