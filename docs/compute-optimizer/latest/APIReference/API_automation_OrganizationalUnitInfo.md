---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_OrganizationalUnitInfo.html
---

# OrganizationalUnitInfo

Information about an organizational unit (OU) or the organization root, including whether an applicable organization enrollment configuration enables Automation for member accounts and the effective organization rule mode.

## Contents
<a name="API_automation_OrganizationalUnitInfo_Contents"></a>

 ** autoEnrollMemberAccounts **   <a name="computeoptimizer-Type-automation_OrganizationalUnitInfo-autoEnrollMemberAccounts"></a>
Whether an applicable organization enrollment configuration enables Automation for eligible member accounts beneath the organizational unit (OU) or organization root.
+  `All` - An organization enrollment configuration applies and enables Automation for affected member accounts, including accounts that join later. This value applies to configurations with either `AnyAllowed` or `NoneAllowed`.
+  `None` - No organization enrollment configuration applies, so Automation isn't enabled by an organization enrollment configuration.
Type: String
Valid Values: `All | None`
Required: Yes

 ** organizationalUnitId **   <a name="computeoptimizer-Type-automation_OrganizationalUnitInfo-organizationalUnitId"></a>
The ID of the organizational unit (OU) or organization root.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 68.
Pattern: `(r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: Yes

 ** organizationRuleMode **   <a name="computeoptimizer-Type-automation_OrganizationalUnitInfo-organizationRuleMode"></a>
The effective organization rule mode for the organizational unit or organization root.
Type: String
Valid Values: `AnyAllowed | NoneAllowed`
Required: Yes

 ** organizationRuleModeSource **   <a name="computeoptimizer-Type-automation_OrganizationalUnitInfo-organizationRuleModeSource"></a>
Information about the source of the effective organization rule mode.
Type: [OrganizationRuleModeSource](API_automation_OrganizationRuleModeSource.md) object
Required: Yes

## See Also
<a name="API_automation_OrganizationalUnitInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/OrganizationalUnitInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/OrganizationalUnitInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/OrganizationalUnitInfo)
