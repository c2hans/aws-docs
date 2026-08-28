---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeEthereumAttributes.html
---

# NodeEthereumAttributes
<a name="API_NodeEthereumAttributes"></a>

Attributes of an Ethereum node.

## Contents
<a name="API_NodeEthereumAttributes_Contents"></a>

 ** HttpEndpoint **   <a name="ManagedBlockchain-Type-NodeEthereumAttributes-HttpEndpoint"></a>
The endpoint on which the Ethereum node listens to run Ethereum API methods over HTTP connections from a client. Use this endpoint in client code for smart contracts when using an HTTP connection. Connections to this endpoint are authenticated using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).
Type: String
Required: No

 ** WebSocketEndpoint **   <a name="ManagedBlockchain-Type-NodeEthereumAttributes-WebSocketEndpoint"></a>
The endpoint on which the Ethereum node listens to run Ethereum JSON-RPC methods over WebSocket connections from a client. Use this endpoint in client code for smart contracts when using a WebSocket connection. Connections to this endpoint are authenticated using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).
Type: String
Required: No

## See Also
<a name="API_NodeEthereumAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/NodeEthereumAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/NodeEthereumAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/NodeEthereumAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
