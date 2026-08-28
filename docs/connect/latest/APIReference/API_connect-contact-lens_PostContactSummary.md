---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-contact-lens_PostContactSummary.html
---

# PostContactSummary
<a name="API_connect-contact-lens_PostContactSummary"></a>

Information about the post-contact summary.

## Contents
<a name="API_connect-contact-lens_PostContactSummary_Contents"></a>

 ** Status **   <a name="connect-Type-connect-contact-lens_PostContactSummary-Status"></a>
Whether the summary was successfully COMPLETED or FAILED to be generated.
Type: String
Valid Values: `FAILED | COMPLETED`
Required: Yes

 ** Content **   <a name="connect-Type-connect-contact-lens_PostContactSummary-Content"></a>
The content of the summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1762.
Required: No

 ** FailureCode **   <a name="connect-Type-connect-contact-lens_PostContactSummary-FailureCode"></a>
If the summary failed to be generated, one of the following failure codes occurs:
+  `QUOTA_EXCEEDED`: The number of concurrent analytics jobs reached your service quota.
+  `INSUFFICIENT_CONVERSATION_CONTENT`: The conversation needs to have at least one turn from both the participants in order to generate the summary.
+  `FAILED_SAFETY_GUIDELINES`: The generated summary cannot be provided because it failed to meet system safety guidelines.
+  `INVALID_ANALYSIS_CONFIGURATION`: This code occurs when, for example, you're using a [language](https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html#supported-languages-contact-lens) that isn't supported by generative AI-powered post-contact summaries.
+  `INTERNAL_ERROR`: Internal system error.
Type: String
Valid Values: `QUOTA_EXCEEDED | INSUFFICIENT_CONVERSATION_CONTENT | FAILED_SAFETY_GUIDELINES | INVALID_ANALYSIS_CONFIGURATION | INTERNAL_ERROR`
Required: No

## See Also
<a name="API_connect-contact-lens_PostContactSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-contact-lens-2020-08-21/PostContactSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-contact-lens-2020-08-21/PostContactSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-contact-lens-2020-08-21/PostContactSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
