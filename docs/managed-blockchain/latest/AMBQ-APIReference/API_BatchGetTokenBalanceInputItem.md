---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_BatchGetTokenBalanceInputItem.html
---

# BatchGetTokenBalanceInputItem
<a name="API_BatchGetTokenBalanceInputItem"></a>

The container for the input for getting a token balance.

## Contents
<a name="API_BatchGetTokenBalanceInputItem_Contents"></a>

 ** ownerIdentifier **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceInputItem-ownerIdentifier"></a>
The container for the owner identifier.
Type: [OwnerIdentifier](API_OwnerIdentifier.md) object
Required: Yes

 ** tokenIdentifier **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceInputItem-tokenIdentifier"></a>
The container for the identifier for the token including the unique token ID and its blockchain network.
Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.
Type: [TokenIdentifier](API_TokenIdentifier.md) object
Required: Yes

 ** atBlockchainInstant **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceInputItem-atBlockchainInstant"></a>
The container for time.
Type: [BlockchainInstant](API_BlockchainInstant.md) object
Required: No

## See Also
<a name="API_BatchGetTokenBalanceInputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/BatchGetTokenBalanceInputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/BatchGetTokenBalanceInputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/BatchGetTokenBalanceInputItem)
