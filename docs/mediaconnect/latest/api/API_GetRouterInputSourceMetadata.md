---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterInputSourceMetadata.html
---

# GetRouterInputSourceMetadata
<a name="API_GetRouterInputSourceMetadata"></a>

Retrieves detailed metadata information about a specific router input source, including stream details and connection state.

## Request Syntax
<a name="API_GetRouterInputSourceMetadata_RequestSyntax"></a>

```
GET /v1/routerInput/{{arn}}/source-metadata HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRouterInputSourceMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetRouterInputSourceMetadata_RequestSyntax) **   <a name="mediaconnect-GetRouterInputSourceMetadata-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the router input to retrieve metadata for.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`
Required: Yes

## Request Body
<a name="API_GetRouterInputSourceMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRouterInputSourceMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "name": "string",
   "sourceMetadataDetails": {
      "routerInputMetadata": { ... },
      "sourceMetadataMessages": [
         {
            "code": "string",
            "message": "string"
         }
      ],
      "timestamp": "string"
   }
}
```

## Response Elements
<a name="API_GetRouterInputSourceMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetRouterInputSourceMetadata_ResponseSyntax) **   <a name="mediaconnect-GetRouterInputSourceMetadata-response-arn"></a>
The Amazon Resource Name (ARN) of the router input.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`

 ** [name](#API_GetRouterInputSourceMetadata_ResponseSyntax) **   <a name="mediaconnect-GetRouterInputSourceMetadata-response-name"></a>
The name of the router input.
Type: String

 ** [sourceMetadataDetails](#API_GetRouterInputSourceMetadata_ResponseSyntax) **   <a name="mediaconnect-GetRouterInputSourceMetadata-response-sourceMetadataDetails"></a>
Detailed metadata information about the router input source, including connection state, timestamps, and stream configuration.
Type: [RouterInputSourceMetadataDetails](API_RouterInputSourceMetadataDetails.md) object

## Errors
<a name="API_GetRouterInputSourceMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

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
<a name="API_GetRouterInputSourceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/GetRouterInputSourceMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/GetRouterInputSourceMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/GetRouterInputSourceMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/GetRouterInputSourceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/GetRouterInputSourceMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/GetRouterInputSourceMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/GetRouterInputSourceMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/GetRouterInputSourceMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/GetRouterInputSourceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/GetRouterInputSourceMetadata)
