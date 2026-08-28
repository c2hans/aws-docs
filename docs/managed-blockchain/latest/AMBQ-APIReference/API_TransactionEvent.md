---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TransactionEvent.html
---

# TransactionEvent
<a name="API_TransactionEvent"></a>

The container for the properties of a transaction event.

## Contents
<a name="API_TransactionEvent_Contents"></a>

 ** eventType **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-eventType"></a>
The type of transaction event.
Type: String
Valid Values: `ERC20_TRANSFER | ERC20_MINT | ERC20_BURN | ERC20_DEPOSIT | ERC20_WITHDRAWAL | ERC721_TRANSFER | ERC1155_TRANSFER | BITCOIN_VIN | BITCOIN_VOUT | INTERNAL_ETH_TRANSFER | ETH_TRANSFER`
Required: Yes

 ** network **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-network"></a>
The blockchain network where the transaction occurred.
Type: String
Valid Values: `ETHEREUM_MAINNET | ETHEREUM_SEPOLIA_TESTNET | BITCOIN_MAINNET | BITCOIN_TESTNET`
Required: Yes

 ** transactionHash **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-transactionHash"></a>
The hash of a transaction. It is generated when a transaction is created.
Type: String
Pattern: `(0x[A-Fa-f0-9]{64}|[A-Fa-f0-9]{64})`
Required: Yes

 ** blockchainInstant **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-blockchainInstant"></a>
The container for time.
Type: [BlockchainInstant](API_BlockchainInstant.md) object
Required: No

 ** confirmationStatus **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-confirmationStatus"></a>
This container specifies whether the transaction has reached Finality.
Type: String
Valid Values: `FINAL | NONFINAL`
Required: No

 ** contractAddress **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-contractAddress"></a>
The blockchain address for the contract
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: No

 ** from **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-from"></a>
The wallet address initiating the transaction. It can either be a public key or a contract.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: No

 ** spentVoutIndex **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-spentVoutIndex"></a>
The position of the spent transaction output in the output list of the *creating transaction*.
This is only returned for `BITCOIN_VIN` event types.
Type: Integer
Required: No

 ** spentVoutTransactionHash **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-spentVoutTransactionHash"></a>
The transactionHash that *created* the spent transaction output.
This is only returned for `BITCOIN_VIN` event types.
Type: String
Required: No

 ** spentVoutTransactionId **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-spentVoutTransactionId"></a>
The transactionId that *created* the spent transaction output.
This is only returned for `BITCOIN_VIN` event types.
Type: String
Required: No

 ** to **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-to"></a>
The wallet address receiving the transaction. It can either be a public key or a contract.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: No

 ** tokenId **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-tokenId"></a>
The unique identifier for the token involved in the transaction.
Type: String
Pattern: `[a-zA-Z0-9]{1,66}`
Required: No

 ** transactionId **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-transactionId"></a>
The identifier of a Bitcoin transaction. It is generated when a transaction is created.
Type: String
Required: No

 ** value **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-value"></a>
The value that was transacted.
Type: String
Required: No

 ** voutIndex **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-voutIndex"></a>
The position of the transaction output in the transaction output list.
Type: Integer
Required: No

 ** voutSpent **   <a name="ManagedBlockchainQueryAPIReference-Type-TransactionEvent-voutSpent"></a>
Specifies if the transaction output is spent or unspent. This is only returned for BITCOIN\_VOUT event types.
This is only returned for `BITCOIN_VOUT` event types.
Type: Boolean
Required: No

## See Also
<a name="API_TransactionEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/TransactionEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/TransactionEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/TransactionEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
