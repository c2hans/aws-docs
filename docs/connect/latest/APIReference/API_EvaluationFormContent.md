---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormContent.html
---

# EvaluationFormContent
<a name="API_EvaluationFormContent"></a>

Information about an evaluation form used in a contact evaluation.

## Contents
<a name="API_EvaluationFormContent_Contents"></a>

 ** EvaluationFormArn **   <a name="connect-Type-EvaluationFormContent-EvaluationFormArn"></a>
The Amazon Resource Name (ARN) for the evaluation form resource.
Type: String
Required: Yes

 ** EvaluationFormId **   <a name="connect-Type-EvaluationFormContent-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** EvaluationFormVersion **   <a name="connect-Type-EvaluationFormContent-EvaluationFormVersion"></a>
A version of the evaluation form.
Type: Integer
Required: Yes

 ** Items **   <a name="connect-Type-EvaluationFormContent-Items"></a>
Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.
Type: Array of [EvaluationFormItem](API_EvaluationFormItem.md) objects
Required: Yes

 ** Title **   <a name="connect-Type-EvaluationFormContent-Title"></a>
A title of the evaluation form.
Type: String
Required: Yes

 ** AutoEvaluationConfiguration **   <a name="connect-Type-EvaluationFormContent-AutoEvaluationConfiguration"></a>
The configuration of the automated evaluation.
Type: [EvaluationFormAutoEvaluationConfiguration](API_EvaluationFormAutoEvaluationConfiguration.md) object
Required: No

 ** Description **   <a name="connect-Type-EvaluationFormContent-Description"></a>
The description of the evaluation form.
Type: String
Required: No

 ** LanguageConfiguration **   <a name="connect-Type-EvaluationFormContent-LanguageConfiguration"></a>
Configuration for language settings of this evaluation form content.
Type: [EvaluationFormLanguageConfiguration](API_EvaluationFormLanguageConfiguration.md) object
Required: No

 ** ReviewConfiguration **   <a name="connect-Type-EvaluationFormContent-ReviewConfiguration"></a>
Configuration for evaluation review settings of this evaluation form content.
Type: [EvaluationReviewConfiguration](API_EvaluationReviewConfiguration.md) object
Required: No

 ** ScoringStrategy **   <a name="connect-Type-EvaluationFormContent-ScoringStrategy"></a>
A scoring strategy of the evaluation form.
Type: [EvaluationFormScoringStrategy](API_EvaluationFormScoringStrategy.md) object
Required: No

 ** TargetConfiguration **   <a name="connect-Type-EvaluationFormContent-TargetConfiguration"></a>
Configuration that specifies the target for this evaluation form content.
Type: [EvaluationFormTargetConfiguration](API_EvaluationFormTargetConfiguration.md) object
Required: No

## See Also
<a name="API_EvaluationFormContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
