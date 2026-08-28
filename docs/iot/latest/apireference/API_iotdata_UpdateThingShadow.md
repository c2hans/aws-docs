---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_UpdateThingShadow.html
---

# UpdateThingShadow
<a name="API_iotdata_UpdateThingShadow"></a>

Updates the shadow for the specified thing.

Requires permission to access the [UpdateThingShadow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

For more information, see [UpdateThingShadow](http://docs.aws.amazon.com/iot/latest/developerguide/API_UpdateThingShadow.html) in the AWS IoT Developer Guide.

## Request Syntax
<a name="API_iotdata_UpdateThingShadow_RequestSyntax"></a>

```
POST /things/{{thingName}}/shadow?name={{shadowName}} HTTP/1.1

{{payload}}
```

## URI Request Parameters
<a name="API_iotdata_UpdateThingShadow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [shadowName](#API_iotdata_UpdateThingShadow_RequestSyntax) **   <a name="iot-iotdata_UpdateThingShadow-request-uri-shadowName"></a>
The name of the shadow.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[$a-zA-Z0-9:_-]+`

 ** [thingName](#API_iotdata_UpdateThingShadow_RequestSyntax) **   <a name="iot-iotdata_UpdateThingShadow-request-uri-thingName"></a>
The name of the thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_iotdata_UpdateThingShadow_RequestBody"></a>

The request accepts the following binary data.

 ** [payload](#API_iotdata_UpdateThingShadow_RequestSyntax) **   <a name="iot-iotdata_UpdateThingShadow-request-payload"></a>
The state information, in JSON format.
Required: Yes

## Response Syntax
<a name="API_iotdata_UpdateThingShadow_ResponseSyntax"></a>

```
HTTP/1.1 200

{{payload}}
```

## Response Elements
<a name="API_iotdata_UpdateThingShadow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [payload](#API_iotdata_UpdateThingShadow_ResponseSyntax) **   <a name="iot-iotdata_UpdateThingShadow-response-payload"></a>
The state information, in JSON format.

## Errors
<a name="API_iotdata_UpdateThingShadow_Errors"></a>

 ** ConflictException **
The specified version does not match the version of the document.
 ** message **
The message for the exception.
HTTP Status Code: 409

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** MethodNotAllowedException **
The specified combination of HTTP verb and URI is not supported.
 ** message **
The message for the exception.
HTTP Status Code: 405

 ** RequestEntityTooLargeException **
The payload exceeds the maximum size allowed.
 ** message **
The message for the exception.
HTTP Status Code: 413

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

 ** UnsupportedDocumentEncodingException **
The document encoding is not supported.
 ** message **
The message for the exception.
HTTP Status Code: 415

## See Also
<a name="API_iotdata_UpdateThingShadow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-data-2015-05-28/UpdateThingShadow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-data-2015-05-28/UpdateThingShadow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/UpdateThingShadow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-data-2015-05-28/UpdateThingShadow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/UpdateThingShadow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-data-2015-05-28/UpdateThingShadow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-data-2015-05-28/UpdateThingShadow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-data-2015-05-28/UpdateThingShadow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-data-2015-05-28/UpdateThingShadow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/UpdateThingShadow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
