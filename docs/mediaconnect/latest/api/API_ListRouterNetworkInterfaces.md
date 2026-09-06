---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListRouterNetworkInterfaces.html
---

# ListRouterNetworkInterfaces
<a name="API_ListRouterNetworkInterfaces"></a>

Retrieves a list of router network interfaces in AWS Elemental MediaConnect.

## Request Syntax
<a name="API_ListRouterNetworkInterfaces_RequestSyntax"></a>

```
POST /v1/routerNetworkInterfaces?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filters": [
      { ... }
   ]
}
```

## URI Request Parameters
<a name="API_ListRouterNetworkInterfaces_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListRouterNetworkInterfaces_RequestSyntax) **   <a name="mediaconnect-ListRouterNetworkInterfaces-request-uri-maxResults"></a>
The maximum number of router network interfaces to return in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListRouterNetworkInterfaces_RequestSyntax) **   <a name="mediaconnect-ListRouterNetworkInterfaces-request-uri-nextToken"></a>
A token used to retrieve the next page of results.

## Request Body
<a name="API_ListRouterNetworkInterfaces_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListRouterNetworkInterfaces_RequestSyntax) **   <a name="mediaconnect-ListRouterNetworkInterfaces-request-filters"></a>
The filters to apply when retrieving the list of router network interfaces.
Type: Array of [RouterNetworkInterfaceFilter](API_RouterNetworkInterfaceFilter.md) objects
Required: No

## Response Syntax
<a name="API_ListRouterNetworkInterfaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "routerNetworkInterfaces": [
      {
         "arn": "string",
         "associatedInputCount": number,
         "associatedOutputCount": number,
         "createdAt": "string",
         "id": "string",
         "name": "string",
         "networkInterfaceType": "string",
         "regionName": "string",
         "state": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRouterNetworkInterfaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRouterNetworkInterfaces_ResponseSyntax) **   <a name="mediaconnect-ListRouterNetworkInterfaces-response-nextToken"></a>
The token to use to retrieve the next page of results.
Type: String

 ** [routerNetworkInterfaces](#API_ListRouterNetworkInterfaces_ResponseSyntax) **   <a name="mediaconnect-ListRouterNetworkInterfaces-response-routerNetworkInterfaces"></a>
The summary information for the retrieved router network interfaces.
Type: Array of [ListedRouterNetworkInterface](API_ListedRouterNetworkInterface.md) objects

## Errors
<a name="API_ListRouterNetworkInterfaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_ListRouterNetworkInterfaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/ListRouterNetworkInterfaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/ListRouterNetworkInterfaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListRouterNetworkInterfaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/ListRouterNetworkInterfaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListRouterNetworkInterfaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/ListRouterNetworkInterfaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/ListRouterNetworkInterfaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/ListRouterNetworkInterfaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/ListRouterNetworkInterfaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListRouterNetworkInterfaces)
