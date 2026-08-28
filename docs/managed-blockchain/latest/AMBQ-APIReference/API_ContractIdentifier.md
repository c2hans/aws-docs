---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ContractIdentifier.html
---

# ContractIdentifier
<a name="API_ContractIdentifier"></a>

Container for the blockchain address and network information about a contract.

## Contents
<a name="API_ContractIdentifier_Contents"></a>

 ** contractAddress **   <a name="ManagedBlockchainQueryAPIReference-Type-ContractIdentifier-contractAddress"></a>
Container for the blockchain address about a contract.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: Yes

 ** network **   <a name="ManagedBlockchainQueryAPIReference-Type-ContractIdentifier-network"></a>
The blockchain network of the contract.
Type: String
Valid Values: `ETHEREUM_MAINNET | ETHEREUM_SEPOLIA_TESTNET | BITCOIN_MAINNET | BITCOIN_TESTNET`
Required: Yes

## See Also
<a name="API_ContractIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/ContractIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/ContractIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ContractIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
