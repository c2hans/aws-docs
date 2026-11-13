---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_OrganizationAnalysis.html
---

# OrganizationAnalysis
<a name="API_OrganizationAnalysis"></a>

Contains an analysis of the findings across an organization.

## Contents
<a name="API_OrganizationAnalysis_Contents"></a>

 ** accountBreakdown **   <a name="guardduty-Type-OrganizationAnalysis-accountBreakdown"></a>
The accounts in the organization that have findings, with the number of findings in each.
Type: Array of [AccountSummary](API_AccountSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** findingsSummary **   <a name="guardduty-Type-OrganizationAnalysis-findingsSummary"></a>
A summary of the findings across the organization.
Type: [OrganizationFindingsSummary](API_OrganizationFindingsSummary.md) object
Required: No

## See Also
<a name="API_OrganizationAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/OrganizationAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/OrganizationAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/OrganizationAnalysis)
