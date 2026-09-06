---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_BatchGetTokenBalance.html
---

# BatchGetTokenBalance
<a name="API_BatchGetTokenBalance"></a>

Gets the token balance for a batch of tokens by using the `BatchGetTokenBalance` action for every token in the request.

**Note**
Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.

## Request Syntax
<a name="API_BatchGetTokenBalance_RequestSyntax"></a>

```
POST /batch-get-token-balance HTTP/1.1
Content-type: application/json

{
   "getTokenBalanceInputs": [
      {
         "atBlockchainInstant": {
            "time": {{number}}
         },
         "ownerIdentifier": {
            "address": "{{string}}"
         },
         "tokenIdentifier": {
            "contractAddress": "{{string}}",
            "network": "{{string}}",
            "tokenId": "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchGetTokenBalance_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetTokenBalance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [getTokenBalanceInputs](#API_BatchGetTokenBalance_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-BatchGetTokenBalance-request-getTokenBalanceInputs"></a>
An array of `BatchGetTokenBalanceInputItem` objects whose balance is being requested.
Type: Array of [BatchGetTokenBalanceInputItem](API_BatchGetTokenBalanceInputItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## Response Syntax
<a name="API_BatchGetTokenBalance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "atBlockchainInstant": {
            "time": number
         },
         "errorCode": "string",
         "errorMessage": "string",
         "errorType": "string",
         "ownerIdentifier": {
            "address": "string"
         },
         "tokenIdentifier": {
            "contractAddress": "string",
            "network": "string",
            "tokenId": "string"
         }
      }
   ],
   "tokenBalances": [
      {
         "atBlockchainInstant": {
            "time": number
         },
         "balance": "string",
         "lastUpdatedTime": {
            "time": number
         },
         "ownerIdentifier": {
            "address": "string"
         },
         "tokenIdentifier": {
            "contractAddress": "string",
            "network": "string",
            "tokenId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetTokenBalance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetTokenBalance_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-BatchGetTokenBalance-response-errors"></a>
An array of `BatchGetTokenBalanceErrorItem` objects returned from the request.
Type: Array of [BatchGetTokenBalanceErrorItem](API_BatchGetTokenBalanceErrorItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [tokenBalances](#API_BatchGetTokenBalance_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-BatchGetTokenBalance-response-tokenBalances"></a>
An array of `BatchGetTokenBalanceOutputItem` objects returned by the response.
Type: Array of [BatchGetTokenBalanceOutputItem](API_BatchGetTokenBalanceOutputItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_BatchGetTokenBalance_Errors"></a>

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
<a name="API_BatchGetTokenBalance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-query-2023-05-04/BatchGetTokenBalance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-query-2023-05-04/BatchGetTokenBalance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/BatchGetTokenBalance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-query-2023-05-04/BatchGetTokenBalance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/BatchGetTokenBalance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-query-2023-05-04/BatchGetTokenBalance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-query-2023-05-04/BatchGetTokenBalance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-query-2023-05-04/BatchGetTokenBalance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-query-2023-05-04/BatchGetTokenBalance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/BatchGetTokenBalance)
