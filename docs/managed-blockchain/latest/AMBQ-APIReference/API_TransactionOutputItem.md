---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TransactionOutputItem.html
---

# TransactionOutputItem
<a name="API_TransactionOutputItem"></a>

The container of the transaction output.

## Contents
<a name="API_TransactionOutputItem_Contents"></a>

 ** network **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionOutputItem-network"></a>
The blockchain network where the transaction occurred.
Type: String
Valid Values: `ETHEREUM_MAINNET | ETHEREUM_SEPOLIA_TESTNET | BITCOIN_MAINNET | BITCOIN_TESTNET`
Required: Yes

 ** transactionHash **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionOutputItem-transactionHash"></a>
The hash of a transaction. It is generated when a transaction is created.
Type: String
Pattern: `(0x[A-Fa-f0-9]{64}|[A-Fa-f0-9]{64})`
Required: Yes

 ** transactionTimestamp **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionOutputItem-transactionTimestamp"></a>
The time when the transaction occurred.
Type: Timestamp
Required: Yes

 ** confirmationStatus **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionOutputItem-confirmationStatus"></a>
Specifies whether to list transactions that have not reached Finality.
Type: String
Valid Values: `FINAL | NONFINAL`
Required: No

 ** transactionId **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionOutputItem-transactionId"></a>
The identifier of a Bitcoin transaction. It is generated when a transaction is created.
Type: String
Pattern: `(0x[A-Fa-f0-9]{64}|[A-Fa-f0-9]{64})`
Required: No

## See Also
<a name="API_TransactionOutputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/TransactionOutputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/TransactionOutputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/TransactionOutputItem)
