---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_AssetContract.html
---

# AssetContract
<a name="API_AssetContract"></a>

This container contains information about an contract.

## Contents
<a name="API_AssetContract_Contents"></a>

 ** contractIdentifier **   <a name="ManagedBlockchainQueryAPIReference-Type-AssetContract-contractIdentifier"></a>
The container for the contract identifier containing its blockchain network and address.
Type: [ContractIdentifier](API_ContractIdentifier.md) object
Required: Yes

 ** deployerAddress **   <a name="ManagedBlockchainQueryAPIReference-Type-AssetContract-deployerAddress"></a>
The address of the contract deployer.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: Yes

 ** tokenStandard **   <a name="ManagedBlockchainQueryAPIReference-Type-AssetContract-tokenStandard"></a>
The token standard of the contract.
Type: String
Valid Values: `ERC20 | ERC721 | ERC1155`
Required: Yes

## See Also
<a name="API_AssetContract_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/AssetContract)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/AssetContract)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/AssetContract)
