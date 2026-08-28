---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCommand.html
---

# DeleteCommand
<a name="API_DeleteCommand"></a>

Delete a command resource.

## Request Syntax
<a name="API_DeleteCommand_RequestSyntax"></a>

```
DELETE /commands/{{commandId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCommand_RequestParameters"></a>

The request uses the following URI parameters.

 ** [commandId](#API_DeleteCommand_RequestSyntax) **   <a name="iot-DeleteCommand-request-uri-commandId"></a>
The unique identifier of the command to be deleted.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_DeleteCommand_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCommand_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
```

## Response Elements
<a name="API_DeleteCommand_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_DeleteCommand_ResponseSyntax) **   <a name="iot-DeleteCommand-response-statusCode"></a>
The status code for the command deletion request. The status code is in the 200 range for a successful request.
+ If the command hasn't been deprecated, or has been deprecated for a duration that is shorter than the maximum time out duration of 12 hours, when calling the `DeleteCommand` request, the deletion will be scheduled and a 202 status code will be returned. While the command is being deleted, it will be in a `pendingDeletion` state. Once the time out duration has been reached, the command will be permanently removed from your account.
+ If the command has been deprecated for a duration that is longer than the maximum time out duration of 12 hours, when calling the `DeleteCommand` request, the command will be deleted immediately and a 204 status code will be returned.

## Errors
<a name="API_DeleteCommand_Errors"></a>

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
A resource with the same name already exists.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeleteCommand)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeleteCommand)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeleteCommand)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeleteCommand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeleteCommand)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeleteCommand)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeleteCommand)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeleteCommand)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeleteCommand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeleteCommand)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
