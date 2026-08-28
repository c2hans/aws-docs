---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_DeleteMethodResponse.html
---

# DeleteMethodResponse
<a name="API_DeleteMethodResponse"></a>

Deletes an existing MethodResponse resource.

## Request Syntax
<a name="API_DeleteMethodResponse_RequestSyntax"></a>

```
DELETE /restapis/{{restapi_id}}/resources/{{resource_id}}/methods/{{http_method}}/responses/{{status_code}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteMethodResponse_RequestParameters"></a>

The request uses the following URI parameters.

 ** [http\_method](#API_DeleteMethodResponse_RequestSyntax) **   <a name="apigw-DeleteMethodResponse-request-uri-httpMethod"></a>
The HTTP verb of the Method resource.
Required: Yes

 ** [resource\_id](#API_DeleteMethodResponse_RequestSyntax) **   <a name="apigw-DeleteMethodResponse-request-uri-resourceId"></a>
The Resource identifier for the MethodResponse resource.
Required: Yes

 ** [restapi\_id](#API_DeleteMethodResponse_RequestSyntax) **   <a name="apigw-DeleteMethodResponse-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

 ** [status\_code](#API_DeleteMethodResponse_RequestSyntax) **   <a name="apigw-DeleteMethodResponse-request-uri-statusCode"></a>
The status code identifier for the MethodResponse resource.
Pattern: `[1-5]\d\d`
Required: Yes

## Request Body
<a name="API_DeleteMethodResponse_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteMethodResponse_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteMethodResponse_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteMethodResponse_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 409

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
<a name="API_DeleteMethodResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/DeleteMethodResponse)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/DeleteMethodResponse)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/DeleteMethodResponse)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/DeleteMethodResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/DeleteMethodResponse)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/DeleteMethodResponse)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/DeleteMethodResponse)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/DeleteMethodResponse)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/DeleteMethodResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/DeleteMethodResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
