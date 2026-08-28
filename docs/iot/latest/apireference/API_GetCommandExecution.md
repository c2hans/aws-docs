---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetCommandExecution.html
---

# GetCommandExecution
<a name="API_GetCommandExecution"></a>

Gets information about the specific command execution on a single device.

## Request Syntax
<a name="API_GetCommandExecution_RequestSyntax"></a>

```
GET /command-executions/{{executionId}}?includeResult={{includeResult}}&targetArn={{targetArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCommandExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [executionId](#API_GetCommandExecution_RequestSyntax) **   <a name="iot-GetCommandExecution-request-uri-executionId"></a>
The unique identifier for the command execution. This information is returned as a response of the `StartCommandExecution` API request.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [includeResult](#API_GetCommandExecution_RequestSyntax) **   <a name="iot-GetCommandExecution-request-uri-includeResult"></a>
Can be used to specify whether to include the result of the command execution in the `GetCommandExecution` API response. Your device can use this field to provide additional information about the command execution. You only need to specify this field when using the `AWS-IoT` namespace.

 ** [targetArn](#API_GetCommandExecution_RequestSyntax) **   <a name="iot-GetCommandExecution-request-uri-targetArn"></a>
The Amazon Resource Number (ARN) of the device on which the command execution is being performed.
Length Constraints: Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_GetCommandExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCommandExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "commandArn": "string",
   "completedAt": number,
   "createdAt": number,
   "executionId": "string",
   "executionTimeoutSeconds": number,
   "lastUpdatedAt": number,
   "parameters": {
      "string" : {
         "B": boolean,
         "BIN": blob,
         "D": number,
         "I": number,
         "L": number,
         "S": "string",
         "UL": "string"
      }
   },
   "result": {
      "string" : {
         "B": boolean,
         "BIN": blob,
         "S": "string"
      }
   },
   "startedAt": number,
   "status": "string",
   "statusReason": {
      "reasonCode": "string",
      "reasonDescription": "string"
   },
   "targetArn": "string",
   "timeToLive": number
}
```

## Response Elements
<a name="API_GetCommandExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commandArn](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-commandArn"></a>
The Amazon Resource Number (ARN) of the command. For example, ``arn:aws:iot:<region>:<accountid>:command/<commandId>
Type: String

 ** [completedAt](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-completedAt"></a>
The timestamp, when the command execution was completed.
Type: Timestamp

 ** [createdAt](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-createdAt"></a>
The timestamp, when the command execution was created.
Type: Timestamp

 ** [executionId](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-executionId"></a>
The unique identifier of the command execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [executionTimeoutSeconds](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-executionTimeoutSeconds"></a>
Specifies the amount of time in seconds that the device can take to finish a command execution. A timer starts when the command execution is created. If the command execution status is not set to another terminal state before the timer expires, it will automatically update to `TIMED_OUT`.
Type: Long
Valid Range: Minimum value of 1.

 ** [lastUpdatedAt](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-lastUpdatedAt"></a>
The timestamp, when the command execution was last updated.
Type: Timestamp

 ** [parameters](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-parameters"></a>
The list of parameters that the `StartCommandExecution` API used when performing the command on the device.
Type: String to [CommandParameterValue](API_CommandParameterValue.md) object map
Map Entries: Maximum number of items.
Key Length Constraints: Minimum length of 1. Maximum length of 192.
Key Pattern: `^[.$a-zA-Z0-9_-]+$`

 ** [result](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-result"></a>
The result value for the current state of the command execution. The status provides information about the progress of the command execution. The device can use the result field to share additional details about the execution such as a return value of a remote function call.
If you use the `AWS-IoT-FleetWise` namespace, then this field is not applicable in the API response.
Type: String to [CommandExecutionResult](API_CommandExecutionResult.md) object map
Map Entries: Maximum number of items.
Key Length Constraints: Minimum length of 1. Maximum length of 32.
Key Pattern: `[a-zA-Z0-9_-]+`

 ** [startedAt](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-startedAt"></a>
The timestamp, when the command execution was started.
Type: Timestamp

 ** [status](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-status"></a>
The status of the command execution. After your devices receive the command and start performing the operations specified in the command, it can use the `UpdateCommandExecution` MQTT API to update the status information.
Type: String
Valid Values: `CREATED | IN_PROGRESS | SUCCEEDED | FAILED | REJECTED | TIMED_OUT`

 ** [statusReason](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-statusReason"></a>
Your devices can use this parameter to provide additional context about the status of a command execution using a reason code and description.
Type: [StatusReason](API_StatusReason.md) object

 ** [targetArn](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-targetArn"></a>
The Amazon Resource Number (ARN) of the device on which the command execution is being performed.
Type: String
Length Constraints: Maximum length of 2048.

 ** [timeToLive](#API_GetCommandExecution_ResponseSyntax) **   <a name="iot-GetCommandExecution-response-timeToLive"></a>
The time to live (TTL) parameter that indicates the duration for which executions will be retained in your account. The default value is six months.
Type: Timestamp

## Errors
<a name="API_GetCommandExecution_Errors"></a>

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetCommandExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetCommandExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetCommandExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetCommandExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetCommandExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetCommandExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetCommandExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetCommandExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetCommandExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetCommandExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetCommandExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
