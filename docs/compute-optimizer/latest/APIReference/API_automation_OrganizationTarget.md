---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_OrganizationTarget.html
---

# OrganizationTarget

An account, organizational unit (OU), or organization root to which an organization enrollment configuration applies. The management account can't be specified as an account target.

## Contents
<a name="API_automation_OrganizationTarget_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accountId **   <a name="computeoptimizer-Type-automation_OrganizationTarget-accountId"></a>
The ID of the member account to target. You can't specify the management account.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** organizationalUnitId **   <a name="computeoptimizer-Type-automation_OrganizationTarget-organizationalUnitId"></a>
The ID of the organizational unit (OU) or organization root to target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 68.
Pattern: `(r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

## See Also
<a name="API_automation_OrganizationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/OrganizationTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/OrganizationTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/OrganizationTarget)
