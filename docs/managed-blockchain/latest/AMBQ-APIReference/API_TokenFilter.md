---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TokenFilter.html
---

# TokenFilter
<a name="API_TokenFilter"></a>

The container of the token filter like the contract address on a given blockchain network or a unique token identifier on a given blockchain network.

**Note**
You must always specify the network property of this container when using this operation.

## Contents
<a name="API_TokenFilter_Contents"></a>

 ** network **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenFilter-network"></a>
The blockchain network of the token.
Type: String
Valid Values: `ETHEREUM_MAINNET | ETHEREUM_SEPOLIA_TESTNET | BITCOIN_MAINNET | BITCOIN_TESTNET`
Required: Yes

 ** contractAddress **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenFilter-contractAddress"></a>
This is the address of the contract.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: No

 ** tokenId **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenFilter-tokenId"></a>
The unique identifier of the token.
Type: String
Pattern: `[a-zA-Z0-9]{1,66}`
Required: No

## See Also
<a name="API_TokenFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/TokenFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/TokenFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/TokenFilter)
