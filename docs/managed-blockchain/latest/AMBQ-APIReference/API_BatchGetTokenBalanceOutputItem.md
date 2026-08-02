---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_BatchGetTokenBalanceOutputItem.html
---

# BatchGetTokenBalanceOutputItem
<a name="API_BatchGetTokenBalanceOutputItem"></a>

The container for the properties of a token balance output.

## Contents
<a name="API_BatchGetTokenBalanceOutputItem_Contents"></a>

 ** atBlockchainInstant **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceOutputItem-atBlockchainInstant"></a>
The container for time.
Type: [BlockchainInstant](API_BlockchainInstant.md) object
Required: Yes

 ** balance **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceOutputItem-balance"></a>
The container for the token balance.
Type: String
Required: Yes

 ** lastUpdatedTime **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceOutputItem-lastUpdatedTime"></a>
The container for time.
Type: [BlockchainInstant](API_BlockchainInstant.md) object
Required: No

 ** ownerIdentifier **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceOutputItem-ownerIdentifier"></a>
The container for the owner identifier.
Type: [OwnerIdentifier](API_OwnerIdentifier.md) object
Required: No

 ** tokenIdentifier **   <a name="ManagedBlockchainQueryAPIReference-Type-BatchGetTokenBalanceOutputItem-tokenIdentifier"></a>
The container for the identifier for the token including the unique token ID and its blockchain network.
Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.
Type: [TokenIdentifier](API_TokenIdentifier.md) object
Required: No

## See Also
<a name="API_BatchGetTokenBalanceOutputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/BatchGetTokenBalanceOutputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/BatchGetTokenBalanceOutputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/BatchGetTokenBalanceOutputItem)
