---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_OrganizationRuleModeSource.html
---

# OrganizationRuleModeSource

Information about the source of an effective organization rule mode.

## Contents
<a name="API_automation_OrganizationRuleModeSource_Contents"></a>

 ** sourceType **   <a name="computeoptimizer-Type-automation_OrganizationRuleModeSource-sourceType"></a>
How the effective organization rule mode is supplied.
+  `Applied` - An organization enrollment configuration is on this organizational unit or account.
+  `Inherited` - The organization enrollment configuration is on the parent organizational unit or root.
+  `Direct` - The organization rule mode is set on the account itself, with no organization enrollment configuration applied.
+  `Default` - No organization enrollment configuration applies, so the organization rule mode is None allowed.
Type: String
Valid Values: `Applied | Inherited | Direct | Default`
Required: Yes

 ** sourceTargetId **   <a name="computeoptimizer-Type-automation_OrganizationRuleModeSource-sourceTargetId"></a>
The ID of the account, organizational unit (OU), or organization root that has the organization enrollment configuration. This field is omitted when `sourceType` is `Direct` or `Default`.
Type: String
Required: No

## See Also
<a name="API_automation_OrganizationRuleModeSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/OrganizationRuleModeSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/OrganizationRuleModeSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/OrganizationRuleModeSource)
