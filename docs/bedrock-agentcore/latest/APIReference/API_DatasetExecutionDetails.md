---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DatasetExecutionDetails.html
---

# DatasetExecutionDetails

The details of the dataset and agent that a batch evaluation ran.

## Contents
<a name="API_DatasetExecutionDetails_Contents"></a>

 ** agentInvocation **   <a name="BedrockAgentCore-Type-DatasetExecutionDetails-agentInvocation"></a>
The agent that the batch evaluation invoked.
Type: [AgentInvocationDetails](API_AgentInvocationDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** dataset **   <a name="BedrockAgentCore-Type-DatasetExecutionDetails-dataset"></a>
The dataset and the version of it that the batch evaluation ran.
Type: [DatasetDetails](API_DatasetDetails.md) object
Required: Yes

## See Also
<a name="API_DatasetExecutionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DatasetExecutionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DatasetExecutionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DatasetExecutionDetails)
