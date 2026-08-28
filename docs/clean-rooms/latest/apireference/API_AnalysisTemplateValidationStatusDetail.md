---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisTemplateValidationStatusDetail.html
---

# AnalysisTemplateValidationStatusDetail
<a name="API_AnalysisTemplateValidationStatusDetail"></a>

The status details of the analysis template validation. AWS Clean Rooms Differential Privacy uses a general-purpose query structure to support complex SQL queries and validates whether an analysis template fits that general-purpose query structure. Validation is performed when analysis templates are created and fetched. Because analysis templates are immutable by design, we recommend that you create analysis templates after you associate the configured tables with their analysis rule to your collaboration.

For more information, see [https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules-custom.html#custom-diff-privacy](https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules-custom.html#custom-diff-privacy).

## Contents
<a name="API_AnalysisTemplateValidationStatusDetail_Contents"></a>

 ** status **   <a name="API-Type-AnalysisTemplateValidationStatusDetail-status"></a>
The status of the validation.
Type: String
Valid Values: `VALID | INVALID | UNABLE_TO_VALIDATE`
Required: Yes

 ** type **   <a name="API-Type-AnalysisTemplateValidationStatusDetail-type"></a>
The type of validation that was performed.
Type: String
Valid Values: `DIFFERENTIAL_PRIVACY`
Required: Yes

 ** reasons **   <a name="API-Type-AnalysisTemplateValidationStatusDetail-reasons"></a>
The reasons for the validation results.
Type: Array of [AnalysisTemplateValidationStatusReason](API_AnalysisTemplateValidationStatusReason.md) objects
Required: No

## See Also
<a name="API_AnalysisTemplateValidationStatusDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisTemplateValidationStatusDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisTemplateValidationStatusDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisTemplateValidationStatusDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
