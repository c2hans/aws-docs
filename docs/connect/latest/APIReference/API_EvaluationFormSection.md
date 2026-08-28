---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormSection.html
---

# EvaluationFormSection
<a name="API_EvaluationFormSection"></a>

Information about a section from an evaluation form. A section can contain sections and/or questions. Evaluation forms can only contain sections and subsections (two level nesting).

## Contents
<a name="API_EvaluationFormSection_Contents"></a>

 ** Items **   <a name="connect-Type-EvaluationFormSection-Items"></a>
The items of the section.
Type: Array of [EvaluationFormItem](API_EvaluationFormItem.md) objects
Required: Yes

 ** RefId **   <a name="connect-Type-EvaluationFormSection-RefId"></a>
The identifier of the section. An identifier must be unique within the evaluation form.
Type: String
Required: Yes

 ** Title **   <a name="connect-Type-EvaluationFormSection-Title"></a>
The title of the section.
Type: String
Required: Yes

 ** Instructions **   <a name="connect-Type-EvaluationFormSection-Instructions"></a>
The instructions of the section.
Type: String
Required: No

 ** IsExcludedFromScoring **   <a name="connect-Type-EvaluationFormSection-IsExcludedFromScoring"></a>
The flag to exclude the section from scoring.
Type: Boolean
Required: No

 ** ScoreThresholds **   <a name="connect-Type-EvaluationFormSection-ScoreThresholds"></a>
The score thresholds for performance categories.
Type: Array of [EvaluationFormScoreThreshold](API_EvaluationFormScoreThreshold.md) objects
Required: No

 ** Weight **   <a name="connect-Type-EvaluationFormSection-Weight"></a>
The scoring weight of the section.
Type: Double
Required: No

## See Also
<a name="API_EvaluationFormSection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormSection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormSection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormSection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
