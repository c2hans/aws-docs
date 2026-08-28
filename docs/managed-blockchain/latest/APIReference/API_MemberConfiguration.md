---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberConfiguration.html
---

# MemberConfiguration
<a name="API_MemberConfiguration"></a>

Configuration properties of the member.

Applies only to Hyperledger Fabric.

## Contents
<a name="API_MemberConfiguration_Contents"></a>

 ** FrameworkConfiguration **   <a name="ManagedBlockchain-Type-MemberConfiguration-FrameworkConfiguration"></a>
Configuration properties of the blockchain framework relevant to the member.
Type: [MemberFrameworkConfiguration](API_MemberFrameworkConfiguration.md) object
Required: Yes

 ** Name **   <a name="ManagedBlockchain-Type-MemberConfiguration-Name"></a>
The name of the member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!-|[0-9])(?!.*-$)(?!.*?--)[a-zA-Z0-9-]+$`
Required: Yes

 ** Description **   <a name="ManagedBlockchain-Type-MemberConfiguration-Description"></a>
An optional description of the member.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** KmsKeyArn **   <a name="ManagedBlockchain-Type-MemberConfiguration-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the customer managed key in AWS Key Management Service (AWS KMS) to use for encryption at rest in the member. This parameter is inherited by any nodes that this member creates. For more information, see [Encryption at Rest](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-encryption-at-rest.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Use one of the following options to specify this parameter:
+  **Undefined or empty string** - By default, use an AWS KMS key that is owned and managed by AWS on your behalf.
+  **A valid symmetric customer managed KMS key** - Use the specified KMS key in your account that you create, own, and manage.

  Amazon Managed Blockchain doesn't support asymmetric keys. For more information, see [Using symmetric and asymmetric keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the * AWS Key Management Service Developer Guide*.

  The following is an example of a KMS key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** LogPublishingConfiguration **   <a name="ManagedBlockchain-Type-MemberConfiguration-LogPublishingConfiguration"></a>
Configuration properties for logging events associated with a member of a Managed Blockchain network.
Type: [MemberLogPublishingConfiguration](API_MemberLogPublishingConfiguration.md) object
Required: No

 ** Tags **   <a name="ManagedBlockchain-Type-MemberConfiguration-Tags"></a>
Tags assigned to the member. Tags consist of a key and optional value.
When specifying tags during creation, you can specify multiple key-value pairs in a single request, with an overall maximum of 50 tags added to each resource.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_MemberConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/MemberConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/MemberConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/MemberConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
