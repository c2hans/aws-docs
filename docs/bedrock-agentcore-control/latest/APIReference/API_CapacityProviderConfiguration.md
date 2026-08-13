---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CapacityProviderConfiguration.html
---

# CapacityProviderConfiguration
<a name="API_CapacityProviderConfiguration"></a>

The configuration for a capacity provider that supplies compute resources to the AgentCore Runtime. Specify this configuration to run the AgentCore Runtime on Amazon EC2 instances in your account.

## Contents
<a name="API_CapacityProviderConfiguration_Contents"></a>

 ** capacityProviderArn **   <a name="bedrockagentcorecontrol-Type-CapacityProviderConfiguration-capacityProviderArn"></a>
The Amazon Resource Name (ARN) of the capacity provider to use for the AgentCore Runtime.
Type: String
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:capacity-provider/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`
Required: No

## See Also
<a name="API_CapacityProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CapacityProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CapacityProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CapacityProviderConfiguration)
