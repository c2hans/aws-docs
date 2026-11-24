---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CpuOptions.html
---

# CpuOptions

The CPU configuration for capacity provider instances, including nested virtualization.

## Contents
<a name="API_CpuOptions_Contents"></a>

 ** nestedVirtualization **   <a name="bedrockagentcorecontrol-Type-CpuOptions-nestedVirtualization"></a>
Specifies whether your agents can use hardware virtualization on their instances. The following values are possible:
+  `ENABLED` – Your agents can use hardware virtualization on their instances. To use this value, choose the `LINUX_X86_64` operating system and instance types that support nested virtualization.
+  `DISABLED` – Your agents can't use hardware virtualization on their instances. This is the default.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_CpuOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CpuOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CpuOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CpuOptions)
