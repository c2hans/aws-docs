---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_PutIntegrationResponse.html
---

# PutIntegrationResponse
<a name="API_PutIntegrationResponse"></a>

Represents a put integration.

## Request Syntax
<a name="API_PutIntegrationResponse_RequestSyntax"></a>

```
PUT /restapis/{{restapi_id}}/resources/{{resource_id}}/methods/{{http_method}}/integration/responses/{{status_code}} HTTP/1.1
Content-type: application/json

{
   "contentHandling": "{{string}}",
   "responseParameters": {
      "{{string}}" : "{{string}}"
   },
   "responseTemplates": {
      "{{string}}" : "{{string}}"
   },
   "selectionPattern": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutIntegrationResponse_RequestParameters"></a>

The request uses the following URI parameters.

 ** [http\_method](#API_PutIntegrationResponse_RequestSyntax) **   <a name="apigw-PutIntegrationResponse-request-uri-httpMethod"></a>
Specifies a put integration response request's HTTP method.
Required: Yes

 ** [resource\_id](#API_PutIntegrationResponse_RequestSyntax) **   <a name="apigw-PutIntegrationResponse-request-uri-resourceId"></a>
Specifies a put integration response request's resource identifier.
Required: Yes

 ** [restapi\_id](#API_PutIntegrationResponse_RequestSyntax) **   <a name="apigw-PutIntegrationResponse-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

 ** [status\_code](#API_PutIntegrationResponse_RequestSyntax) **   <a name="apigw-PutIntegrationResponse-request-uri-statusCode"></a>
Specifies the status code that is used to map the integration response to an existing MethodResponse.
Pattern: `[1-5]\d\d`
Required: Yes

## Request Body
<a name="API_PutIntegrationResponse_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [contentHandling](#API_PutIntegrationResponse_RequestSyntax) **   <a name="apigw-PutIntegrationResponse-request-contentHandling"></a>
Specifies how to handle response payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following behaviors:
If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.
Type: String
Valid Values: `CONVERT_TO_BINARY | CONVERT_TO_TEXT`
Required: No

 ** [responseParameters](#API_PutIntegrationResponse_RequestSyntax) **   <a name="apigw-PutIntegrationResponse-request-responseParameters"></a>
A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of `method.response.header.{name}`, where `name` is a valid and unique header name. The mapped non-static value must match the pattern of `integration.response.header.{name}` or `integration.response.body.{JSON-expression}`, where `name` must be a valid and unique response header name and `JSON-expression` a valid JSON expression without the `$` prefix.
Type: String to string map
Required: No

 ** [responseTemplates](#API_PutIntegrationResponse_RequestSyntax) **   <a name="apigw-PutIntegrationResponse-request-responseTemplates"></a>
Specifies a put integration response's templates.
Type: String to string map
Required: No

 ** [selectionPattern](#API_PutIntegrationResponse_RequestSyntax) **   <a name="apigw-PutIntegrationResponse-request-selectionPattern"></a>
Specifies the selection pattern of a put integration response.
Type: String
Required: No

## Response Syntax
<a name="API_PutIntegrationResponse_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "contentHandling": "string",
   "responseParameters": {
      "string" : "string"
   },
   "responseTemplates": {
      "string" : "string"
   },
   "selectionPattern": "string",
   "statusCode": "string"
}
```

## Response Elements
<a name="API_PutIntegrationResponse_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [contentHandling](#API_PutIntegrationResponse_ResponseSyntax) **   <a name="apigw-PutIntegrationResponse-response-contentHandling"></a>
Specifies how to handle response payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following behaviors:
If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.
Type: String
Valid Values: `CONVERT_TO_BINARY | CONVERT_TO_TEXT`

 ** [responseParameters](#API_PutIntegrationResponse_ResponseSyntax) **   <a name="apigw-PutIntegrationResponse-response-responseParameters"></a>
A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of `method.response.header.{name}`, where `name` is a valid and unique header name. The mapped non-static value must match the pattern of `integration.response.header.{name}` or `integration.response.body.{JSON-expression}`, where `name` is a valid and unique response header name and `JSON-expression` is a valid JSON expression without the `$` prefix.
Type: String to string map

 ** [responseTemplates](#API_PutIntegrationResponse_ResponseSyntax) **   <a name="apigw-PutIntegrationResponse-response-responseTemplates"></a>
Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
Type: String to string map

 ** [selectionPattern](#API_PutIntegrationResponse_ResponseSyntax) **   <a name="apigw-PutIntegrationResponse-response-selectionPattern"></a>
Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the `.+` regex to match error response. However, make sure that the error response does not contain any newline (`\n`) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.
Type: String

 ** [statusCode](#API_PutIntegrationResponse_ResponseSyntax) **   <a name="apigw-PutIntegrationResponse-response-statusCode"></a>
Specifies the status code that is used to map the integration response to an existing MethodResponse.
Type: String
Pattern: `[1-5]\d\d`

## Errors
<a name="API_PutIntegrationResponse_Errors"></a>

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

## Examples
<a name="API_PutIntegrationResponse_Examples"></a>

### Set up an integration response
<a name="API_PutIntegrationResponse_Example_1"></a>

This example illustrates one usage of PutIntegrationResponse.

#### Sample Request
<a name="API_PutIntegrationResponse_Example_1_Request"></a>

```
PUT /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160602T233930Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160602/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "selectionPattern" : "2\d{2}",
  "responseParameters" : {
    "method.response.header.Content-Type" : "'application/json'"
  }
}
```

#### Sample Response
<a name="API_PutIntegrationResponse_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html",
      "name": "integrationresponse",
      "templated": true
    },
    "self": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200",
      "title": "200"
    },
    "integrationresponse:delete": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200"
    },
    "integrationresponse:update": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200"
    }
  },
  "responseParameters": {
    "method.response.header.Content-Type": "'application/json'"
  },
  "selectionPattern": "2\d{2}",
  "statusCode": "200"
}
```

## See Also
<a name="API_PutIntegrationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/PutIntegrationResponse)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/PutIntegrationResponse)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/PutIntegrationResponse)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/PutIntegrationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/PutIntegrationResponse)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/PutIntegrationResponse)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/PutIntegrationResponse)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/PutIntegrationResponse)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/PutIntegrationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/PutIntegrationResponse)
