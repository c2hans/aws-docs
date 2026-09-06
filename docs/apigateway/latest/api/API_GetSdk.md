---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetSdk.html
---

# GetSdk
<a name="API_GetSdk"></a>

Generates a client SDK for a RestApi and Stage.

## Request Syntax
<a name="API_GetSdk_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/stages/{{stage_name}}/sdks/{{sdk_type}}?{{parameters}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSdk_RequestParameters"></a>

The request uses the following URI parameters.

 ** [parameters](#API_GetSdk_RequestSyntax) **   <a name="apigw-GetSdk-request-uri-parameters"></a>
A string-to-string key-value map of query parameters `sdkType`-dependent properties of the SDK. For `sdkType` of `objectivec` or `swift`, a parameter named `classPrefix` is required. For `sdkType` of `android`, parameters named `groupId`, `artifactId`, `artifactVersion`, and `invokerPackage` are required. For `sdkType` of `java`, parameters named `serviceName` and `javaPackageName` are required.

 ** [restapi\_id](#API_GetSdk_RequestSyntax) **   <a name="apigw-GetSdk-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

 ** [sdk\_type](#API_GetSdk_RequestSyntax) **   <a name="apigw-GetSdk-request-uri-sdkType"></a>
The language for the generated SDK. Currently `java`, `javascript`, `android`, `objectivec` (for iOS), `swift` (for iOS), and `ruby` are supported.
Required: Yes

 ** [stage\_name](#API_GetSdk_RequestSyntax) **   <a name="apigw-GetSdk-request-uri-stageName"></a>
The name of the Stage that the SDK will use.
Required: Yes

## Request Body
<a name="API_GetSdk_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSdk_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{contentType}}
Content-Disposition: {{contentDisposition}}

{{body}}
```

## Response Elements
<a name="API_GetSdk_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [contentDisposition](#API_GetSdk_ResponseSyntax) **   <a name="apigw-GetSdk-response-contentDisposition"></a>
The content-disposition header value in the HTTP response.

 ** [contentType](#API_GetSdk_ResponseSyntax) **   <a name="apigw-GetSdk-response-contentType"></a>
The content-type header value in the HTTP response.

The response returns the following as the HTTP body.

 ** [body](#API_GetSdk_ResponseSyntax) **   <a name="apigw-GetSdk-response-body"></a>
The binary blob response to GetSdk, which contains the generated SDK.

## Errors
<a name="API_GetSdk_Errors"></a>

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
<a name="API_GetSdk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetSdk)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetSdk)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetSdk)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetSdk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetSdk)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetSdk)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetSdk)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetSdk)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetSdk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetSdk)
