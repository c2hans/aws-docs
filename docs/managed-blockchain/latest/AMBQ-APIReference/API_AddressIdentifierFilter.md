---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_AddressIdentifierFilter.html
---

# AddressIdentifierFilter
<a name="API_AddressIdentifierFilter"></a>

This is the container for the unique public address on the blockchain.

## Contents
<a name="API_AddressIdentifierFilter_Contents"></a>

 ** transactionEventToAddress **   <a name="ManagedBlockchainQueryAPIReference-Type-AddressIdentifierFilter-transactionEventToAddress"></a>
The container for the recipient address of the transaction.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[-A-Za-z0-9]{13,74}`
Required: Yes

## See Also
<a name="API_AddressIdentifierFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/AddressIdentifierFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/AddressIdentifierFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/AddressIdentifierFilter)
