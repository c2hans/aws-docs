---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_OperatingSystemConfiguration.html
---

# OperatingSystemConfiguration

Contains the operating system configuration of the agents that AgentCore Runtime runs on a capacity provider. Specify the member for the operating system of the capacity provider.

## Contents
<a name="API_OperatingSystemConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** linux **   <a name="bedrockagentcorecontrol-Type-OperatingSystemConfiguration-linux"></a>
The operating system configuration of agents that run on Linux instances.
Type: [LinuxOperatingSystemConfiguration](API_LinuxOperatingSystemConfiguration.md) object
Required: No

## See Also
<a name="API_OperatingSystemConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/OperatingSystemConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/OperatingSystemConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/OperatingSystemConfiguration)
