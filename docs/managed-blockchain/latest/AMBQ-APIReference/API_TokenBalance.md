---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TokenBalance.html
---

# TokenBalance
<a name="API_TokenBalance"></a>

The balance of the token.

## Contents
<a name="API_TokenBalance_Contents"></a>

 ** atBlockchainInstant **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenBalance-atBlockchainInstant"></a>
The time for when the TokenBalance is requested or the current time if a time is not provided in the request.
This time will only be recorded up to the second.
Type: [BlockchainInstant](API_BlockchainInstant.md) object
Required: Yes

 ** balance **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenBalance-balance"></a>
The container of the token balance.
Type: String
Required: Yes

 ** lastUpdatedTime **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenBalance-lastUpdatedTime"></a>
The `Timestamp` of the last transaction at which the balance for the token in the wallet was updated.
Type: [BlockchainInstant](API_BlockchainInstant.md) object
Required: No

 ** ownerIdentifier **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenBalance-ownerIdentifier"></a>
The container for the identifier of the owner.
Type: [OwnerIdentifier](API_OwnerIdentifier.md) object
Required: No

 ** tokenIdentifier **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenBalance-tokenIdentifier"></a>
The identifier for the token, including the unique token ID and its blockchain network.
Type: [TokenIdentifier](API_TokenIdentifier.md) object
Required: No

## See Also
<a name="API_TokenBalance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/TokenBalance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/TokenBalance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/TokenBalance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
