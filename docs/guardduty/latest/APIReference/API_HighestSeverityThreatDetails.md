---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_HighestSeverityThreatDetails.html
---

# HighestSeverityThreatDetails
<a name="API_HighestSeverityThreatDetails"></a>

Contains details of the highest severity threat detected during scan and number of infected files.

## Contents
<a name="API_HighestSeverityThreatDetails_Contents"></a>

 ** count **   <a name="guardduty-Type-HighestSeverityThreatDetails-count"></a>
Total number of infected files with the highest severity threat detected.
Type: Integer
Required: No

 ** severity **   <a name="guardduty-Type-HighestSeverityThreatDetails-severity"></a>
Severity level of the highest severity threat detected.
Type: String
Required: No

 ** threatName **   <a name="guardduty-Type-HighestSeverityThreatDetails-threatName"></a>
Threat name of the highest severity threat detected as part of the malware scan.
Type: String
Required: No

## See Also
<a name="API_HighestSeverityThreatDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/HighestSeverityThreatDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/HighestSeverityThreatDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/HighestSeverityThreatDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
