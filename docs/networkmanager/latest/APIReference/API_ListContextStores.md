---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListContextStores.html
---

# ListContextStores

Returns the context stores in your account. You can optionally return only the context stores in a specific global network.

## Request Syntax
<a name="API_ListContextStores_RequestSyntax"></a>

```
GET /context-stores?globalNetworkId={{GlobalNetworkId}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContextStores_RequestParameters"></a>

The request uses the following URI parameters.

 ** [GlobalNetworkId](#API_ListContextStores_RequestSyntax) **   <a name="networkmanager-ListContextStores-request-uri-GlobalNetworkId"></a>
The ID of a global network. If you specify this parameter, only the context stores in the global network are returned.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`

 ** [MaxResults](#API_ListContextStores_RequestSyntax) **   <a name="networkmanager-ListContextStores-request-uri-MaxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 500.

 ** [NextToken](#API_ListContextStores_RequestSyntax) **   <a name="networkmanager-ListContextStores-request-uri-NextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Request Body
<a name="API_ListContextStores_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContextStores_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContextStores": [
      {
         "ContextStoreArn": "string",
         "ContextStoreId": "string",
         "CreatedAt": number,
         "Description": "string",
         "GlobalNetworkId": "string",
         "State": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContextStores_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContextStores](#API_ListContextStores_ResponseSyntax) **   <a name="networkmanager-ListContextStores-response-ContextStores"></a>
The context stores.
Type: Array of [ContextStore](API_ContextStore.md) objects

 ** [NextToken](#API_ListContextStores_ResponseSyntax) **   <a name="networkmanager-ListContextStores-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Errors
<a name="API_ListContextStores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** Context **
The specified resource could not be found.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason for the error.
HTTP Status Code: 400

## See Also
<a name="API_ListContextStores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListContextStores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/ListContextStores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListContextStores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListContextStores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListContextStores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListContextStores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListContextStores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListContextStores)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListContextStores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListContextStores)
