---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ThreatAssessment.html
---

# ThreatAssessment
<a name="API_ThreatAssessment"></a>

Contains an assessment of the threat that a `FINDING` investigation identified.

## Contents
<a name="API_ThreatAssessment_Contents"></a>

 ** attackProgression **   <a name="guardduty-Type-ThreatAssessment-attackProgression"></a>
The phases of the attack, in terms of MITRE ATT&CK tactics.
Type: Array of [AttackPhase](API_AttackPhase.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** threatActorProfile **   <a name="guardduty-Type-ThreatAssessment-threatActorProfile"></a>
A description of the likely threat actor.
Type: String
Required: No

## See Also
<a name="API_ThreatAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ThreatAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ThreatAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ThreatAssessment)
