---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetDocumentationVersion.html
---

# GetDocumentationVersion
<a name="API_GetDocumentationVersion"></a>

Gets a documentation version.

## Request Syntax
<a name="API_GetDocumentationVersion_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/documentation/versions/{{doc_version}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDocumentationVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [doc\_version](#API_GetDocumentationVersion_RequestSyntax) **   <a name="apigw-GetDocumentationVersion-request-uri-documentationVersion"></a>
The version identifier of the to-be-retrieved documentation snapshot.
Required: Yes

 ** [restapi\_id](#API_GetDocumentationVersion_RequestSyntax) **   <a name="apigw-GetDocumentationVersion-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_GetDocumentationVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDocumentationVersion_ResponseSyntax"></a>

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
<a name="API_GetDocumentationVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_GetDocumentationVersion_ResponseSyntax) **   <a name="apigw-GetDocumentationVersion-response-createdDate"></a>
The date when the API documentation snapshot is created.
Type: Timestamp

 ** [description](#API_GetDocumentationVersion_ResponseSyntax) **   <a name="apigw-GetDocumentationVersion-response-description"></a>
The description of the API documentation snapshot.
Type: String

 ** [version](#API_GetDocumentationVersion_ResponseSyntax) **   <a name="apigw-GetDocumentationVersion-response-version"></a>
The version identifier of the API documentation snapshot.
Type: String

## Errors
<a name="API_GetDocumentationVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetDocumentationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetDocumentationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetDocumentationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetDocumentationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetDocumentationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetDocumentationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetDocumentationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetDocumentationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetDocumentationVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetDocumentationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetDocumentationVersion)
