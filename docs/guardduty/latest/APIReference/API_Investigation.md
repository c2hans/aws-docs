---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Investigation.html
---

# Investigation
<a name="API_Investigation"></a>

Contains the details and results of a GuardDuty investigation.

## Contents
<a name="API_Investigation_Contents"></a>

 ** investigationId **   <a name="guardduty-Type-Investigation-investigationId"></a>
The unique identifier of the investigation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-fA-F0-9\-]+`
Required: Yes

 ** status **   <a name="guardduty-Type-Investigation-status"></a>
The current status of the investigation. Possible values are `RUNNING`, `COMPLETED`, and `FAILED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `RUNNING | COMPLETED | FAILED`
Required: Yes

 ** triggeredBy **   <a name="guardduty-Type-Investigation-triggeredBy"></a>
The account that initiated the investigation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** triggerPrompt **   <a name="guardduty-Type-Investigation-triggerPrompt"></a>
The natural-language prompt that initiated this investigation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** cloud **   <a name="guardduty-Type-Investigation-cloud"></a>
Details about the cloud environment in which the investigation was performed, including the provider, region, and account.
Type: [CloudDetails](API_CloudDetails.md) object
Required: No

 ** confidence **   <a name="guardduty-Type-Investigation-confidence"></a>
The confidence level of the investigation's assessment. Possible values are `Unknown`, `Low`, `Medium`, and `High`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Valid Values: `Unknown | Low | Medium | High`
Required: No

 ** endTime **   <a name="guardduty-Type-Investigation-endTime"></a>
The timestamp at which the investigation completed.
Type: Timestamp
Required: No

 ** error **   <a name="guardduty-Type-Investigation-error"></a>
Details about the error if the investigation status is `FAILED`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** metadata **   <a name="guardduty-Type-Investigation-metadata"></a>
Metadata about the product and version that produced the investigation.
Type: [InvestigationMetadata](API_InvestigationMetadata.md) object
Required: No

 ** risk **   <a name="guardduty-Type-Investigation-risk"></a>
A human-readable description of the assessed risk.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** riskLevel **   <a name="guardduty-Type-Investigation-riskLevel"></a>
The assessed risk level of the investigated threat. Possible values are `Info`, `Low`, `Medium`, `High`, and `Critical`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `Info | Low | Medium | High | Critical`
Required: No

 ** startTime **   <a name="guardduty-Type-Investigation-startTime"></a>
The timestamp at which the investigation started.
Type: Timestamp
Required: No

 ** summary **   <a name="guardduty-Type-Investigation-summary"></a>
A structured summary of the investigation findings, including affected resources, threat assessment, and recommended remediation steps.
Type: String
Required: No

## See Also
<a name="API_Investigation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Investigation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Investigation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Investigation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
