---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListDestinationEndpoints.html
---

# ListDestinationEndpoints
<a name="API_ListDestinationEndpoints"></a>

Retrieves a list of the destination endpoints in your account. The results are paginated. Use the NextToken value that's returned to retrieve additional results.

## Request Syntax
<a name="API_ListDestinationEndpoints_RequestSyntax"></a>

```
POST /v1/destinationEndpoints?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filters": [
      { ... }
   ]
}
```

## URI Request Parameters
<a name="API_ListDestinationEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListDestinationEndpoints_RequestSyntax) **   <a name="mediaconnect-ListDestinationEndpoints-request-uri-maxResults"></a>
The maximum number of results to return in a single request. The valid range is 1 to 100. If you don't specify a value, the service returns up to 100 results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListDestinationEndpoints_RequestSyntax) **   <a name="mediaconnect-ListDestinationEndpoints-request-uri-nextToken"></a>
The token that identifies the next page of results to return. Use the token that a previous request returned.

## Request Body
<a name="API_ListDestinationEndpoints_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListDestinationEndpoints_RequestSyntax) **   <a name="mediaconnect-ListDestinationEndpoints-request-filters"></a>
The filters to apply to the list of destination endpoints.
Type: Array of [DestinationEndpointFilter](API_DestinationEndpointFilter.md) objects
Required: No

## Response Syntax
<a name="API_ListDestinationEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "destinationEndpoints": [
      {
         "arn": "string",
         "associatedResourceArn": "string",
         "availabilityZone": "string",
         "availabilityZoneId": "string",
         "connectedSource": "string",
         "connectionState": "string",
         "createdAt": "string",
         "decryptionType": "string",
         "destinationType": "string",
         "id": "string",
         "lifecycleManagement": "string",
         "messageCount": number,
         "name": "string",
         "regionName": "string",
         "registrationState": "string",
         "resourceShareOwnership": "string",
         "resourceShareState": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDestinationEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destinationEndpoints](#API_ListDestinationEndpoints_ResponseSyntax) **   <a name="mediaconnect-ListDestinationEndpoints-response-destinationEndpoints"></a>
The destination endpoints that match the request.
Type: Array of [ListedDestinationEndpoint](API_ListedDestinationEndpoint.md) objects

 ** [nextToken](#API_ListDestinationEndpoints_ResponseSyntax) **   <a name="mediaconnect-ListDestinationEndpoints-response-nextToken"></a>
The token to use in the next request to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

## Errors
<a name="API_ListDestinationEndpoints_Errors"></a>

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
<a name="API_ListDestinationEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/ListDestinationEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/ListDestinationEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListDestinationEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/ListDestinationEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListDestinationEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/ListDestinationEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/ListDestinationEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/ListDestinationEndpoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/ListDestinationEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListDestinationEndpoints)
