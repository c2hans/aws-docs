---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Accessor.html
---

# Accessor
<a name="API_Accessor"></a>

The properties of the Accessor.

## Contents
<a name="API_Accessor_Contents"></a>

 ** Arn **   <a name="ManagedBlockchain-Type-Accessor-Arn"></a>
The Amazon Resource Name (ARN) of the accessor. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** BillingToken **   <a name="ManagedBlockchain-Type-Accessor-BillingToken"></a>
The billing token is a property of the Accessor. Use this token to when making calls to the blockchain network. The billing token is used to track your accessor token for billing requests.
Type: String
Length Constraints: Fixed length of 42.
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-Accessor-CreationDate"></a>
The creation date and time of the accessor.
Type: Timestamp
Required: No

 ** Id **   <a name="ManagedBlockchain-Type-Accessor-Id"></a>
The unique identifier of the accessor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** NetworkType **   <a name="ManagedBlockchain-Type-Accessor-NetworkType"></a>
The blockchain network that the Accessor token is created for.
Type: String
Valid Values: `ETHEREUM_GOERLI | ETHEREUM_MAINNET | ETHEREUM_MAINNET_AND_GOERLI | POLYGON_MAINNET | POLYGON_MUMBAI`
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-Accessor-Status"></a>
The current status of the accessor.
Type: String
Valid Values: `AVAILABLE | PENDING_DELETION | DELETED`
Required: No

 ** Tags **   <a name="ManagedBlockchain-Type-Accessor-Tags"></a>
The tags assigned to the Accessor.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** Type **   <a name="ManagedBlockchain-Type-Accessor-Type"></a>
The type of the accessor.
Currently, accessor type is restricted to `BILLING_TOKEN`.
Type: String
Valid Values: `BILLING_TOKEN`
Required: No

## See Also
<a name="API_Accessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/Accessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/Accessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/Accessor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
