---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTokenBalances.html
---

# ListTokenBalances
<a name="API_ListTokenBalances"></a>

This action returns the following for a given blockchain network:
+ Lists all token balances owned by an address (either a contract address or a wallet address).
+ Lists all token balances for all tokens created by a contract.
+ Lists all token balances for a given token.

**Note**
You must always specify the network property of the `tokenFilter` when using this operation.

## Request Syntax
<a name="API_ListTokenBalances_RequestSyntax"></a>

```
POST /list-token-balances HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "ownerFilter": {
      "address": "{{string}}"
   },
   "tokenFilter": {
      "contractAddress": "{{string}}",
      "network": "{{string}}",
      "tokenId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListTokenBalances_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTokenBalances_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListTokenBalances_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTokenBalances-request-maxResults"></a>
The maximum number of token balances to return.
Default: `100`
Even if additional results can be retrieved, the request can return less results than `maxResults` or an empty array of results.
To retrieve the next set of results, make another request with the returned `nextToken` value. The value of `nextToken` is `null` when there are no more results to return
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 250.
Required: No

 ** [nextToken](#API_ListTokenBalances_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTokenBalances-request-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131070.
Required: No

 ** [ownerFilter](#API_ListTokenBalances_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTokenBalances-request-ownerFilter"></a>
The contract or wallet address on the blockchain network by which to filter the request. You must specify the `address` property of the `ownerFilter` when listing balances of tokens owned by the address.
Type: [OwnerFilter](API_OwnerFilter.md) object
Required: No

 ** [tokenFilter](#API_ListTokenBalances_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTokenBalances-request-tokenFilter"></a>
The contract address or a token identifier on the blockchain network by which to filter the request. You must specify the `contractAddress` property of this container when listing tokens minted by a contract.
You must always specify the network property of this container when using this operation.
Type: [TokenFilter](API_TokenFilter.md) object
Required: Yes

## Response Syntax
<a name="API_ListTokenBalances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
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
<a name="API_ListTokenBalances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTokenBalances_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTokenBalances-response-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131070.

 ** [tokenBalances](#API_ListTokenBalances_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-ListTokenBalances-response-tokenBalances"></a>
An array of `TokenBalance` objects. Each object contains details about the token balance.
Type: Array of [TokenBalance](API_TokenBalance.md) objects
Array Members: Minimum number of 0 items. Maximum number of 250 items.

## Errors
<a name="API_ListTokenBalances_Errors"></a>

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
<a name="API_ListTokenBalances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-query-2023-05-04/ListTokenBalances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-query-2023-05-04/ListTokenBalances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/ListTokenBalances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-query-2023-05-04/ListTokenBalances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/ListTokenBalances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-query-2023-05-04/ListTokenBalances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-query-2023-05-04/ListTokenBalances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-query-2023-05-04/ListTokenBalances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-query-2023-05-04/ListTokenBalances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ListTokenBalances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
