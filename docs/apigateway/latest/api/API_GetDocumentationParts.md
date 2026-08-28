---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetDocumentationParts.html
---

# GetDocumentationParts
<a name="API_GetDocumentationParts"></a>

Gets documentation parts.

## Request Syntax
<a name="API_GetDocumentationParts_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/documentation/parts?limit={{limit}}&locationStatus={{locationStatus}}&name={{nameQuery}}&path={{path}}&position={{position}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDocumentationParts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_GetDocumentationParts_RequestSyntax) **   <a name="apigw-GetDocumentationParts-request-uri-limit"></a>
The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [locationStatus](#API_GetDocumentationParts_RequestSyntax) **   <a name="apigw-GetDocumentationParts-request-uri-locationStatus"></a>
The status of the API documentation parts to retrieve. Valid values are `DOCUMENTED` for retrieving DocumentationPart resources with content and `UNDOCUMENTED` for DocumentationPart resources without content.
Valid Values: `DOCUMENTED | UNDOCUMENTED`

 ** [nameQuery](#API_GetDocumentationParts_RequestSyntax) **   <a name="apigw-GetDocumentationParts-request-uri-nameQuery"></a>
The name of API entities of the to-be-retrieved documentation parts.

 ** [path](#API_GetDocumentationParts_RequestSyntax) **   <a name="apigw-GetDocumentationParts-request-uri-path"></a>
The path of API entities of the to-be-retrieved documentation parts.

 ** [position](#API_GetDocumentationParts_RequestSyntax) **   <a name="apigw-GetDocumentationParts-request-uri-position"></a>
The current pagination position in the paged result set.

 ** [restapi\_id](#API_GetDocumentationParts_RequestSyntax) **   <a name="apigw-GetDocumentationParts-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

 ** [type](#API_GetDocumentationParts_RequestSyntax) **   <a name="apigw-GetDocumentationParts-request-uri-type"></a>
The type of API entities of the to-be-retrieved documentation parts.
Valid Values: `API | AUTHORIZER | MODEL | RESOURCE | METHOD | PATH_PARAMETER | QUERY_PARAMETER | REQUEST_HEADER | REQUEST_BODY | RESPONSE | RESPONSE_HEADER | RESPONSE_BODY`

## Request Body
<a name="API_GetDocumentationParts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDocumentationParts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
      {
         "id": "string",
         "location": {
            "method": "string",
            "name": "string",
            "path": "string",
            "statusCode": "string",
            "type": "string"
         },
         "properties": "string"
      }
   ],
   "position": "string"
}
```

## Response Elements
<a name="API_GetDocumentationParts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetDocumentationParts_ResponseSyntax) **   <a name="apigw-GetDocumentationParts-response-item"></a>
The current page of elements from this collection.
Type: Array of [DocumentationPart](API_DocumentationPart.md) objects

 ** [position](#API_GetDocumentationParts_ResponseSyntax) **   <a name="apigw-GetDocumentationParts-response-position"></a>
The current pagination position in the paged result set.
Type: String

## Errors
<a name="API_GetDocumentationParts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

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
<a name="API_GetDocumentationParts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetDocumentationParts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetDocumentationParts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetDocumentationParts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetDocumentationParts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetDocumentationParts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetDocumentationParts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetDocumentationParts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetDocumentationParts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetDocumentationParts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetDocumentationParts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
