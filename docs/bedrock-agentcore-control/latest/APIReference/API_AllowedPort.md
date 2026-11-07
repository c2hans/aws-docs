---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_AllowedPort.html
---

# AllowedPort
<a name="API_AllowedPort"></a>

A port or port range that is reachable through the runtime's session URL. Specify exactly one of `port` or `portRange`.

## Contents
<a name="API_AllowedPort_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** port **   <a name="bedrockagentcorecontrol-Type-AllowedPort-port"></a>
A single port that is reachable through the runtime's session URL.
Type: Integer
Valid Range: Minimum value of 8000. Maximum value of 12000.
Required: No

 ** portRange **   <a name="bedrockagentcorecontrol-Type-AllowedPort-portRange"></a>
An inclusive range of ports that are reachable through the runtime's session URL.
Type: [PortRange](API_PortRange.md) object
Required: No

## See Also
<a name="API_AllowedPort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/AllowedPort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/AllowedPort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/AllowedPort)
