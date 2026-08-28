---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListFilteredTransactionEvents.html
---

# ListFilteredTransactionEvents
<a name="API_ListFilteredTransactionEvents"></a>

Lists all the transaction events for an address on the blockchain.

**Note**
This operation is only supported on the Bitcoin networks.

## Request Syntax
<a name="API_ListFilteredTransactionEvents_RequestSyntax"></a>

```
POST /list-filtered-transaction-events HTTP/1.1
Content-type: application/json

{
   "addressIdentifierFilter": {
      "transactionEventToAddress": [ "{{string}}" ]
   },
   "confirmationStatusFilter": {
      "include": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "network": "{{string}}",
   "nextToken": "{{string}}",
   "sort": {
      "sortBy": "{{string}}",
      "sortOrder": "{{string}}"
   },
   "timeFilter": {
      "from": {
         "time": {{number}}
      },
      "to": {
         "time": {{number}}
      }
   },
   "voutFilter": {
      "voutSpent": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_ListFilteredTransactionEvents_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListFilteredTransactionEvents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [addressIdentifierFilter](#API_ListFilteredTransactionEvents_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListFilteredTransactionEvents-request-addressIdentifierFilter"></a>
This is the unique public address on the blockchain for which the transaction events are being requested.
Type: [AddressIdentifierFilter](API_AddressIdentifierFilter.md) object
Required: Yes

 ** [confirmationStatusFilter](#API_ListFilteredTransactionEvents_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListFilteredTransactionEvents-request-confirmationStatusFilter"></a>
The container for the `ConfirmationStatusFilter` that filters for the [*finality*](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality) of the results.
Type: [ConfirmationStatusFilter](API_ConfirmationStatusFilter.md) object
Required: No

 ** [maxResults](#API_ListFilteredTransactionEvents_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListFilteredTransactionEvents-request-maxResults"></a>
The maximum number of transaction events to list.
Default: `100`
Even if additional results can be retrieved, the request can return less results than `maxResults` or an empty array of results.
To retrieve the next set of results, make another request with the returned `nextToken` value. The value of `nextToken` is `null` when there are no more results to return
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 250.
Required: No

 ** [network](#API_ListFilteredTransactionEvents_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListFilteredTransactionEvents-request-network"></a>
The blockchain network where the transaction occurred.
Valid Values: `BITCOIN_MAINNET` \| `BITCOIN_TESTNET`
Type: String
Required: Yes

 ** [nextToken](#API_ListFilteredTransactionEvents_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListFilteredTransactionEvents-request-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131070.
Required: No

 ** [sort](#API_ListFilteredTransactionEvents_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListFilteredTransactionEvents-request-sort"></a>
The order by which the results will be sorted.
Type: [ListFilteredTransactionEventsSort](API_ListFilteredTransactionEventsSort.md) object
Required: No

 ** [timeFilter](#API_ListFilteredTransactionEvents_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListFilteredTransactionEvents-request-timeFilter"></a>
This container specifies the time frame for the transaction events returned in the response.
Type: [TimeFilter](API_TimeFilter.md) object
Required: No

 ** [voutFilter](#API_ListFilteredTransactionEvents_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListFilteredTransactionEvents-request-voutFilter"></a>
This container specifies filtering attributes related to BITCOIN\_VOUT event types
Type: [VoutFilter](API_VoutFilter.md) object
Required: No

## Response Syntax
<a name="API_ListFilteredTransactionEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "events": [
      {
         "blockchainInstant": {
            "time": number
         },
         "confirmationStatus": "string",
         "contractAddress": "string",
         "eventType": "string",
         "from": "string",
         "network": "string",
         "spentVoutIndex": number,
         "spentVoutTransactionHash": "string",
         "spentVoutTransactionId": "string",
         "to": "string",
         "tokenId": "string",
         "transactionHash": "string",
         "transactionId": "string",
         "value": "string",
         "voutIndex": number,
         "voutSpent": boolean
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListFilteredTransactionEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_ListFilteredTransactionEvents_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListFilteredTransactionEvents-response-events"></a>
The transaction events returned by the request.
Type: Array of [TransactionEvent](API_TransactionEvent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 250 items.

 ** [nextToken](#API_ListFilteredTransactionEvents_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListFilteredTransactionEvents-response-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131070.

## Errors
<a name="API_ListFilteredTransactionEvents_Errors"></a>

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
<a name="API_ListFilteredTransactionEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-query-2023-05-04/ListFilteredTransactionEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-query-2023-05-04/ListFilteredTransactionEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/ListFilteredTransactionEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-query-2023-05-04/ListFilteredTransactionEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/ListFilteredTransactionEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-query-2023-05-04/ListFilteredTransactionEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-query-2023-05-04/ListFilteredTransactionEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-query-2023-05-04/ListFilteredTransactionEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-query-2023-05-04/ListFilteredTransactionEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ListFilteredTransactionEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
