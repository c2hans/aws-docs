---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateApiKey.html
---

# UpdateApiKey
<a name="API_UpdateApiKey"></a>

Changes information about an ApiKey resource.

## Request Syntax
<a name="API_UpdateApiKey_RequestSyntax"></a>

```
PATCH /apikeys/{{api_Key}} HTTP/1.1
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
<a name="API_UpdateApiKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [api\_Key](#API_UpdateApiKey_RequestSyntax) **   <a name="apigw-UpdateApiKey-request-uri-apiKey"></a>
The identifier of the ApiKey resource to be updated.
Required: Yes

## Request Body
<a name="API_UpdateApiKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateApiKey_RequestSyntax) **   <a name="apigw-UpdateApiKey-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateApiKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdDate": number,
   "customerId": "string",
   "description": "string",
   "enabled": boolean,
   "id": "string",
   "lastUpdatedDate": number,
   "name": "string",
   "stageKeys": [ "string" ],
   "tags": {
      "string" : "string"
   },
   "value": "string"
}
```

## Response Elements
<a name="API_UpdateApiKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_UpdateApiKey_ResponseSyntax) **   <a name="apigw-UpdateApiKey-response-createdDate"></a>
The timestamp when the API Key was created.
Type: Timestamp

 ** [customerId](#API_UpdateApiKey_ResponseSyntax) **   <a name="apigw-UpdateApiKey-response-customerId"></a>
An AWS Marketplace customer identifier, when integrating with the AWS SaaS Marketplace.
Type: String

 ** [description](#API_UpdateApiKey_ResponseSyntax) **   <a name="apigw-UpdateApiKey-response-description"></a>
The description of the API Key.
Type: String

 ** [enabled](#API_UpdateApiKey_ResponseSyntax) **   <a name="apigw-UpdateApiKey-response-enabled"></a>
Specifies whether the API Key can be used by callers.
Type: Boolean

 ** [id](#API_UpdateApiKey_ResponseSyntax) **   <a name="apigw-UpdateApiKey-response-id"></a>
The identifier of the API Key.
Type: String

 ** [lastUpdatedDate](#API_UpdateApiKey_ResponseSyntax) **   <a name="apigw-UpdateApiKey-response-lastUpdatedDate"></a>
The timestamp when the API Key was last updated.
Type: Timestamp

 ** [name](#API_UpdateApiKey_ResponseSyntax) **   <a name="apigw-UpdateApiKey-response-name"></a>
The name of the API Key.
Type: String

 ** [stageKeys](#API_UpdateApiKey_ResponseSyntax) **   <a name="apigw-UpdateApiKey-response-stageKeys"></a>
A list of Stage resources that are associated with the ApiKey resource.
Type: Array of strings

 ** [tags](#API_UpdateApiKey_ResponseSyntax) **   <a name="apigw-UpdateApiKey-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [value](#API_UpdateApiKey_ResponseSyntax) **   <a name="apigw-UpdateApiKey-response-value"></a>
The value of the API Key.
Type: String

## Errors
<a name="API_UpdateApiKey_Errors"></a>

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
<a name="API_UpdateApiKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateApiKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateApiKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateApiKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateApiKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateApiKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateApiKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateApiKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateApiKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateApiKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateApiKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
