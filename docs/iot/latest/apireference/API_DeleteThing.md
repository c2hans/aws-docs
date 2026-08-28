---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThing.html
---

# DeleteThing
<a name="API_DeleteThing"></a>

Deletes the specified thing. Returns successfully with no error if the deletion is successful or you specify a thing that doesn't exist.

Requires permission to access the [DeleteThing](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DeleteThing_RequestSyntax"></a>

```
DELETE /things/{{thingName}}?expectedVersion={{expectedVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteThing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [expectedVersion](#API_DeleteThing_RequestSyntax) **   <a name="iot-DeleteThing-request-uri-expectedVersion"></a>
The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the `DeleteThing` request is rejected with a `VersionConflictException`.

 ** [thingName](#API_DeleteThing_RequestSyntax) **   <a name="iot-DeleteThing-request-uri-thingName"></a>
The name of the thing to delete.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DeleteThing_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteThing_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteThing_Errors"></a>

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
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

 ** VersionConflictException **
An exception thrown when the version of an entity specified with the `expectedVersion` parameter does not match the latest version in the system.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_DeleteThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeleteThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeleteThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeleteThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeleteThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeleteThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeleteThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeleteThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeleteThing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeleteThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeleteThing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
