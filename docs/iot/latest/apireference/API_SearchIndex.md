---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_SearchIndex.html
---

# SearchIndex
<a name="API_SearchIndex"></a>

Searches the specified index.

If a device has never connected to IoT Core or was disconnected for more than 1 hour before fleet indexing's `thingConnectivityIndexingMode` was enabled, the `connectivity` object for this device in the response will have the `connected` field set to `false` with no additional session details.

Requires permission to access the [SearchIndex](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_SearchIndex_RequestSyntax"></a>

```
POST /indices/search HTTP/1.1
Content-type: application/json

{
   "indexName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "queryString": "{{string}}",
   "queryVersion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchIndex_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchIndex_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [indexName](#API_SearchIndex_RequestSyntax) **   <a name="iot-SearchIndex-request-indexName"></a>
The search index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [maxResults](#API_SearchIndex_RequestSyntax) **   <a name="iot-SearchIndex-request-maxResults"></a>
The maximum number of results to return per page at one time. This maximum number cannot exceed 100. The response might contain fewer results but will never contain more. You can use [https://docs.aws.amazon.com/iot/latest/apireference/API_SearchIndex.html#iot-SearchIndex-request-nextToken](https://docs.aws.amazon.com/iot/latest/apireference/API_SearchIndex.html#iot-SearchIndex-request-nextToken) to retrieve the next set of results until `nextToken` returns `NULL`.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_SearchIndex_RequestSyntax) **   <a name="iot-SearchIndex-request-nextToken"></a>
The token used to get the next set of results, or `null` if there are no additional results.
Type: String
Required: No

 ** [queryString](#API_SearchIndex_RequestSyntax) **   <a name="iot-SearchIndex-request-queryString"></a>
The search query string. For more information about the search query syntax, see [Query syntax](https://docs.aws.amazon.com/iot/latest/developerguide/query-syntax.html).
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [queryVersion](#API_SearchIndex_RequestSyntax) **   <a name="iot-SearchIndex-request-queryVersion"></a>
The query version.
Type: String
Required: No

## Response Syntax
<a name="API_SearchIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "thingGroups": [
      {
         "attributes": {
            "string" : "string"
         },
         "parentGroupNames": [ "string" ],
         "thingGroupDescription": "string",
         "thingGroupId": "string",
         "thingGroupName": "string"
      }
   ],
   "things": [
      {
         "attributes": {
            "string" : "string"
         },
         "connectivity": {
            "cleanSession": boolean,
            "clientId": "string",
            "connected": boolean,
            "disconnectReason": "string",
            "keepAliveDuration": number,
            "sessionExpiry": number,
            "timestamp": number
         },
         "deviceDefender": "string",
         "shadow": "string",
         "thingGroupNames": [ "string" ],
         "thingId": "string",
         "thingName": "string",
         "thingTypeName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_SearchIndex_ResponseSyntax) **   <a name="iot-SearchIndex-response-nextToken"></a>
The token used to get the next set of results, or `null` if there are no additional results.
Type: String

 ** [thingGroups](#API_SearchIndex_ResponseSyntax) **   <a name="iot-SearchIndex-response-thingGroups"></a>
The thing groups that match the search query.
Type: Array of [ThingGroupDocument](API_ThingGroupDocument.md) objects

 ** [things](#API_SearchIndex_ResponseSyntax) **   <a name="iot-SearchIndex-response-things"></a>
The things that match the search query.
Type: Array of [ThingDocument](API_ThingDocument.md) objects

## Errors
<a name="API_SearchIndex_Errors"></a>

 ** IndexNotReadyException **
The index is not ready.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidQueryException **
The query is invalid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_SearchIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/SearchIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/SearchIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/SearchIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/SearchIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/SearchIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/SearchIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/SearchIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/SearchIndex)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/SearchIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/SearchIndex)
