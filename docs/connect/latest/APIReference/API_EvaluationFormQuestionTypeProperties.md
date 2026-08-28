---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormQuestionTypeProperties.html
---

# EvaluationFormQuestionTypeProperties
<a name="API_EvaluationFormQuestionTypeProperties"></a>

Information about properties for a question in an evaluation form. The question type properties must be either for a numeric question or a single select question.

## Contents
<a name="API_EvaluationFormQuestionTypeProperties_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** MultiSelect **   <a name="connect-Type-EvaluationFormQuestionTypeProperties-MultiSelect"></a>
Properties for multi-select question types.
Type: [EvaluationFormMultiSelectQuestionProperties](API_EvaluationFormMultiSelectQuestionProperties.md) object
Required: No

 ** Numeric **   <a name="connect-Type-EvaluationFormQuestionTypeProperties-Numeric"></a>
The properties of the numeric question.
Type: [EvaluationFormNumericQuestionProperties](API_EvaluationFormNumericQuestionProperties.md) object
Required: No

 ** SingleSelect **   <a name="connect-Type-EvaluationFormQuestionTypeProperties-SingleSelect"></a>
The properties of the numeric question.
Type: [EvaluationFormSingleSelectQuestionProperties](API_EvaluationFormSingleSelectQuestionProperties.md) object
Required: No

 ** Text **   <a name="connect-Type-EvaluationFormQuestionTypeProperties-Text"></a>
The properties of the text question.
Type: [EvaluationFormTextQuestionProperties](API_EvaluationFormTextQuestionProperties.md) object
Required: No

## See Also
<a name="API_EvaluationFormQuestionTypeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormQuestionTypeProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormQuestionTypeProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormQuestionTypeProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
