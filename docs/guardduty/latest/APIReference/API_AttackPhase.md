---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AttackPhase.html
---

# AttackPhase
<a name="API_AttackPhase"></a>

Contains information about one phase of an attack.

## Contents
<a name="API_AttackPhase_Contents"></a>

 ** attacks **   <a name="guardduty-Type-AttackPhase-attacks"></a>
The MITRE ATT&CK tactics and techniques observed in this phase, with the findings that are associated with them.
Type: Array of [Attack](API_Attack.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** description **   <a name="guardduty-Type-AttackPhase-description"></a>
A description of the activity in this phase.
Type: String
Required: No

 ** phase **   <a name="guardduty-Type-AttackPhase-phase"></a>
The MITRE ATT&CK tactic of the phase. Possible values are `Reconnaissance`, `Resource Development`, `Initial Access`, `Execution`, `Persistence`, `Privilege Escalation`, `Defense Evasion`, `Credential Access`, `Discovery`, `Lateral Movement`, `Collection`, `Command and Control`, `Exfiltration`, and `Impact`.
Type: String
Valid Values: `Reconnaissance | Resource Development | Initial Access | Execution | Persistence | Privilege Escalation | Defense Evasion | Credential Access | Discovery | Lateral Movement | Collection | Command and Control | Exfiltration | Impact`
Required: No

## See Also
<a name="API_AttackPhase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AttackPhase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AttackPhase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AttackPhase)
