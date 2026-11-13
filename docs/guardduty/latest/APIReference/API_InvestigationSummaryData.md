---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationSummaryData.html
---

# InvestigationSummaryData
<a name="API_InvestigationSummaryData"></a>

Contains the structured summary of a GuardDuty investigation. The fields that are present depend on the investigation type.

## Contents
<a name="API_InvestigationSummaryData_Contents"></a>

 ** accountAnalysis **   <a name="guardduty-Type-InvestigationSummaryData-accountAnalysis"></a>
For an `ACCOUNT` investigation, an analysis of the findings in the investigated account.
Type: [AccountAnalysis](API_AccountAnalysis.md) object
Required: No

 ** countermeasures **   <a name="guardduty-Type-InvestigationSummaryData-countermeasures"></a>
For a `FINDING` investigation, actions that you can take to respond to the threat, grouped by defensive tactic.
Type: Array of [Countermeasure](API_Countermeasure.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** findingType **   <a name="guardduty-Type-InvestigationSummaryData-findingType"></a>
For a `FINDING` investigation, the type of the finding that the investigation analyzed.
Type: String
Required: No

 ** keyObservations **   <a name="guardduty-Type-InvestigationSummaryData-keyObservations"></a>
The key observations of the investigation.
Type: [KeyObservations](API_KeyObservations.md) object
Required: No

 ** organizationAnalysis **   <a name="guardduty-Type-InvestigationSummaryData-organizationAnalysis"></a>
For an `ORGANIZATION` investigation, an analysis of the findings across the organization.
Type: [OrganizationAnalysis](API_OrganizationAnalysis.md) object
Required: No

 ** recommendations **   <a name="guardduty-Type-InvestigationSummaryData-recommendations"></a>
For an `ACCOUNT` or `ORGANIZATION` investigation, the recommended actions.
Type: Array of [Recommendation](API_Recommendation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** threatAssessment **   <a name="guardduty-Type-InvestigationSummaryData-threatAssessment"></a>
For a `FINDING` investigation, an assessment of the threat, including how the attack progressed.
Type: [ThreatAssessment](API_ThreatAssessment.md) object
Required: No

## See Also
<a name="API_InvestigationSummaryData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationSummaryData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationSummaryData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationSummaryData)
