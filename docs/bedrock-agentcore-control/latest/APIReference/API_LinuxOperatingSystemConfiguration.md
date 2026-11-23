---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_LinuxOperatingSystemConfiguration.html
---

# LinuxOperatingSystemConfiguration

Contains the operating system configuration of agents that run on Linux instances, such as the privilege mode.

## Contents
<a name="API_LinuxOperatingSystemConfiguration_Contents"></a>

 ** privilegeMode **   <a name="bedrockagentcorecontrol-Type-LinuxOperatingSystemConfiguration-privilegeMode"></a>
The privilege mode of the agents. If you omit this field, the agents run in `STANDARD` privilege mode. The following values are possible:
+  `STANDARD` – The agent runs without elevated privileges. This is the default.
+  `PRIVILEGED` – The agent runs with elevated privileges on its instance. Use this mode for agents that build container images, run containers, or install system packages. A session that runs a `PRIVILEGED` agent runs only that agent.
Type: String
Valid Values: `STANDARD | PRIVILEGED`
Required: No

## See Also
<a name="API_LinuxOperatingSystemConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LinuxOperatingSystemConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LinuxOperatingSystemConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LinuxOperatingSystemConfiguration)
