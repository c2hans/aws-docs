---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DatasetExecutionConfig.html
---

# DatasetExecutionConfig

The configuration for running the scenarios in a dataset against an agent as part of a batch evaluation.

## Contents
<a name="API_DatasetExecutionConfig_Contents"></a>

 ** agentInvocation **   <a name="BedrockAgentCore-Type-DatasetExecutionConfig-agentInvocation"></a>
Specifies the agent runtime endpoint and the request template that the batch evaluation uses to invoke the agent for each scenario in the dataset.
Type: [AgentInvocationConfig](API_AgentInvocationConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** dataset **   <a name="BedrockAgentCore-Type-DatasetExecutionConfig-dataset"></a>
The dataset whose scenarios are sent to the agent. The dataset must use the predefined evaluation schema, and the version that runs must contain between 1 and 1,000 scenarios.
Type: [DatasetSource](API_DatasetSource.md) object
Required: Yes

## See Also
<a name="API_DatasetExecutionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DatasetExecutionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DatasetExecutionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DatasetExecutionConfig)
