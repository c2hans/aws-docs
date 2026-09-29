---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_GetTokenBalance.html
---

# GetTokenBalance
<a name="API_GetTokenBalance"></a>

**Note**
End of support notice: Amazon Managed Blockchain will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain. For more information, see [Amazon Managed Blockchain availability change](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

Gets the balance of a specific token, including native tokens, for a given address (wallet or contract) on the blockchain.

**Note**
Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.

## Request Syntax
<a name="API_GetTokenBalance_RequestSyntax"></a>

```
POST /get-token-balance HTTP/1.1
Content-type: application/json

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
```

## URI Request Parameters
<a name="API_GetTokenBalance_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTokenBalance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [atBlockchainInstant](#API_GetTokenBalance_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTokenBalance-request-atBlockchainInstant"></a>
The time for when the TokenBalance is requested or the current time if a time is not provided in the request.
This time will only be recorded up to the second.
Type: [BlockchainInstant](API_BlockchainInstant.md) object
Required: No

 ** [ownerIdentifier](#API_GetTokenBalance_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTokenBalance-request-ownerIdentifier"></a>
The container for the identifier for the owner.
Type: [OwnerIdentifier](API_OwnerIdentifier.md) object
Required: Yes

 ** [tokenIdentifier](#API_GetTokenBalance_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTokenBalance-request-tokenIdentifier"></a>
The container for the identifier for the token, including the unique token ID and its blockchain network.
Type: [TokenIdentifier](API_TokenIdentifier.md) object
Required: Yes

## Response Syntax
<a name="API_GetTokenBalance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_GetTokenBalance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [atBlockchainInstant](#API_GetTokenBalance_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTokenBalance-response-atBlockchainInstant"></a>
The container for time.
Type: [BlockchainInstant](API_BlockchainInstant.md) object

 ** [balance](#API_GetTokenBalance_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTokenBalance-response-balance"></a>
The container for the token balance.
Type: String

 ** [lastUpdatedTime](#API_GetTokenBalance_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTokenBalance-response-lastUpdatedTime"></a>
The container for time.
Type: [BlockchainInstant](API_BlockchainInstant.md) object

 ** [ownerIdentifier](#API_GetTokenBalance_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTokenBalance-response-ownerIdentifier"></a>
The container for the owner identifier.
Type: [OwnerIdentifier](API_OwnerIdentifier.md) object

 ** [tokenIdentifier](#API_GetTokenBalance_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetTokenBalance-response-tokenIdentifier"></a>
The container for the identifier for the token including the unique token ID and its blockchain network.
Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.
Type: [TokenIdentifier](API_TokenIdentifier.md) object

## Errors
<a name="API_GetTokenBalance_Errors"></a>

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
<a name="API_GetTokenBalance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-query-2023-05-04/GetTokenBalance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-query-2023-05-04/GetTokenBalance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/GetTokenBalance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-query-2023-05-04/GetTokenBalance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/GetTokenBalance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-query-2023-05-04/GetTokenBalance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-query-2023-05-04/GetTokenBalance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-query-2023-05-04/GetTokenBalance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/managedblockchain-query-2023-05-04/GetTokenBalance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/GetTokenBalance)
