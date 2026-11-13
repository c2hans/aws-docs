---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessAgentCoreRuntimeEnvironmentRequest.html
---

# HarnessAgentCoreRuntimeEnvironmentRequest
<a name="API_HarnessAgentCoreRuntimeEnvironmentRequest"></a>

The AgentCore Runtime environment request configuration.

## Contents
<a name="API_HarnessAgentCoreRuntimeEnvironmentRequest_Contents"></a>

 ** filesystemConfigurations **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreRuntimeEnvironmentRequest-filesystemConfigurations"></a>
The filesystem configurations for the runtime environment.
Type: Array of [FilesystemConfiguration](API_FilesystemConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** lifecycleConfiguration **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreRuntimeEnvironmentRequest-lifecycleConfiguration"></a>
The lifecycle configuration for the harness's runtime environment. For a harness, `idleRuntimeSessionTimeout` and `maxLifetime` each accept a value between 60 and 28800 seconds (8 hours), and `idleRuntimeSessionTimeout` must be less than or equal to `maxLifetime`. Values above 28800 seconds are rejected with a `ValidationException`.
Type: [LifecycleConfiguration](API_LifecycleConfiguration.md) object
Required: No

 ** networkConfiguration **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreRuntimeEnvironmentRequest-networkConfiguration"></a>
SecurityConfig for the Agent.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

## See Also
<a name="API_HarnessAgentCoreRuntimeEnvironmentRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessAgentCoreRuntimeEnvironmentRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessAgentCoreRuntimeEnvironmentRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessAgentCoreRuntimeEnvironmentRequest)
