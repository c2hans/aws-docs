---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListAccessors.html
---

# ListAccessors
<a name="API_ListAccessors"></a>

Returns a list of the accessors and their properties. Accessor objects are containers that have the information required for token based access to your Ethereum nodes.

## Request Syntax
<a name="API_ListAccessors_RequestSyntax"></a>

```
GET /accessors?maxResults={{MaxResults}}&networkType={{NetworkType}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAccessors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListAccessors_RequestSyntax) **   <a name="ManagedBlockchain-ListAccessors-request-uri-MaxResults"></a>
 The maximum number of accessors to list.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NetworkType](#API_ListAccessors_RequestSyntax) **   <a name="ManagedBlockchain-ListAccessors-request-uri-NetworkType"></a>
The blockchain network that the `Accessor` token is created for.
Use the value `ETHEREUM_MAINNET_AND_GOERLI` for all existing `Accessors` tokens that were created before the `networkType` property was introduced.
Valid Values: `ETHEREUM_GOERLI | ETHEREUM_MAINNET | ETHEREUM_MAINNET_AND_GOERLI | POLYGON_MAINNET | POLYGON_MUMBAI`

 ** [NextToken](#API_ListAccessors_RequestSyntax) **   <a name="ManagedBlockchain-ListAccessors-request-uri-NextToken"></a>
 The pagination token that indicates the next set of results to retrieve.
Length Constraints: Maximum length of 128.

## Request Body
<a name="API_ListAccessors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAccessors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Accessors": [
      {
         "Arn": "string",
         "CreationDate": "string",
         "Id": "string",
         "NetworkType": "string",
         "Status": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAccessors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Accessors](#API_ListAccessors_ResponseSyntax) **   <a name="ManagedBlockchain-ListAccessors-response-Accessors"></a>
An array of AccessorSummary objects that contain configuration properties for each accessor.
Type: Array of [AccessorSummary](API_AccessorSummary.md) objects

 ** [NextToken](#API_ListAccessors_ResponseSyntax) **   <a name="ManagedBlockchain-ListAccessors-response-NextToken"></a>
 The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Maximum length of 128.

## Errors
<a name="API_ListAccessors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceErrorException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** InvalidRequestException **
The action or operation requested is invalid. Verify that the action is typed correctly.
HTTP Status Code: 400

 ** ThrottlingException **
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.
HTTP Status Code: 429

## See Also
<a name="API_ListAccessors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/ListAccessors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/ListAccessors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/ListAccessors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/ListAccessors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/ListAccessors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/ListAccessors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/ListAccessors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/ListAccessors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/ListAccessors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/ListAccessors)
