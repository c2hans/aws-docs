---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ConnectEndpoints.html
---

# ConnectEndpoints
<a name="API_ConnectEndpoints"></a>

Connects a source endpoint to a destination endpoint.

## Request Syntax
<a name="API_ConnectEndpoints_RequestSyntax"></a>

```
PUT /v1/connectEndpoints/{{destinationEndpointArn}} HTTP/1.1
Content-type: application/json

{
   "sourceEndpointArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ConnectEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [destinationEndpointArn](#API_ConnectEndpoints_RequestSyntax) **   <a name="mediaconnect-ConnectEndpoints-request-uri-destinationEndpointArn"></a>
The Amazon Resource Name (ARN) of the destination endpoint to connect.
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:destinationEndpoint:[a-z0-9]{12}`
Required: Yes

## Request Body
<a name="API_ConnectEndpoints_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sourceEndpointArn](#API_ConnectEndpoints_RequestSyntax) **   <a name="mediaconnect-ConnectEndpoints-request-sourceEndpointArn"></a>
The Amazon Resource Name (ARN) of the source endpoint to connect.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:sourceEndpoint:[a-z0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_ConnectEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "destinationEndpointArn": "string",
   "destinationEndpointName": "string",
   "sourceEndpointArn": "string",
   "sourceEndpointName": "string"
}
```

## Response Elements
<a name="API_ConnectEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [destinationEndpointArn](#API_ConnectEndpoints_ResponseSyntax) **   <a name="mediaconnect-ConnectEndpoints-response-destinationEndpointArn"></a>
The Amazon Resource Name (ARN) of the connected destination endpoint.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:destinationEndpoint:[a-z0-9]{12}`

 ** [destinationEndpointName](#API_ConnectEndpoints_ResponseSyntax) **   <a name="mediaconnect-ConnectEndpoints-response-destinationEndpointName"></a>
The name of the connected destination endpoint.
Type: String

 ** [sourceEndpointArn](#API_ConnectEndpoints_ResponseSyntax) **   <a name="mediaconnect-ConnectEndpoints-response-sourceEndpointArn"></a>
The Amazon Resource Name (ARN) of the connected source endpoint.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:sourceEndpoint:[a-z0-9]{12}`

 ** [sourceEndpointName](#API_ConnectEndpoints_ResponseSyntax) **   <a name="mediaconnect-ConnectEndpoints-response-sourceEndpointName"></a>
The name of the connected source endpoint.
Type: String

## Errors
<a name="API_ConnectEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_ConnectEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/ConnectEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/ConnectEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ConnectEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/ConnectEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ConnectEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/ConnectEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/ConnectEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/ConnectEndpoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/ConnectEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ConnectEndpoints)
