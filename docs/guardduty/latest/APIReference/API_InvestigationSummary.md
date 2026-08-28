---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationSummary.html
---

# InvestigationSummary
<a name="API_InvestigationSummary"></a>

Contains summary information about a GuardDuty investigation.

## Contents
<a name="API_InvestigationSummary_Contents"></a>

 ** accountId **   <a name="guardduty-Type-InvestigationSummary-accountId"></a>
The AWS account ID associated with the investigation.
Type: String
Required: No

 ** confidence **   <a name="guardduty-Type-InvestigationSummary-confidence"></a>
The confidence level of the investigation's assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Valid Values: `Unknown | Low | Medium | High`
Required: No

 ** endTime **   <a name="guardduty-Type-InvestigationSummary-endTime"></a>
The timestamp at which the investigation completed.
Type: Timestamp
Required: No

 ** investigationId **   <a name="guardduty-Type-InvestigationSummary-investigationId"></a>
The unique identifier of the investigation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-fA-F0-9\-]+`
Required: No

 ** riskLevel **   <a name="guardduty-Type-InvestigationSummary-riskLevel"></a>
The assessed risk level of the investigated threat.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `Info | Low | Medium | High | Critical`
Required: No

 ** startTime **   <a name="guardduty-Type-InvestigationSummary-startTime"></a>
The timestamp at which the investigation started.
Type: Timestamp
Required: No

 ** status **   <a name="guardduty-Type-InvestigationSummary-status"></a>
The current status of the investigation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `RUNNING | COMPLETED | FAILED`
Required: No

 ** title **   <a name="guardduty-Type-InvestigationSummary-title"></a>
A short title summarizing the investigation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** triggerPrompt **   <a name="guardduty-Type-InvestigationSummary-triggerPrompt"></a>
The natural-language prompt that initiated this investigation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_InvestigationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
