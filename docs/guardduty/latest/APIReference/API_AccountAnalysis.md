---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AccountAnalysis.html
---

# AccountAnalysis
<a name="API_AccountAnalysis"></a>

Contains an analysis of the findings in an AWS account.

## Contents
<a name="API_AccountAnalysis_Contents"></a>

 ** affectedResources **   <a name="guardduty-Type-AccountAnalysis-affectedResources"></a>
The resources in the account that are associated with findings.
Type: Array of [AccountAffectedResource](API_AccountAffectedResource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** findingsSummary **   <a name="guardduty-Type-AccountAnalysis-findingsSummary"></a>
A summary of the findings in the account.
Type: [FindingsSummary](API_FindingsSummary.md) object
Required: No

 ** tacticCoverage **   <a name="guardduty-Type-AccountAnalysis-tacticCoverage"></a>
The findings in the account, mapped to MITRE ATT&CK tactics and techniques.
Type: Array of [TacticCoverage](API_TacticCoverage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_AccountAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AccountAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AccountAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AccountAnalysis)
