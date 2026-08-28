---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CreateDocumentationVersion.html
---

# CreateDocumentationVersion
<a name="API_CreateDocumentationVersion"></a>

Creates a documentation version

## Request Syntax
<a name="API_CreateDocumentationVersion_RequestSyntax"></a>

```
POST /restapis/{{restapi_id}}/documentation/versions HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "documentationVersion": "{{string}}",
   "stageName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDocumentationVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [restapi\_id](#API_CreateDocumentationVersion_RequestSyntax) **   <a name="apigw-CreateDocumentationVersion-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_CreateDocumentationVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateDocumentationVersion_RequestSyntax) **   <a name="apigw-CreateDocumentationVersion-request-description"></a>
A description about the new documentation snapshot.
Type: String
Required: No

 ** [documentationVersion](#API_CreateDocumentationVersion_RequestSyntax) **   <a name="apigw-CreateDocumentationVersion-request-documentationVersion"></a>
The version identifier of the new snapshot.
Type: String
Required: Yes

 ** [stageName](#API_CreateDocumentationVersion_RequestSyntax) **   <a name="apigw-CreateDocumentationVersion-request-stageName"></a>
The stage name to be associated with the new documentation snapshot.
Type: String
Required: No

## Response Syntax
<a name="API_CreateDocumentationVersion_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdDate": number,
   "description": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_CreateDocumentationVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_CreateDocumentationVersion_ResponseSyntax) **   <a name="apigw-CreateDocumentationVersion-response-createdDate"></a>
The date when the API documentation snapshot is created.
Type: Timestamp

 ** [description](#API_CreateDocumentationVersion_ResponseSyntax) **   <a name="apigw-CreateDocumentationVersion-response-description"></a>
The description of the API documentation snapshot.
Type: String

 ** [version](#API_CreateDocumentationVersion_ResponseSyntax) **   <a name="apigw-CreateDocumentationVersion-response-version"></a>
The version identifier of the API documentation snapshot.
Type: String

## Errors
<a name="API_CreateDocumentationVersion_Errors"></a>

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
<a name="API_CreateDocumentationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/CreateDocumentationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/CreateDocumentationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CreateDocumentationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/CreateDocumentationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateDocumentationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/CreateDocumentationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/CreateDocumentationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/CreateDocumentationVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateDocumentationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CreateDocumentationVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
