---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_PreProcessingTrace.html
---

# PreProcessingTrace
<a name="API_agent-runtime_PreProcessingTrace"></a>

Details about the pre-processing step, in which the agent contextualizes and categorizes user inputs.

## Contents
<a name="API_agent-runtime_PreProcessingTrace_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** modelInvocationInput **   <a name="bedrock-Type-agent-runtime_PreProcessingTrace-modelInvocationInput"></a>
The input for the pre-processing step.
+ The `type` is `PRE_PROCESSING`.
+ The `text` contains the prompt.
+ The `inferenceConfiguration`, `parserMode`, and `overrideLambda` values are set in the [PromptOverrideConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html) object that was set when the agent was created or updated.
Type: [ModelInvocationInput](API_agent-runtime_ModelInvocationInput.md) object
Required: No

 ** modelInvocationOutput **   <a name="bedrock-Type-agent-runtime_PreProcessingTrace-modelInvocationOutput"></a>
The foundation model output from the pre-processing step.
Type: [PreProcessingModelInvocationOutput](API_agent-runtime_PreProcessingModelInvocationOutput.md) object
Required: No

## See Also
<a name="API_agent-runtime_PreProcessingTrace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/PreProcessingTrace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/PreProcessingTrace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/PreProcessingTrace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
