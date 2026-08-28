---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeFabricLogPublishingConfiguration.html
---

# NodeFabricLogPublishingConfiguration
<a name="API_NodeFabricLogPublishingConfiguration"></a>

Configuration properties for logging events associated with a peer node owned by a member in a Managed Blockchain network.

## Contents
<a name="API_NodeFabricLogPublishingConfiguration_Contents"></a>

 ** ChaincodeLogs **   <a name="ManagedBlockchain-Type-NodeFabricLogPublishingConfiguration-ChaincodeLogs"></a>
Configuration properties for logging events associated with chaincode execution on a peer node. Chaincode logs contain the results of instantiating, invoking, and querying the chaincode. A peer can run multiple instances of chaincode. When enabled, a log stream is created for all chaincodes, with an individual log stream for each chaincode.
Type: [LogConfigurations](API_LogConfigurations.md) object
Required: No

 ** PeerLogs **   <a name="ManagedBlockchain-Type-NodeFabricLogPublishingConfiguration-PeerLogs"></a>
Configuration properties for a peer node log. Peer node logs contain messages generated when your client submits transaction proposals to peer nodes, requests to join channels, enrolls an admin peer, and lists the chaincode instances on a peer node.
Type: [LogConfigurations](API_LogConfigurations.md) object
Required: No

## See Also
<a name="API_NodeFabricLogPublishingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/NodeFabricLogPublishingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/NodeFabricLogPublishingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/NodeFabricLogPublishingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
