---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Node.html
---

# Node
<a name="API_Node"></a>

Configuration properties of a node.

## Contents
<a name="API_Node_Contents"></a>

 ** Arn **   <a name="ManagedBlockchain-Type-Node-Arn"></a>
The Amazon Resource Name (ARN) of the node. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** AvailabilityZone **   <a name="ManagedBlockchain-Type-Node-AvailabilityZone"></a>
The Availability Zone in which the node exists. Required for Ethereum nodes.
Type: String
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-Node-CreationDate"></a>
The date and time that the node was created.
Type: Timestamp
Required: No

 ** FrameworkAttributes **   <a name="ManagedBlockchain-Type-Node-FrameworkAttributes"></a>
Attributes of the blockchain framework being used.
Type: [NodeFrameworkAttributes](API_NodeFrameworkAttributes.md) object
Required: No

 ** Id **   <a name="ManagedBlockchain-Type-Node-Id"></a>
The unique identifier of the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** InstanceType **   <a name="ManagedBlockchain-Type-Node-InstanceType"></a>
The instance type of the node.
Type: String
Required: No

 ** KmsKeyArn **   <a name="ManagedBlockchain-Type-Node-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the customer managed key in AWS Key Management Service (AWS KMS) that the node uses for encryption at rest. If the value of this parameter is `"AWS Owned KMS Key"`, the node uses an AWS owned KMS key for encryption. The node inherits this parameter from the member that it belongs to.
For more information, see [Encryption at Rest](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-encryption-at-rest.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Applies only to Hyperledger Fabric.
Type: String
Required: No

 ** LogPublishingConfiguration **   <a name="ManagedBlockchain-Type-Node-LogPublishingConfiguration"></a>
Configuration properties for logging events associated with a peer node on a Hyperledger Fabric network on Managed Blockchain.
Type: [NodeLogPublishingConfiguration](API_NodeLogPublishingConfiguration.md) object
Required: No

 ** MemberId **   <a name="ManagedBlockchain-Type-Node-MemberId"></a>
The unique identifier of the member to which the node belongs.
Applies only to Hyperledger Fabric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** NetworkId **   <a name="ManagedBlockchain-Type-Node-NetworkId"></a>
The unique identifier of the network that the node is on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** StateDB **   <a name="ManagedBlockchain-Type-Node-StateDB"></a>
The state database that the node uses. Values are `LevelDB` or `CouchDB`.
Applies only to Hyperledger Fabric.
Type: String
Valid Values: `LevelDB | CouchDB`
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-Node-Status"></a>
The status of the node.
+  `CREATING` - The AWS account is in the process of creating a node.
+  `AVAILABLE` - The node has been created and can participate in the network.
+  `UNHEALTHY` - The node is impaired and might not function as expected. Amazon Managed Blockchain automatically finds nodes in this state and tries to recover them. If a node is recoverable, it returns to `AVAILABLE`. Otherwise, it moves to `FAILED` status.
+  `CREATE_FAILED` - The AWS account attempted to create a node and creation failed.
+  `UPDATING` - The node is in the process of being updated.
+  `DELETING` - The node is in the process of being deleted.
+  `DELETED` - The node can no longer participate on the network.
+  `FAILED` - The node is no longer functional, cannot be recovered, and must be deleted.
+  `INACCESSIBLE_ENCRYPTION_KEY` - The node is impaired and might not function as expected because it cannot access the specified customer managed key in AWS KMS for encryption at rest. Either the KMS key was disabled or deleted, or the grants on the key were revoked.

  The effect of disabling or deleting a key or of revoking a grant isn't immediate. It might take some time for the node resource to discover that the key is inaccessible. When a resource is in this state, we recommend deleting and recreating the resource.
Type: String
Valid Values: `CREATING | AVAILABLE | UNHEALTHY | CREATE_FAILED | UPDATING | DELETING | DELETED | FAILED | INACCESSIBLE_ENCRYPTION_KEY`
Required: No

 ** Tags **   <a name="ManagedBlockchain-Type-Node-Tags"></a>
Tags assigned to the node. Each tag consists of a key and optional value.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Node_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/Node)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/Node)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/Node)
