---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationThreatAssessment.html
---

# InvestigationThreatAssessment
<a name="API_InvestigationThreatAssessment"></a>

Contains a threat assessment. The members that are set depend on the `AnalysisType` of the record.

## Contents
<a name="API_InvestigationThreatAssessment_Contents"></a>

 ** assessment **   <a name="guardduty-Type-InvestigationThreatAssessment-assessment"></a>
The assessment of the threat.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** authenticationContext **   <a name="guardduty-Type-InvestigationThreatAssessment-authenticationContext"></a>
Context about how the identity involved in the activity authenticated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** classification **   <a name="guardduty-Type-InvestigationThreatAssessment-classification"></a>
The classification of the threat.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** credentialCompromise **   <a name="guardduty-Type-InvestigationThreatAssessment-credentialCompromise"></a>
An assessment of whether credentials were compromised.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** ipAccountActivity **   <a name="guardduty-Type-InvestigationThreatAssessment-ipAccountActivity"></a>
An assessment of the activity from the IP address in the account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** rdsControlPlaneActivity **   <a name="guardduty-Type-InvestigationThreatAssessment-rdsControlPlaneActivity"></a>
An assessment of Amazon RDS control plane activity that is related to the threat.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** reputation **   <a name="guardduty-Type-InvestigationThreatAssessment-reputation"></a>
Reputation information about a threat indicator. Set when `AnalysisType` is `REPUTATION`.
Type: [Reputation](API_Reputation.md) object
Required: No

 ** threatConfidence **   <a name="guardduty-Type-InvestigationThreatAssessment-threatConfidence"></a>
The confidence in the threat assessment. Possible values are `VERY_HIGH`, `HIGH`, `MEDIUM`, and `LOW`.
Type: String
Valid Values: `VERY_HIGH | HIGH | MEDIUM | LOW`
Required: No

## See Also
<a name="API_InvestigationThreatAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationThreatAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationThreatAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationThreatAssessment)
