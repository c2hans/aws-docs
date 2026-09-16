---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCommandExecution.html
---

# DeleteCommandExecution
<a name="API_DeleteCommandExecution"></a>

Delete a command execution.

**Note**
Only command executions that enter a terminal state can be deleted from your account.

## Request Syntax
<a name="API_DeleteCommandExecution_RequestSyntax"></a>

```
DELETE /command-executions/{{executionId}}?targetArn={{targetArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCommandExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [executionId](#API_DeleteCommandExecution_RequestSyntax) **   <a name="iot-DeleteCommandExecution-request-uri-executionId"></a>
The unique identifier of the command execution that you want to delete from your account.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [targetArn](#API_DeleteCommandExecution_RequestSyntax) **   <a name="iot-DeleteCommandExecution-request-uri-targetArn"></a>
The Amazon Resource Number (ARN) of the target device for which you want to delete command executions.
Length Constraints: Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_DeleteCommandExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCommandExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteCommandExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCommandExecution_Errors"></a>

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
<a name="API_DeleteCommandExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeleteCommandExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeleteCommandExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeleteCommandExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeleteCommandExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeleteCommandExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeleteCommandExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeleteCommandExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeleteCommandExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeleteCommandExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeleteCommandExecution)
