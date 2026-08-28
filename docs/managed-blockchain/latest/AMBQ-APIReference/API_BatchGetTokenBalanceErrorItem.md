---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_BatchGetTokenBalanceErrorItem.html
---

# BatchGetTokenBalanceErrorItem
<a name="API_BatchGetTokenBalanceErrorItem"></a>

Error generated from a failed `BatchGetTokenBalance` request.

## Contents
<a name="API_BatchGetTokenBalanceErrorItem_Contents"></a>

 ** errorCode **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceErrorItem-errorCode"></a>
The error code associated with the error.
Type: String
Required: Yes

 ** errorMessage **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceErrorItem-errorMessage"></a>
The message associated with the error.
Type: String
Required: Yes

 ** errorType **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceErrorItem-errorType"></a>
The type of error.
Type: String
Valid Values: `VALIDATION_EXCEPTION | RESOURCE_NOT_FOUND_EXCEPTION`
Required: Yes

 ** atBlockchainInstant **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceErrorItem-atBlockchainInstant"></a>
The container for time.
Type: [BlockchainInstant](API_BlockchainInstant.md) object
Required: No

 ** ownerIdentifier **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceErrorItem-ownerIdentifier"></a>
The container for the owner identifier.
Type: [OwnerIdentifier](API_OwnerIdentifier.md) object
Required: No

 ** tokenIdentifier **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceErrorItem-tokenIdentifier"></a>
The container for the identifier for the token including the unique token ID and its blockchain network.
Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.
Type: [TokenIdentifier](API_TokenIdentifier.md) object
Required: No

## See Also
<a name="API_BatchGetTokenBalanceErrorItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/BatchGetTokenBalanceErrorItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/BatchGetTokenBalanceErrorItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/BatchGetTokenBalanceErrorItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
