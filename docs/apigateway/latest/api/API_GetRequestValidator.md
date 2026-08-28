---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetRequestValidator.html
---

# GetRequestValidator
<a name="API_GetRequestValidator"></a>

Gets a RequestValidator of a given RestApi.

## Request Syntax
<a name="API_GetRequestValidator_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/requestvalidators/{{requestvalidator_id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRequestValidator_RequestParameters"></a>

The request uses the following URI parameters.

 ** [requestvalidator\_id](#API_GetRequestValidator_RequestSyntax) **   <a name="apigw-GetRequestValidator-request-uri-requestValidatorId"></a>
The identifier of the RequestValidator to be retrieved.
Required: Yes

 ** [restapi\_id](#API_GetRequestValidator_RequestSyntax) **   <a name="apigw-GetRequestValidator-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_GetRequestValidator_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRequestValidator_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string",
   "name": "string",
   "validateRequestBody": boolean,
   "validateRequestParameters": boolean
}
```

## Response Elements
<a name="API_GetRequestValidator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_GetRequestValidator_ResponseSyntax) **   <a name="apigw-GetRequestValidator-response-id"></a>
The identifier of this RequestValidator.
Type: String

 ** [name](#API_GetRequestValidator_ResponseSyntax) **   <a name="apigw-GetRequestValidator-response-name"></a>
The name of this RequestValidator
Type: String

 ** [validateRequestBody](#API_GetRequestValidator_ResponseSyntax) **   <a name="apigw-GetRequestValidator-response-validateRequestBody"></a>
A Boolean flag to indicate whether to validate a request body according to the configured Model schema.
Type: Boolean

 ** [validateRequestParameters](#API_GetRequestValidator_ResponseSyntax) **   <a name="apigw-GetRequestValidator-response-validateRequestParameters"></a>
A Boolean flag to indicate whether to validate request parameters (`true`) or not (`false`).
Type: Boolean

## Errors
<a name="API_GetRequestValidator_Errors"></a>

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

## Examples
<a name="API_GetRequestValidator_Examples"></a>

### Get the specified RequestValidator of an API
<a name="API_GetRequestValidator_Example_1"></a>

This example illustrates one usage of GetRequestValidator.

#### Sample Request
<a name="API_GetRequestValidator_Example_1_Request"></a>

```
GET /restapis/mkhqppt4e4/requestvalidators/1t3hul HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20170223T172652Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetRequestValidator_Example_1_Response"></a>

```
{
  "_links": {
    "self": {
      "href": "/restapis/mkhqppt4e4/requestvalidators/1t3hul"
    },
    "request-validator-delete": {
      "href": "/restapis/mkhqppt4e4/requestvalidators/1t3hul"
    },
    "request-validator-update": {
      "href": "/restapis/mkhqppt4e4/requestvalidators/1t3hul"
    }
  },
  "id": "1t3hul",
  "name": "params-only",
  "validateRequestBody": false,
  "validateRequestParameters": true
}
```

## See Also
<a name="API_GetRequestValidator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetRequestValidator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetRequestValidator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetRequestValidator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetRequestValidator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetRequestValidator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetRequestValidator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetRequestValidator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetRequestValidator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetRequestValidator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetRequestValidator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
