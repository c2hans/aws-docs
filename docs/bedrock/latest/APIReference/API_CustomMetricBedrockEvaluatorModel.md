---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CustomMetricBedrockEvaluatorModel.html
---

# CustomMetricBedrockEvaluatorModel
<a name="API_CustomMetricBedrockEvaluatorModel"></a>

Defines the model you want to evaluate custom metrics in an Amazon Bedrock evaluation job.

## Contents
<a name="API_CustomMetricBedrockEvaluatorModel_Contents"></a>

 ** modelIdentifier **   <a name="bedrock-Type-CustomMetricBedrockEvaluatorModel-modelIdentifier"></a>
The Amazon Resource Name (ARN) of the evaluator model for custom metrics. For a list of supported evaluator models, see [Evaluate model performance using another LLM as a judge](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html) and [Evaluate the performance of RAG sources using Amazon Bedrock evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:((:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:inference-profile/(([a-z-]{2,8}.)[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63})))))$|(^[a-z0-9-]+[.][a-z0-9-]+([.][a-z0-9-]+)*(:[a-z0-9-]+)?$)|^[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)`
Required: Yes

## See Also
<a name="API_CustomMetricBedrockEvaluatorModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CustomMetricBedrockEvaluatorModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CustomMetricBedrockEvaluatorModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CustomMetricBedrockEvaluatorModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
