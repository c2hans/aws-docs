---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormMultiSelectQuestionOption.html
---

# EvaluationFormMultiSelectQuestionOption
<a name="API_EvaluationFormMultiSelectQuestionOption"></a>

An option for a multi-select question in an evaluation form.

## Contents
<a name="API_EvaluationFormMultiSelectQuestionOption_Contents"></a>

 ** RefId **   <a name="connect-Type-EvaluationFormMultiSelectQuestionOption-RefId"></a>
Reference identifier for this option.
Type: String
Required: Yes

 ** Text **   <a name="connect-Type-EvaluationFormMultiSelectQuestionOption-Text"></a>
Display text for this option.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** AutomaticFail **   <a name="connect-Type-EvaluationFormMultiSelectQuestionOption-AutomaticFail"></a>
The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.
Type: Boolean
Required: No

 ** AutomaticFailConfiguration **   <a name="connect-Type-EvaluationFormMultiSelectQuestionOption-AutomaticFailConfiguration"></a>
Information about automatic fail configuration for an evaluation form.
Type: [AutomaticFailConfiguration](API_AutomaticFailConfiguration.md) object
Required: No

 ** PointsConfiguration **   <a name="connect-Type-EvaluationFormMultiSelectQuestionOption-PointsConfiguration"></a>
The points configuration for point-based scoring.
Type: [QuestionOptionPointsConfiguration](API_QuestionOptionPointsConfiguration.md) object
Required: No

 ** Score **   <a name="connect-Type-EvaluationFormMultiSelectQuestionOption-Score"></a>
The score assigned to the answer option.
Type: Integer
Required: No

## See Also
<a name="API_EvaluationFormMultiSelectQuestionOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormMultiSelectQuestionOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormMultiSelectQuestionOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormMultiSelectQuestionOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
