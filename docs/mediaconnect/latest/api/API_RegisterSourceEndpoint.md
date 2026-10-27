---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RegisterSourceEndpoint.html
---

# RegisterSourceEndpoint
<a name="API_RegisterSourceEndpoint"></a>

Registers a new source endpoint in MediaConnect.

## Request Syntax
<a name="API_RegisterSourceEndpoint_RequestSyntax"></a>

```
POST /v1/sourceEndpoint HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configuration": { ... },
   "description": "{{string}}",
   "regionName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_RegisterSourceEndpoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterSourceEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_RegisterSourceEndpoint_RequestSyntax) **   <a name="mediaconnect-RegisterSourceEndpoint-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If this token matches a previous request, the service ignores the request, but does not return an error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[!-~]+`
Required: No

 ** [configuration](#API_RegisterSourceEndpoint_RequestSyntax) **   <a name="mediaconnect-RegisterSourceEndpoint-request-configuration"></a>
The configuration settings for the source endpoint.
Type: [SourceEndpointConfiguration](API_SourceEndpointConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [description](#API_RegisterSourceEndpoint_RequestSyntax) **   <a name="mediaconnect-RegisterSourceEndpoint-request-description"></a>
A description to help you identify the source endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[ a-zA-Z_0-9\-.',@:;\(\)\[\]*]+`
Required: No

 ** [regionName](#API_RegisterSourceEndpoint_RequestSyntax) **   <a name="mediaconnect-RegisterSourceEndpoint-request-regionName"></a>
The name of the AWS Region in which to register the source endpoint. Defaults to the current region if not specified.
Type: String
Required: No

 ** [tags](#API_RegisterSourceEndpoint_RequestSyntax) **   <a name="mediaconnect-RegisterSourceEndpoint-request-tags"></a>
The tags to apply to the source endpoint. Each tag is a key-value pair.
Type: String to string map
Required: No

## Response Syntax
<a name="API_RegisterSourceEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "sourceEndpoint": {
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
}
```

## Response Elements
<a name="API_RegisterSourceEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [sourceEndpoint](#API_RegisterSourceEndpoint_ResponseSyntax) **   <a name="mediaconnect-RegisterSourceEndpoint-response-sourceEndpoint"></a>
The details of the source endpoint that was registered.
Type: [SourceEndpoint](API_SourceEndpoint.md) object

## Errors
<a name="API_RegisterSourceEndpoint_Errors"></a>

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

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** SourceEndpointServiceQuotaExceededException **
The request would cause you to exceed a service quota for source endpoints. Delete unused source endpoints or request a quota increase, then try your request again.
HTTP Status Code: 420

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_RegisterSourceEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/RegisterSourceEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/RegisterSourceEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RegisterSourceEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/RegisterSourceEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RegisterSourceEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/RegisterSourceEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/RegisterSourceEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/RegisterSourceEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/RegisterSourceEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RegisterSourceEndpoint)
