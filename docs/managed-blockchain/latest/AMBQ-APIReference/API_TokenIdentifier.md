---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TokenIdentifier.html
---

# TokenIdentifier
<a name="API_TokenIdentifier"></a>

The container for the identifier for the token including the unique token ID and its blockchain network.

**Note**
Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.

## Contents
<a name="API_TokenIdentifier_Contents"></a>

 ** network **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenIdentifier-network"></a>
The blockchain network of the token.
Type: String
Valid Values: `ETHEREUM_MAINNET | ETHEREUM_SEPOLIA_TESTNET | BITCOIN_MAINNET | BITCOIN_TESTNET`
Required: Yes

 ** contractAddress **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenIdentifier-contractAddress"></a>
This is the token's contract address.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: No

 ** tokenId **   <a name="ManagedBlockchainQueryAPIReference-Type-TokenIdentifier-tokenId"></a>
The unique identifier of the token.
For native tokens, use the 3 character abbreviation that best matches your token. For example, btc for Bitcoin, eth for Ether, etc. For all other token types you must specify the `tokenId` in the 64 character hexadecimal `tokenid` format.
Type: String
Pattern: `[a-zA-Z0-9]{1,66}`
Required: No

## See Also
<a name="API_TokenIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/TokenIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/TokenIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/TokenIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
