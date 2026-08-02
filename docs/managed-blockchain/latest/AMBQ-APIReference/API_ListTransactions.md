---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTransactions.html
---

# ListTransactions
<a name="API_ListTransactions"></a>

Lists all the transaction events for a transaction.

## Request Syntax
<a name="API_ListTransactions_RequestSyntax"></a>

```
POST /list-transactions HTTP/1.1
Content-type: application/json

{
   "address": "{{string}}",
   "confirmationStatusFilter": {
      "include": [ "{{string}}" ]
   },
   "fromBlockchainInstant": {
      "time": {{number}}
   },
   "maxResults": {{number}},
   "network": "{{string}}",
   "nextToken": "{{string}}",
   "sort": {
      "sortBy": "{{string}}",
      "sortOrder": "{{string}}"
   },
   "toBlockchainInstant": {
      "time": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_ListTransactions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTransactions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [address](#API_ListTransactions_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTransactions-request-address"></a>
The address (either a contract or wallet), whose transactions are being requested.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`
Required: Yes

 ** [confirmationStatusFilter](#API_ListTransactions_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTransactions-request-confirmationStatusFilter"></a>
This filter is used to include transactions in the response that haven't reached [https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality). Transactions that have reached finality are always part of the response.
Type: [ConfirmationStatusFilter](API_ConfirmationStatusFilter.md) object
Required: No

 ** [fromBlockchainInstant](#API_ListTransactions_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTransactions-request-fromBlockchainInstant"></a>
The container for time.
Type: [BlockchainInstant](API_BlockchainInstant.md) object
Required: No

 ** [maxResults](#API_ListTransactions_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTransactions-request-maxResults"></a>
The maximum number of transactions to list.
Default: `100`
Even if additional results can be retrieved, the request can return less results than `maxResults` or an empty array of results.
To retrieve the next set of results, make another request with the returned `nextToken` value. The value of `nextToken` is `null` when there are no more results to return
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 250.
Required: No

 ** [network](#API_ListTransactions_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTransactions-request-network"></a>
The blockchain network where the transactions occurred.
Type: String
Valid Values: `ETHEREUM_MAINNET | ETHEREUM_SEPOLIA_TESTNET | BITCOIN_MAINNET | BITCOIN_TESTNET`
Required: Yes

 ** [nextToken](#API_ListTransactions_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTransactions-request-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131070.
Required: No

 ** [sort](#API_ListTransactions_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTransactions-request-sort"></a>
The order by which the results will be sorted.
Type: [ListTransactionsSort](API_ListTransactionsSort.md) object
Required: No

 ** [toBlockchainInstant](#API_ListTransactions_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTransactions-request-toBlockchainInstant"></a>
The container for time.
Type: [BlockchainInstant](API_BlockchainInstant.md) object
Required: No

## Response Syntax
<a name="API_ListTransactions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "transactions": [
      {
         "confirmationStatus": "string",
         "network": "string",
         "transactionHash": "string",
         "transactionId": "string",
         "transactionTimestamp": number
      }
   ]
}
```

## Response Elements
<a name="API_ListTransactions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTransactions_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTransactions-response-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131070.

 ** [transactions](#API_ListTransactions_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTransactions-response-transactions"></a>
The array of transactions returned by the request.
Type: Array of [TransactionOutputItem](API_TransactionOutputItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 250 items.

## Errors
<a name="API_ListTransactions_Errors"></a>

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
<a name="API_ListTransactions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-query-2023-05-04/ListTransactions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-query-2023-05-04/ListTransactions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/ListTransactions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-query-2023-05-04/ListTransactions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/ListTransactions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-query-2023-05-04/ListTransactions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-query-2023-05-04/ListTransactions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-query-2023-05-04/ListTransactions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-query-2023-05-04/ListTransactions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ListTransactions)
