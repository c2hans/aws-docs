---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateDocumentationVersion.html
---

# UpdateDocumentationVersion
<a name="API_UpdateDocumentationVersion"></a>

Updates a documentation version.

## Request Syntax
<a name="API_UpdateDocumentationVersion_RequestSyntax"></a>

```
PATCH /restapis/{{restapi_id}}/documentation/versions/{{doc_version}} HTTP/1.1
Content-type: application/json

{
   "patchOperations": [
      {
         "from": "{{string}}",
         "op": "{{string}}",
         "path": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateDocumentationVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [doc\_version](#API_UpdateDocumentationVersion_RequestSyntax) **   <a name="apigw-UpdateDocumentationVersion-request-uri-documentationVersion"></a>
The version identifier of the to-be-updated documentation version.
Required: Yes

 ** [restapi\_id](#API_UpdateDocumentationVersion_RequestSyntax) **   <a name="apigw-UpdateDocumentationVersion-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_UpdateDocumentationVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateDocumentationVersion_RequestSyntax) **   <a name="apigw-UpdateDocumentationVersion-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateDocumentationVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdDate": number,
   "description": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_UpdateDocumentationVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_UpdateDocumentationVersion_ResponseSyntax) **   <a name="apigw-UpdateDocumentationVersion-response-createdDate"></a>
The date when the API documentation snapshot is created.
Type: Timestamp

 ** [description](#API_UpdateDocumentationVersion_ResponseSyntax) **   <a name="apigw-UpdateDocumentationVersion-response-description"></a>
The description of the API documentation snapshot.
Type: String

 ** [version](#API_UpdateDocumentationVersion_ResponseSyntax) **   <a name="apigw-UpdateDocumentationVersion-response-version"></a>
The version identifier of the API documentation snapshot.
Type: String

## Errors
<a name="API_UpdateDocumentationVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 409

 ** LimitExceededException **
The request exceeded the rate limit. Retry after the specified time period.
HTTP Status Code: 429

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## See Also
<a name="API_UpdateDocumentationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateDocumentationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateDocumentationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateDocumentationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateDocumentationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateDocumentationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateDocumentationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateDocumentationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateDocumentationVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateDocumentationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateDocumentationVersion)
