---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Indicator.html
---

# Indicator
<a name="API_Indicator"></a>

 Contains information about the indicators observed in an Amazon GuardDuty Extended Threat Detection attack sequence. Indicators include a set of signals, which can be API activities or findings that GuardDuty uses to detect an attack sequence finding. GuardDuty generates an attack sequence finding when multiple signals align to a potentially suspicious activity. To receive GuardDuty attack sequence findings in AWS Security Hub CSPM, you must have GuardDuty and GuardDuty S3 Protection enabled. For more information, see [GuardDuty Extended Threat Detection ](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html) in the *Amazon GuardDuty User Guide*.

## Contents
<a name="API_Indicator_Contents"></a>

 ** Key **   <a name="securityhub-Type-Indicator-Key"></a>
 The name of the indicator that’s present in the attack sequence finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Title **   <a name="securityhub-Type-Indicator-Title"></a>
 The title describing the indicator.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-Indicator-Type"></a>
 The type of indicator.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Values **   <a name="securityhub-Type-Indicator-Values"></a>
Values associated with each indicator key. For example, if the indicator key is `SUSPICIOUS_NETWORK`, then the value will be the name of the network. If the indicator key is `ATTACK_TACTIC`, then the value will be one of the MITRE tactics.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Indicator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Indicator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Indicator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Indicator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
