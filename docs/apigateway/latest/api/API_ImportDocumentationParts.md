---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_ImportDocumentationParts.html
---

# ImportDocumentationParts
<a name="API_ImportDocumentationParts"></a>

Imports documentation parts

## Request Syntax
<a name="API_ImportDocumentationParts_RequestSyntax"></a>

```
PUT /restapis/{{restapi_id}}/documentation/parts?failonwarnings={{failOnWarnings}}&mode={{mode}} HTTP/1.1

{{body}}
```

## URI Request Parameters
<a name="API_ImportDocumentationParts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [failOnWarnings](#API_ImportDocumentationParts_RequestSyntax) **   <a name="apigw-ImportDocumentationParts-request-uri-failOnWarnings"></a>
A query parameter to specify whether to rollback the documentation importation (`true`) or not (`false`) when a warning is encountered. The default value is `false`.

 ** [mode](#API_ImportDocumentationParts_RequestSyntax) **   <a name="apigw-ImportDocumentationParts-request-uri-mode"></a>
A query parameter to indicate whether to overwrite (`overwrite`) any existing DocumentationParts definition or to merge (`merge`) the new definition into the existing one. The default value is `merge`.
Valid Values: `merge | overwrite`

 ** [restapi\_id](#API_ImportDocumentationParts_RequestSyntax) **   <a name="apigw-ImportDocumentationParts-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_ImportDocumentationParts_RequestBody"></a>

The request accepts the following binary data.

 ** [body](#API_ImportDocumentationParts_RequestSyntax) **   <a name="apigw-ImportDocumentationParts-request-body"></a>
Raw byte array representing the to-be-imported documentation parts. To import from an OpenAPI file, this is a JSON object.
Required: Yes

## Response Syntax
<a name="API_ImportDocumentationParts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ids": [ "string" ],
   "warnings": [ "string" ]
}
```

## Response Elements
<a name="API_ImportDocumentationParts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ids](#API_ImportDocumentationParts_ResponseSyntax) **   <a name="apigw-ImportDocumentationParts-response-ids"></a>
A list of the returned documentation part identifiers.
Type: Array of strings

 ** [warnings](#API_ImportDocumentationParts_ResponseSyntax) **   <a name="apigw-ImportDocumentationParts-response-warnings"></a>
A list of warning messages reported during import of documentation parts.
Type: Array of strings

## Errors
<a name="API_ImportDocumentationParts_Errors"></a>

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
<a name="API_ImportDocumentationParts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/ImportDocumentationParts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/ImportDocumentationParts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/ImportDocumentationParts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/ImportDocumentationParts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/ImportDocumentationParts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/ImportDocumentationParts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/ImportDocumentationParts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/ImportDocumentationParts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/ImportDocumentationParts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/ImportDocumentationParts)
