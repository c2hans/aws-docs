---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ContractFilter.html
---

# ContractFilter
<a name="API_ContractFilter"></a>

The contract or wallet address by which to filter the request.

## Contents
<a name="API_ContractFilter_Contents"></a>

 ** deployerAddress **   <a name="ManagedBlockchainQueryAPIReference-Type-ContractFilter-deployerAddress"></a>
The network address of the deployer.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: Yes

 ** network **   <a name="ManagedBlockchainQueryAPIReference-Type-ContractFilter-network"></a>
The blockchain network of the contract.
Type: String
Valid Values: `ETHEREUM_MAINNET | ETHEREUM_SEPOLIA_TESTNET | BITCOIN_MAINNET | BITCOIN_TESTNET`
Required: Yes

 ** tokenStandard **   <a name="ManagedBlockchainQueryAPIReference-Type-ContractFilter-tokenStandard"></a>
The container for the token standard.
Type: String
Valid Values: `ERC20 | ERC721 | ERC1155`
Required: Yes

## See Also
<a name="API_ContractFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/ContractFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/ContractFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ContractFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
