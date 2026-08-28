---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_DeleteThingShadow.html
---

# DeleteThingShadow
<a name="API_iotdata_DeleteThingShadow"></a>

Deletes the shadow for the specified thing.

Requires permission to access the [DeleteThingShadow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

For more information, see [DeleteThingShadow](http://docs.aws.amazon.com/iot/latest/developerguide/API_DeleteThingShadow.html) in the AWS IoT Developer Guide.

## Request Syntax
<a name="API_iotdata_DeleteThingShadow_RequestSyntax"></a>

```
DELETE /things/{{thingName}}/shadow?name={{shadowName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdata_DeleteThingShadow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [shadowName](#API_iotdata_DeleteThingShadow_RequestSyntax) **   <a name="iot-iotdata_DeleteThingShadow-request-uri-shadowName"></a>
The name of the shadow.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[$a-zA-Z0-9:_-]+`

 ** [thingName](#API_iotdata_DeleteThingShadow_RequestSyntax) **   <a name="iot-iotdata_DeleteThingShadow-request-uri-thingName"></a>
The name of the thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_iotdata_DeleteThingShadow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdata_DeleteThingShadow_ResponseSyntax"></a>

```
HTTP/1.1 200

{{payload}}
```

## Response Elements
<a name="API_iotdata_DeleteThingShadow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [payload](#API_iotdata_DeleteThingShadow_ResponseSyntax) **   <a name="iot-iotdata_DeleteThingShadow-response-payload"></a>
The state information, in JSON format.

## Errors
<a name="API_iotdata_DeleteThingShadow_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

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
<a name="API_iotdata_DeleteThingShadow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-data-2015-05-28/DeleteThingShadow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-data-2015-05-28/DeleteThingShadow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/DeleteThingShadow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-data-2015-05-28/DeleteThingShadow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/DeleteThingShadow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-data-2015-05-28/DeleteThingShadow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-data-2015-05-28/DeleteThingShadow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-data-2015-05-28/DeleteThingShadow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-data-2015-05-28/DeleteThingShadow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/DeleteThingShadow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
