---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Member.html
---

# Member
<a name="API_Member"></a>

Member configuration properties.

Applies only to Hyperledger Fabric.

## Contents
<a name="API_Member_Contents"></a>

 ** Arn **   <a name="ManagedBlockchain-Type-Member-Arn"></a>
The Amazon Resource Name (ARN) of the member. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-Member-CreationDate"></a>
The date and time that the member was created.
Type: Timestamp
Required: No

 ** Description **   <a name="ManagedBlockchain-Type-Member-Description"></a>
An optional description for the member.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** FrameworkAttributes **   <a name="ManagedBlockchain-Type-Member-FrameworkAttributes"></a>
Attributes relevant to a member for the blockchain framework that the Managed Blockchain network uses.
Type: [MemberFrameworkAttributes](API_MemberFrameworkAttributes.md) object
Required: No

 ** Id **   <a name="ManagedBlockchain-Type-Member-Id"></a>
The unique identifier of the member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** KmsKeyArn **   <a name="ManagedBlockchain-Type-Member-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the customer managed key in AWS Key Management Service (AWS KMS) that the member uses for encryption at rest. If the value of this parameter is `"AWS Owned KMS Key"`, the member uses an AWS owned KMS key for encryption. This parameter is inherited by the nodes that this member owns.
For more information, see [Encryption at Rest](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-encryption-at-rest.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String
Required: No

 ** LogPublishingConfiguration **   <a name="ManagedBlockchain-Type-Member-LogPublishingConfiguration"></a>
Configuration properties for logging events associated with a member.
Type: [MemberLogPublishingConfiguration](API_MemberLogPublishingConfiguration.md) object
Required: No

 ** Name **   <a name="ManagedBlockchain-Type-Member-Name"></a>
The name of the member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!-|[0-9])(?!.*-$)(?!.*?--)[a-zA-Z0-9-]+$`
Required: No

 ** NetworkId **   <a name="ManagedBlockchain-Type-Member-NetworkId"></a>
The unique identifier of the network to which the member belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-Member-Status"></a>
The status of a member.
+  `CREATING` - The AWS account is in the process of creating a member.
+  `AVAILABLE` - The member has been created and can participate in the network.
+  `CREATE_FAILED` - The AWS account attempted to create a member and creation failed.
+  `UPDATING` - The member is in the process of being updated.
+  `DELETING` - The member and all associated resources are in the process of being deleted. Either the AWS account that owns the member deleted it, or the member is being deleted as the result of an `APPROVED` `PROPOSAL` to remove the member.
+  `DELETED` - The member can no longer participate on the network and all associated resources are deleted. Either the AWS account that owns the member deleted it, or the member is being deleted as the result of an `APPROVED` `PROPOSAL` to remove the member.
+  `INACCESSIBLE_ENCRYPTION_KEY` - The member is impaired and might not function as expected because it cannot access the specified customer managed key in AWS KMS for encryption at rest. Either the KMS key was disabled or deleted, or the grants on the key were revoked.

  The effect of disabling or deleting a key or of revoking a grant isn't immediate. It might take some time for the member resource to discover that the key is inaccessible. When a resource is in this state, we recommend deleting and recreating the resource.
Type: String
Valid Values: `CREATING | AVAILABLE | CREATE_FAILED | UPDATING | DELETING | DELETED | INACCESSIBLE_ENCRYPTION_KEY`
Required: No

 ** Tags **   <a name="ManagedBlockchain-Type-Member-Tags"></a>
Tags assigned to the member. Tags consist of a key and optional value.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Member_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/Member)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/Member)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/Member)
