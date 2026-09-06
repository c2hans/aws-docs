---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Network.html
---

# Network
<a name="API_Network"></a>

Network configuration properties.

## Contents
<a name="API_Network_Contents"></a>

 ** Arn **   <a name="ManagedBlockchain-Type-Network-Arn"></a>
The Amazon Resource Name (ARN) of the network. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-Network-CreationDate"></a>
The date and time that the network was created.
Type: Timestamp
Required: No

 ** Description **   <a name="ManagedBlockchain-Type-Network-Description"></a>
Attributes of the blockchain framework for the network.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** Framework **   <a name="ManagedBlockchain-Type-Network-Framework"></a>
The blockchain framework that the network uses.
Type: String
Valid Values: `HYPERLEDGER_FABRIC | ETHEREUM`
Required: No

 ** FrameworkAttributes **   <a name="ManagedBlockchain-Type-Network-FrameworkAttributes"></a>
Attributes of the blockchain framework that the network uses.
Type: [NetworkFrameworkAttributes](API_NetworkFrameworkAttributes.md) object
Required: No

 ** FrameworkVersion **   <a name="ManagedBlockchain-Type-Network-FrameworkVersion"></a>
The version of the blockchain framework that the network uses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Required: No

 ** Id **   <a name="ManagedBlockchain-Type-Network-Id"></a>
The unique identifier of the network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** Name **   <a name="ManagedBlockchain-Type-Network-Name"></a>
The name of the network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-Network-Status"></a>
The current status of the network.
Type: String
Valid Values: `CREATING | AVAILABLE | CREATE_FAILED | DELETING | DELETED`
Required: No

 ** Tags **   <a name="ManagedBlockchain-Type-Network-Tags"></a>
Tags assigned to the network. Each tag consists of a key and optional value.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** VotingPolicy **   <a name="ManagedBlockchain-Type-Network-VotingPolicy"></a>
The voting rules that the network uses to decide if a proposal is accepted.
Type: [VotingPolicy](API_VotingPolicy.md) object
Required: No

 ** VpcEndpointServiceName **   <a name="ManagedBlockchain-Type-Network-VpcEndpointServiceName"></a>
The VPC endpoint service name of the VPC endpoint service of the network. Members use the VPC endpoint service name to create a VPC endpoint to access network resources.
Type: String
Required: No

## See Also
<a name="API_Network_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/Network)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/Network)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/Network)
