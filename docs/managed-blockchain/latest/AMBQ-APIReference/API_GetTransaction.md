---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_GetTransaction.html
---

# GetTransaction
<a name="API_GetTransaction"></a>

Gets the details of a transaction.

**Note**
This action will return transaction details for all transactions that are *confirmed* on the blockchain, even if they have not reached [finality](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality).

## Request Syntax
<a name="API_GetTransaction_RequestSyntax"></a>

```
POST /get-transaction HTTP/1.1
Content-type: application/json

{
   "network": "{{string}}",
   "transactionHash": "{{string}}",
   "transactionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetTransaction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTransaction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [network](#API_GetTransaction_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTransaction-request-network"></a>
The blockchain network where the transaction occurred.
Type: String
Valid Values: `ETHEREUM_MAINNET | ETHEREUM_SEPOLIA_TESTNET | BITCOIN_MAINNET | BITCOIN_TESTNET`
Required: Yes

 ** [transactionHash](#API_GetTransaction_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTransaction-request-transactionHash"></a>
The hash of a transaction. It is generated when a transaction is created.
Type: String
Pattern: `(0x[A-Fa-f0-9]{64}|[A-Fa-f0-9]{64})`
Required: No

 ** [transactionId](#API_GetTransaction_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTransaction-request-transactionId"></a>
The identifier of a Bitcoin transaction. It is generated when a transaction is created.
 `transactionId` is only supported on the Bitcoin networks.
Type: String
Pattern: `(0x[A-Fa-f0-9]{64}|[A-Fa-f0-9]{64})`
Required: No

## Response Syntax
<a name="API_GetTransaction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "transaction": {
      "blockHash": "string",
      "blockNumber": "string",
      "confirmationStatus": "string",
      "contractAddress": "string",
      "cumulativeGasUsed": "string",
      "effectiveGasPrice": "string",
      "executionStatus": "string",
      "from": "string",
      "gasUsed": "string",
      "network": "string",
      "numberOfTransactions": number,
      "signatureR": "string",
      "signatureS": "string",
      "signatureV": number,
      "to": "string",
      "transactionFee": "string",
      "transactionHash": "string",
      "transactionId": "string",
      "transactionIndex": number,
      "transactionTimestamp": number
   }
}
```

## Response Elements
<a name="API_GetTransaction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [transaction](#API_GetTransaction_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTransaction-response-transaction"></a>
Contains the details of the transaction.
Type: [Transaction](API_Transaction.md) object

## Errors
<a name="API_GetTransaction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
The AWS account doesn’t have access to this resource.
 ** message **
The container for the exception message.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The request processing has failed because of an internal error in the service.
 ** message **
The container for the exception message.
 ** retryAfterSeconds **
Specifies the `retryAfterSeconds` value.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The resource was not found.
 ** message **
The container for the exception message.
 ** resourceId **
The `resourceId` of the resource that caused the exception.
 ** resourceType **
The `resourceType` of the resource that caused the exception.
HTTP Status Code: 404

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The service quota has been exceeded for this resource.
 ** message **
The container for the exception message.
 ** quotaCode **
The container for the `quotaCode`.
 ** resourceId **
The `resourceId` of the resource that caused the exception.
 ** resourceType **
The `resourceType` of the resource that caused the exception.
 ** serviceCode **
The container for the `serviceCode`.
HTTP Status Code: 402

 [ThrottlingException](API_ThrottlingException.md)
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.
 ** message **
The container for the exception message.
 ** quotaCode **
The container for the `quotaCode`.
 ** retryAfterSeconds **
The container of the `retryAfterSeconds` value.
 ** serviceCode **
The container for the `serviceCode`.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The resource passed is invalid.
 ** fieldList **
The container for the `fieldList` of the exception.
 ** message **
The container for the exception message.
 ** reason **
The container for the reason for the exception
HTTP Status Code: 400

## See Also
<a name="API_GetTransaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-query-2023-05-04/GetTransaction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-query-2023-05-04/GetTransaction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/GetTransaction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-query-2023-05-04/GetTransaction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/GetTransaction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-query-2023-05-04/GetTransaction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-query-2023-05-04/GetTransaction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-query-2023-05-04/GetTransaction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/managedblockchain-query-2023-05-04/GetTransaction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/GetTransaction)
