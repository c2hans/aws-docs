---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListCommandExecutions.html
---

# ListCommandExecutions
<a name="API_ListCommandExecutions"></a>

List all command executions.

**Important**
You must provide only the `startedTimeFilter` or the `completedTimeFilter` information. If you provide both time filters, the API will generate an error. You can use this information to retrieve a list of command executions within a specific timeframe.
You must provide only the `commandArn` or the `thingArn` information depending on whether you want to list executions for a specific command or an IoT thing. If you provide both fields, the API will generate an error.
For more information about considerations for using this API, see [List command executions in your account (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/iot-remote-command-execution-start-monitor.html#iot-remote-command-execution-list-cli).

## Request Syntax
<a name="API_ListCommandExecutions_RequestSyntax"></a>

```
POST /command-executions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "commandArn": "{{string}}",
   "completedTimeFilter": {
      "after": "{{string}}",
      "before": "{{string}}"
   },
   "namespace": "{{string}}",
   "sortOrder": "{{string}}",
   "startedTimeFilter": {
      "after": "{{string}}",
      "before": "{{string}}"
   },
   "status": "{{string}}",
   "targetArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCommandExecutions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListCommandExecutions_RequestSyntax) **   <a name="iot-ListCommandExecutions-request-uri-maxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListCommandExecutions_RequestSyntax) **   <a name="iot-ListCommandExecutions-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise `null` to receive the first set of results.

## Request Body
<a name="API_ListCommandExecutions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [commandArn](#API_ListCommandExecutions_RequestSyntax) **   <a name="iot-ListCommandExecutions-request-commandArn"></a>
The Amazon Resource Number (ARN) of the command. You can use this information to list all command executions for a particular command.
Type: String
Required: No

 ** [completedTimeFilter](#API_ListCommandExecutions_RequestSyntax) **   <a name="iot-ListCommandExecutions-request-completedTimeFilter"></a>
List all command executions that completed any time before or after the date and time that you specify. The date and time uses the format `yyyy-MM-dd'T'HH:mm`.
Type: [TimeFilter](API_TimeFilter.md) object
Required: No

 ** [namespace](#API_ListCommandExecutions_RequestSyntax) **   <a name="iot-ListCommandExecutions-request-namespace"></a>
The namespace of the command.
Type: String
Valid Values: `AWS-IoT | AWS-IoT-FleetWise`
Required: No

 ** [sortOrder](#API_ListCommandExecutions_RequestSyntax) **   <a name="iot-ListCommandExecutions-request-sortOrder"></a>
Specify whether to list the command executions that were created in the ascending or descending order. By default, the API returns all commands in the descending order based on the start time or completion time of the executions, that are determined by the `startTimeFilter` and `completeTimeFilter` parameters.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

 ** [startedTimeFilter](#API_ListCommandExecutions_RequestSyntax) **   <a name="iot-ListCommandExecutions-request-startedTimeFilter"></a>
List all command executions that started any time before or after the date and time that you specify. The date and time uses the format `yyyy-MM-dd'T'HH:mm`.
Type: [TimeFilter](API_TimeFilter.md) object
Required: No

 ** [status](#API_ListCommandExecutions_RequestSyntax) **   <a name="iot-ListCommandExecutions-request-status"></a>
List all command executions for the device that have a particular status. For example, you can filter the list to display only command executions that have failed or timed out.
Type: String
Valid Values: `CREATED | IN_PROGRESS | SUCCEEDED | FAILED | REJECTED | TIMED_OUT`
Required: No

 ** [targetArn](#API_ListCommandExecutions_RequestSyntax) **   <a name="iot-ListCommandExecutions-request-targetArn"></a>
The Amazon Resource Number (ARN) of the target device. You can use this information to list all command executions for a particular device.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListCommandExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "commandExecutions": [
      {
         "commandArn": "string",
         "completedAt": number,
         "createdAt": number,
         "executionId": "string",
         "startedAt": number,
         "status": "string",
         "targetArn": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCommandExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commandExecutions](#API_ListCommandExecutions_ResponseSyntax) **   <a name="iot-ListCommandExecutions-response-commandExecutions"></a>
The list of command executions.
Type: Array of [CommandExecutionSummary](API_CommandExecutionSummary.md) objects

 ** [nextToken](#API_ListCommandExecutions_ResponseSyntax) **   <a name="iot-ListCommandExecutions-response-nextToken"></a>
The token to use to get the next set of results, or `null` if there are no additional results.
Type: String

## Errors
<a name="API_ListCommandExecutions_Errors"></a>

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
<a name="API_ListCommandExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListCommandExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListCommandExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListCommandExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListCommandExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListCommandExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListCommandExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListCommandExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListCommandExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListCommandExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListCommandExecutions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
