---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Indicator.html
---

# Indicator
<a name="API_Indicator"></a>

Contains information about the indicators that include a set of signals observed in an attack sequence.

## Contents
<a name="API_Indicator_Contents"></a>

 ** key **   <a name="guardduty-Type-Indicator-key"></a>
Specific indicator keys observed in the attack sequence. For description of the valid values for key, see [Attack sequence finding details](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-summary.html#guardduty-extended-threat-detection-attack-sequence-finding-details) in the *Amazon GuardDuty User Guide*.
Type: String
Valid Values: `SUSPICIOUS_USER_AGENT | SUSPICIOUS_NETWORK | MALICIOUS_IP | TOR_IP | ATTACK_TACTIC | HIGH_RISK_API | ATTACK_TECHNIQUE | UNUSUAL_API_FOR_ACCOUNT | UNUSUAL_ASN_FOR_ACCOUNT | UNUSUAL_ASN_FOR_USER | SUSPICIOUS_PROCESS | MALICIOUS_DOMAIN | MALICIOUS_PROCESS | CRYPTOMINING_IP | CRYPTOMINING_DOMAIN | CRYPTOMINING_PROCESS | MALICIOUS_FILE | VULNERABILITY | MALICIOUS_PACKAGE | MISCONFIGURATION | REACHABILITY | SENSITIVE_DATA`
Required: Yes

 ** title **   <a name="guardduty-Type-Indicator-title"></a>
Title describing the indicator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** values **   <a name="guardduty-Type-Indicator-values"></a>
Values associated with each indicator key. For example, if the indicator key is `SUSPICIOUS_NETWORK`, then the value will be the name of the network. If the indicator key is `ATTACK_TACTIC`, then the value will be one of the MITRE tactics.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 400 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Indicator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Indicator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Indicator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Indicator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
