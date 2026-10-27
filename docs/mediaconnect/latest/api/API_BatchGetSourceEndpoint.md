---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BatchGetSourceEndpoint.html
---

# BatchGetSourceEndpoint
<a name="API_BatchGetSourceEndpoint"></a>

Retrieves information about multiple source endpoints in a single request.

## Request Syntax
<a name="API_BatchGetSourceEndpoint_RequestSyntax"></a>

```
GET /v1/sourceEndpoints?arns={{arns}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BatchGetSourceEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arns](#API_BatchGetSourceEndpoint_RequestSyntax) **   <a name="mediaconnect-BatchGetSourceEndpoint-request-uri-arns"></a>
The Amazon Resource Names (ARNs) of one or more source endpoints to retrieve. You can specify from 1 to 20 ARNs.
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:sourceEndpoint:[a-z0-9]{12}`
Required: Yes

## Request Body
<a name="API_BatchGetSourceEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BatchGetSourceEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "arn": "string",
         "code": "string",
         "message": "string"
      }
   ],
   "sourceEndpoints": [
      {
         "arn": "string",
         "associatedResourceDetails": { ... },
         "availabilityZone": "string",
         "availabilityZoneId": "string",
         "configuration": { ... },
         "connectedDestinations": [ "string" ],
         "connectionDetails": { ... },
         "connectionState": "string",
         "createdAt": "string",
         "description": "string",
         "encryptionConfiguration": { ... },
         "encryptionType": "string",
         "id": "string",
         "lifecycleManagement": "string",
         "messages": [
            {
               "code": "string",
               "message": "string"
            }
         ],
         "name": "string",
         "regionName": "string",
         "registrationState": "string",
         "resourceShareDetails": { ... },
         "resourceShareOwnership": "string",
         "sourceType": "string",
         "tags": {
            "string" : "string"
         },
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetSourceEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetSourceEndpoint_ResponseSyntax) **   <a name="mediaconnect-BatchGetSourceEndpoint-response-errors"></a>
The errors for any source endpoints that MediaConnect couldn't retrieve.
Type: Array of [BatchGetSourceEndpointError](API_BatchGetSourceEndpointError.md) objects

 ** [sourceEndpoints](#API_BatchGetSourceEndpoint_ResponseSyntax) **   <a name="mediaconnect-BatchGetSourceEndpoint-response-sourceEndpoints"></a>
The source endpoints that MediaConnect successfully retrieved.
Type: Array of [SourceEndpoint](API_SourceEndpoint.md) objects

## Errors
<a name="API_BatchGetSourceEndpoint_Errors"></a>

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
<a name="API_BatchGetSourceEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/BatchGetSourceEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/BatchGetSourceEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BatchGetSourceEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/BatchGetSourceEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BatchGetSourceEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/BatchGetSourceEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/BatchGetSourceEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/BatchGetSourceEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/BatchGetSourceEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BatchGetSourceEndpoint)
