---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_Transaction.html
---

# Transaction
<a name="API_Transaction"></a>

There are two possible types of transactions used for this data type:
+ A Bitcoin transaction is a movement of BTC from one address to another.
+ An Ethereum transaction refers to an action initiated by an externally owned account, which is an account managed by a human, not a contract. For example, if Bob sends Alice 1 ETH, Bob's account must be debited and Alice's must be credited. This state-changing action occurs within a transaction.

## Contents
<a name="API_Transaction_Contents"></a>

 ** network **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-network"></a>
The blockchain network where the transaction occurred.
Type: String
Valid Values: `ETHEREUM_MAINNET | ETHEREUM_SEPOLIA_TESTNET | BITCOIN_MAINNET | BITCOIN_TESTNET`
Required: Yes

 ** numberOfTransactions **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-numberOfTransactions"></a>
The number of transactions in the block.
Type: Long
Required: Yes

 ** to **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-to"></a>
The identifier of the transaction. It is generated whenever a transaction is verified and added to the blockchain.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: Yes

 ** transactionHash **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-transactionHash"></a>
The hash of a transaction. It is generated when a transaction is created.
Type: String
Pattern: `(0x[A-Fa-f0-9]{64}|[A-Fa-f0-9]{64})`
Required: Yes

 ** transactionIndex **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-transactionIndex"></a>
The index of the transaction within a blockchain.
Type: Long
Required: Yes

 ** transactionTimestamp **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-transactionTimestamp"></a>
The `Timestamp` of the transaction.
Type: Timestamp
Required: Yes

 ** blockHash **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-blockHash"></a>
The block hash is a unique identifier for a block. It is a fixed-size string that is calculated by using the information in the block. The block hash is used to verify the integrity of the data in the block.
Type: String
Pattern: `(0x[A-Fa-f0-9]{64}|[A-Fa-f0-9]{64})`
Required: No

 ** blockNumber **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-blockNumber"></a>
The block number in which the transaction is recorded.
Type: String
Required: No

 ** confirmationStatus **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-confirmationStatus"></a>
Specifies whether the transaction has reached Finality.
Type: String
Valid Values: `FINAL | NONFINAL`
Required: No

 ** contractAddress **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-contractAddress"></a>
The blockchain address for the contract.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: No

 ** cumulativeGasUsed **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-cumulativeGasUsed"></a>
The amount of gas used up to the specified point in the block.
Type: String
Required: No

 ** effectiveGasPrice **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-effectiveGasPrice"></a>
The effective gas price.
Type: String
Required: No

 ** executionStatus **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-executionStatus"></a>
Identifies whether the transaction has succeeded or failed.
Type: String
Valid Values: `FAILED | SUCCEEDED`
Required: No

 ** from **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-from"></a>
The initiator of the transaction. It is either in the form a public key or a contract address.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: No

 ** gasUsed **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-gasUsed"></a>
The amount of gas used for the transaction.
Type: String
Required: No

 ** signatureR **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-signatureR"></a>
The signature of the transaction. The X coordinate of a point R.
Type: String
Required: No

 ** signatureS **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-signatureS"></a>
The signature of the transaction. The Y coordinate of a point S.
Type: String
Required: No

 ** signatureV **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-signatureV"></a>
The signature of the transaction. The Z coordinate of a point V.
Type: Integer
Required: No

 ** transactionFee **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-transactionFee"></a>
The transaction fee.
Type: String
Required: No

 ** transactionId **   <a name="ManagedBlockchainQueryAPIReference-Type-Transaction-transactionId"></a>
The identifier of a Bitcoin transaction. It is generated when a transaction is created.
Type: String
Required: No

## See Also
<a name="API_Transaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/Transaction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/Transaction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/Transaction)
