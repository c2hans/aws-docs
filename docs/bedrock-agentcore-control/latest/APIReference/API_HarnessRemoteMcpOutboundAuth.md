---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessRemoteMcpOutboundAuth.html
---

# HarnessRemoteMcpOutboundAuth

Authentication method for calling a remote MCP server.

## Contents
<a name="API_HarnessRemoteMcpOutboundAuth_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsIam **   <a name="bedrockagentcorecontrol-Type-HarnessRemoteMcpOutboundAuth-awsIam"></a>
Sign requests to the remote MCP server with Signature Version 4 (SigV4) using the harness execution role. If you don't specify a Region, the harness Region is used.
Type: [IamCredentialProvider](API_IamCredentialProvider.md) object
Required: No

 ** none **   <a name="bedrockagentcorecontrol-Type-HarnessRemoteMcpOutboundAuth-none"></a>
No authentication.
Type: Structure
Required: No

## See Also
<a name="API_HarnessRemoteMcpOutboundAuth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessRemoteMcpOutboundAuth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessRemoteMcpOutboundAuth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessRemoteMcpOutboundAuth)
