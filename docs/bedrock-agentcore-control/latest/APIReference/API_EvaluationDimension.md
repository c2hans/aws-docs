---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_EvaluationDimension.html
---

# EvaluationDimension
<a name="API_EvaluationDimension"></a>

 A single dimension of an LLM-as-a-judge evaluator, defining what the evaluator model should judge for that dimension and how it should be scored.

## Contents
<a name="API_EvaluationDimension_Contents"></a>

 ** dimensionInstruction **   <a name="bedrockagentcorecontrol-Type-EvaluationDimension-dimensionInstruction"></a>
 The instruction to the evaluator model for this dimension, describing what the model should judge when scoring the dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Required: Yes

 ** dimensionName **   <a name="bedrockagentcorecontrol-Type-EvaluationDimension-dimensionName"></a>
 The name of the dimension. This name is unique within the evaluator and identifies the dimension's results.
Type: String
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** dimensionRatingScale **   <a name="bedrockagentcorecontrol-Type-EvaluationDimension-dimensionRatingScale"></a>
 The rating scale for this dimension, which can be numerical or categorical. A dimension's rating scale cannot itself be multi-dimensional.
Type: [DimensionRatingScale](API_DimensionRatingScale.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_EvaluationDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/EvaluationDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/EvaluationDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/EvaluationDimension)
