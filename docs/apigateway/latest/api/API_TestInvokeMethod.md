---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_TestInvokeMethod.html
---

# TestInvokeMethod
<a name="API_TestInvokeMethod"></a>

Simulate the invocation of a Method in your RestApi with headers, parameters, and an incoming request body.

## Request Syntax
<a name="API_TestInvokeMethod_RequestSyntax"></a>

```
POST /restapis/{{restapi_id}}/resources/{{resource_id}}/methods/{{http_method}} HTTP/1.1
Content-type: application/json

{
   "body": "{{string}}",
   "clientCertificateId": "{{string}}",
   "headers": {
      "{{string}}" : "{{string}}"
   },
   "multiValueHeaders": {
      "{{string}}" : [ "{{string}}" ]
   },
   "pathWithQueryString": "{{string}}",
   "stageVariables": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TestInvokeMethod_RequestParameters"></a>

The request uses the following URI parameters.

 ** [http\_method](#API_TestInvokeMethod_RequestSyntax) **   <a name="apigw-TestInvokeMethod-request-uri-httpMethod"></a>
Specifies a test invoke method request's HTTP method.
Required: Yes

 ** [resource\_id](#API_TestInvokeMethod_RequestSyntax) **   <a name="apigw-TestInvokeMethod-request-uri-resourceId"></a>
Specifies a test invoke method request's resource ID.
Required: Yes

 ** [restapi\_id](#API_TestInvokeMethod_RequestSyntax) **   <a name="apigw-TestInvokeMethod-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_TestInvokeMethod_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [body](#API_TestInvokeMethod_RequestSyntax) **   <a name="apigw-TestInvokeMethod-request-body"></a>
The simulated request body of an incoming invocation request.
Type: String
Required: No

 ** [clientCertificateId](#API_TestInvokeMethod_RequestSyntax) **   <a name="apigw-TestInvokeMethod-request-clientCertificateId"></a>
A ClientCertificate identifier to use in the test invocation. API Gateway will use the certificate when making the HTTPS request to the defined back-end endpoint.
Type: String
Required: No

 ** [headers](#API_TestInvokeMethod_RequestSyntax) **   <a name="apigw-TestInvokeMethod-request-headers"></a>
A key-value map of headers to simulate an incoming invocation request.
Type: String to string map
Required: No

 ** [multiValueHeaders](#API_TestInvokeMethod_RequestSyntax) **   <a name="apigw-TestInvokeMethod-request-multiValueHeaders"></a>
The headers as a map from string to list of values to simulate an incoming invocation request.
Type: String to array of strings map
Required: No

 ** [pathWithQueryString](#API_TestInvokeMethod_RequestSyntax) **   <a name="apigw-TestInvokeMethod-request-pathWithQueryString"></a>
The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters.
Type: String
Required: No

 ** [stageVariables](#API_TestInvokeMethod_RequestSyntax) **   <a name="apigw-TestInvokeMethod-request-stageVariables"></a>
A key-value map of stage variables to simulate an invocation on a deployed Stage.
Type: String to string map
Required: No

## Response Syntax
<a name="API_TestInvokeMethod_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "body": "string",
   "headers": {
      "string" : "string"
   },
   "latency": number,
   "log": "string",
   "multiValueHeaders": {
      "string" : [ "string" ]
   },
   "status": number
}
```

## Response Elements
<a name="API_TestInvokeMethod_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [body](#API_TestInvokeMethod_ResponseSyntax) **   <a name="apigw-TestInvokeMethod-response-body"></a>
The body of the HTTP response.
Type: String

 ** [headers](#API_TestInvokeMethod_ResponseSyntax) **   <a name="apigw-TestInvokeMethod-response-headers"></a>
The headers of the HTTP response.
Type: String to string map

 ** [latency](#API_TestInvokeMethod_ResponseSyntax) **   <a name="apigw-TestInvokeMethod-response-latency"></a>
The execution latency, in ms, of the test invoke request.
Type: Long

 ** [log](#API_TestInvokeMethod_ResponseSyntax) **   <a name="apigw-TestInvokeMethod-response-log"></a>
The API Gateway execution log for the test invoke request.
Type: String

 ** [multiValueHeaders](#API_TestInvokeMethod_ResponseSyntax) **   <a name="apigw-TestInvokeMethod-response-multiValueHeaders"></a>
The headers of the HTTP response as a map from string to list of values.
Type: String to array of strings map

 ** [status](#API_TestInvokeMethod_ResponseSyntax) **   <a name="apigw-TestInvokeMethod-response-status"></a>
The HTTP status code.
Type: Integer

## Errors
<a name="API_TestInvokeMethod_Errors"></a>

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
<a name="API_TestInvokeMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/TestInvokeMethod)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/TestInvokeMethod)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/TestInvokeMethod)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/TestInvokeMethod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/TestInvokeMethod)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/TestInvokeMethod)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/TestInvokeMethod)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/TestInvokeMethod)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/TestInvokeMethod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/TestInvokeMethod)
