---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationQuestionAnswerAnalysisDetails.html
---

# EvaluationQuestionAnswerAnalysisDetails
<a name="API_EvaluationQuestionAnswerAnalysisDetails"></a>

Detailed analysis results of the automated answer to the evaluation question.

## Contents
<a name="API_EvaluationQuestionAnswerAnalysisDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ContactLens **   <a name="connect-Type-EvaluationQuestionAnswerAnalysisDetails-ContactLens"></a>
Analysis results from the Contact Lens automation for the question.
Type: [EvaluationContactLensAnswerAnalysisDetails](API_EvaluationContactLensAnswerAnalysisDetails.md) object
Required: No

 ** GenAI **   <a name="connect-Type-EvaluationQuestionAnswerAnalysisDetails-GenAI"></a>
Analysis results from the generative AI automation for the question.
Type: [EvaluationGenAIAnswerAnalysisDetails](API_EvaluationGenAIAnswerAnalysisDetails.md) object
Required: No

## See Also
<a name="API_EvaluationQuestionAnswerAnalysisDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationQuestionAnswerAnalysisDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationQuestionAnswerAnalysisDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationQuestionAnswerAnalysisDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
