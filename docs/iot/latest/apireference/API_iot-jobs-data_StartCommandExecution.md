---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_StartCommandExecution.html
---

# StartCommandExecution
<a name="API_iot-jobs-data_StartCommandExecution"></a>

Using the command created with the `CreateCommand` API, start a command execution on a specific device.

**Note**
The IAM permissions are derived from the `iot:StartCommandExecution` action. For more information on the IAM permissions policy statement, see [Start a command execution (AWS CLI) > Sample IAM policy](https://docs.aws.amazon.com/iot/latest/developerguide/iot-remote-command-execution-start-monitor.html#iot-remote-command-execution-start).

## Request Syntax
<a name="API_iot-jobs-data_StartCommandExecution_RequestSyntax"></a>

```
POST /command-executions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "commandArn": "{{string}}",
   "executionTimeoutSeconds": {{number}},
   "parameters": {
      "{{string}}" : {
         "B": {{boolean}},
         "BIN": {{blob}},
         "D": {{number}},
         "I": {{number}},
         "L": {{number}},
         "S": "{{string}}",
         "UL": "{{string}}"
      }
   },
   "targetArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_iot-jobs-data_StartCommandExecution_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_iot-jobs-data_StartCommandExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_iot-jobs-data_StartCommandExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_StartCommandExecution-request-clientToken"></a>
The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you retry the request using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[\x21-\x7E]+$`
Required: No

 ** [commandArn](#API_iot-jobs-data_StartCommandExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_StartCommandExecution-request-commandArn"></a>
The Amazon Resource Number (ARN) of the command. For example, `arn:aws:iot:<region>:<accountid>:command/<commandName>`
Type: String
Required: Yes

 ** [executionTimeoutSeconds](#API_iot-jobs-data_StartCommandExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_StartCommandExecution-request-executionTimeoutSeconds"></a>
Specifies the amount of time in second the device has to finish the command execution. A timer is started as soon as the command execution is created. If the command execution status is not set to another terminal state before the timer expires, it will automatically update to `TIMED_OUT`.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** [parameters](#API_iot-jobs-data_StartCommandExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_StartCommandExecution-request-parameters"></a>
A list of parameters that are required by the `StartCommandExecution` API when performing the command on a device.
Type: String to [CommandParameterValue](API_iot-jobs-data_CommandParameterValue.md) object map
Map Entries: Maximum number of items.
Key Length Constraints: Minimum length of 1. Maximum length of 192.
Key Pattern: `^[.$a-zA-Z0-9_-]+$`
Required: No

 ** [targetArn](#API_iot-jobs-data_StartCommandExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_StartCommandExecution-request-targetArn"></a>
The Amazon Resource Number (ARN) of the device where the command execution is occurring.
Type: String
Length Constraints: Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_iot-jobs-data_StartCommandExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "executionId": "string"
}
```

## Response Elements
<a name="API_iot-jobs-data_StartCommandExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionId](#API_iot-jobs-data_StartCommandExecution_ResponseSyntax) **   <a name="iot-iot-jobs-data_StartCommandExecution-response-executionId"></a>
A unique identifier for the command execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_iot-jobs-data_StartCommandExecution_Errors"></a>

 ** ConflictException **
A conflict has occurred when performing the API request.
 ** resourceId **
A conflict occurred while performing the API request on the resource ID.
HTTP Status Code: 409

 ** InternalServerException **
An internal server error occurred when performing the API request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded for this request.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message associated with the exception.
 ** payload **
The payload associated with the exception.
HTTP Status Code: 400

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_iot-jobs-data_StartCommandExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-jobs-data-2017-09-29/StartCommandExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-jobs-data-2017-09-29/StartCommandExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-jobs-data-2017-09-29/StartCommandExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-jobs-data-2017-09-29/StartCommandExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-jobs-data-2017-09-29/StartCommandExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-jobs-data-2017-09-29/StartCommandExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-jobs-data-2017-09-29/StartCommandExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-jobs-data-2017-09-29/StartCommandExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-jobs-data-2017-09-29/StartCommandExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-jobs-data-2017-09-29/StartCommandExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
