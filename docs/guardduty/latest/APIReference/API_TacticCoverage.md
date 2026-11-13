---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_TacticCoverage.html
---

# TacticCoverage
<a name="API_TacticCoverage"></a>

Contains information about the findings associated with a MITRE ATT&CK tactic.

## Contents
<a name="API_TacticCoverage_Contents"></a>

 ** findingCount **   <a name="guardduty-Type-TacticCoverage-findingCount"></a>
The number of findings associated with the tactic.
Type: Integer
Required: No

 ** findingTypes **   <a name="guardduty-Type-TacticCoverage-findingTypes"></a>
The finding types associated with the tactic.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** phase **   <a name="guardduty-Type-TacticCoverage-phase"></a>
The name of the tactic. Possible values are `Reconnaissance`, `Resource Development`, `Initial Access`, `Execution`, `Persistence`, `Privilege Escalation`, `Defense Evasion`, `Credential Access`, `Discovery`, `Lateral Movement`, `Collection`, `Command and Control`, `Exfiltration`, and `Impact`.
Type: String
Valid Values: `Reconnaissance | Resource Development | Initial Access | Execution | Persistence | Privilege Escalation | Defense Evasion | Credential Access | Discovery | Lateral Movement | Collection | Command and Control | Exfiltration | Impact`
Required: No

 ** techniques **   <a name="guardduty-Type-TacticCoverage-techniques"></a>
The MITRE ATT&CK techniques within the tactic that are associated with findings.
Type: Array of [TechniqueCoverage](API_TechniqueCoverage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_TacticCoverage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/TacticCoverage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/TacticCoverage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/TacticCoverage)
