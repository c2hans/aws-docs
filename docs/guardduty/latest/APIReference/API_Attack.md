---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Attack.html
---

# Attack
<a name="API_Attack"></a>

Contains a MITRE ATT&CK tactic and technique observed during an attack, with the findings that are associated with them.

## Contents
<a name="API_Attack_Contents"></a>

 ** findings **   <a name="guardduty-Type-Attack-findings"></a>
The findings associated with the tactic and technique.
Type: Array of [FindingReference](API_FindingReference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** tactic **   <a name="guardduty-Type-Attack-tactic"></a>
The MITRE ATT&CK tactic.
Type: [ThreatReference](API_ThreatReference.md) object
Required: No

 ** technique **   <a name="guardduty-Type-Attack-technique"></a>
The MITRE ATT&CK technique.
Type: [ThreatReference](API_ThreatReference.md) object
Required: No

 ** version **   <a name="guardduty-Type-Attack-version"></a>
The version of the attack framework that the tactic and technique classification uses.
Type: String
Required: No

## See Also
<a name="API_Attack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Attack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Attack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Attack)
