---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeConfiguration.html
---

# NodeConfiguration
<a name="API_NodeConfiguration"></a>

Configuration properties of a node.

## Contents
<a name="API_NodeConfiguration_Contents"></a>

 ** InstanceType **   <a name="ManagedBlockchain-Type-NodeConfiguration-InstanceType"></a>
The Amazon Managed Blockchain instance type for the node.
Type: String
Required: Yes

 ** AvailabilityZone **   <a name="ManagedBlockchain-Type-NodeConfiguration-AvailabilityZone"></a>
The Availability Zone in which the node exists. Required for Ethereum nodes.
Type: String
Required: No

 ** LogPublishingConfiguration **   <a name="ManagedBlockchain-Type-NodeConfiguration-LogPublishingConfiguration"></a>
Configuration properties for logging events associated with a peer node on a Hyperledger Fabric network on Managed Blockchain.
Type: [NodeLogPublishingConfiguration](API_NodeLogPublishingConfiguration.md) object
Required: No

 ** StateDB **   <a name="ManagedBlockchain-Type-NodeConfiguration-StateDB"></a>
The state database that the node uses. Values are `LevelDB` or `CouchDB`. When using an Amazon Managed Blockchain network with Hyperledger Fabric version 1.4 or later, the default is `CouchDB`.
Applies only to Hyperledger Fabric.
Type: String
Valid Values: `LevelDB | CouchDB`
Required: No

## See Also
<a name="API_NodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/NodeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/NodeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/NodeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
