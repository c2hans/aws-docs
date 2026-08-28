---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCommand.html
---

# CreateCommand
<a name="API_CreateCommand"></a>

Creates a command. A command contains reusable configurations that can be applied before they are sent to the devices.

## Request Syntax
<a name="API_CreateCommand_RequestSyntax"></a>

```
PUT /commands/{{commandId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "displayName": "{{string}}",
   "mandatoryParameters": [
      {
         "defaultValue": {
            "B": {{boolean}},
            "BIN": {{blob}},
            "D": {{number}},
            "I": {{number}},
            "L": {{number}},
            "S": "{{string}}",
            "UL": "{{string}}"
         },
         "description": "{{string}}",
         "name": "{{string}}",
         "type": "{{string}}",
         "value": {
            "B": {{boolean}},
            "BIN": {{blob}},
            "D": {{number}},
            "I": {{number}},
            "L": {{number}},
            "S": "{{string}}",
            "UL": "{{string}}"
         },
         "valueConditions": [
            {
               "comparisonOperator": "{{string}}",
               "operand": {
                  "number": "{{string}}",
                  "numberRange": {
                     "max": "{{string}}",
                     "min": "{{string}}"
                  },
                  "numbers": [ "{{string}}" ],
                  "string": "{{string}}",
                  "strings": [ "{{string}}" ]
               }
            }
         ]
      }
   ],
   "namespace": "{{string}}",
   "payload": {
      "content": {{blob}},
      "contentType": "{{string}}"
   },
   "payloadTemplate": "{{string}}",
   "preprocessor": {
      "awsJsonSubstitution": {
         "outputFormat": "{{string}}"
      }
   },
   "roleArn": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateCommand_RequestParameters"></a>

The request uses the following URI parameters.

 ** [commandId](#API_CreateCommand_RequestSyntax) **   <a name="iot-CreateCommand-request-uri-commandId"></a>
A unique identifier for the command. We recommend using UUID. Alpha-numeric characters, hyphens, and underscores are valid for use here.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_CreateCommand_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateCommand_RequestSyntax) **   <a name="iot-CreateCommand-request-description"></a>
A short text decription of the command.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]*`
Required: No

 ** [displayName](#API_CreateCommand_RequestSyntax) **   <a name="iot-CreateCommand-request-displayName"></a>
The user-friendly name in the console for the command. This name doesn't have to be unique. You can update the user-friendly name after you define it.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[^\p{C}]*`
Required: No

 ** [mandatoryParameters](#API_CreateCommand_RequestSyntax) **   <a name="iot-CreateCommand-request-mandatoryParameters"></a>
A list of parameters that are used by `StartCommandExecution` API for execution payload generation.
Type: Array of [CommandParameter](API_CommandParameter.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [namespace](#API_CreateCommand_RequestSyntax) **   <a name="iot-CreateCommand-request-namespace"></a>
The namespace of the command. The MQTT reserved topics and validations will be used for command executions according to the namespace setting.
Type: String
Valid Values: `AWS-IoT | AWS-IoT-FleetWise`
Required: No

 ** [payload](#API_CreateCommand_RequestSyntax) **   <a name="iot-CreateCommand-request-payload"></a>
The payload object for the static command.
You can upload a static payload file from your local storage that contains the instructions for the device to process. The payload file can use any format. To make sure that the device correctly interprets the payload, we recommend you to specify the payload content type.
Type: [CommandPayload](API_CommandPayload.md) object
Required: No

 ** [payloadTemplate](#API_CreateCommand_RequestSyntax) **   <a name="iot-CreateCommand-request-payloadTemplate"></a>
The payload template for the dynamic command.
This parameter is required for dynamic commands where the command execution placeholders are supplied either from `mandatoryParameters` or when `StartCommandExecution` is invoked.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** [preprocessor](#API_CreateCommand_RequestSyntax) **   <a name="iot-CreateCommand-request-preprocessor"></a>
Configuration that determines how `payloadTemplate` is processed to generate command execution payload.
This parameter is required for dynamic commands, along with `payloadTemplate`, and `mandatoryParameters`.
Type: [CommandPreprocessor](API_CommandPreprocessor.md) object
Required: No

 ** [roleArn](#API_CreateCommand_RequestSyntax) **   <a name="iot-CreateCommand-request-roleArn"></a>
The IAM role that you must provide when using the `AWS-IoT-FleetWise` namespace. The role grants IoT Device Management the permission to access IoT FleetWise resources for generating the payload for the command. This field is not supported when you use the `AWS-IoT` namespace.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [tags](#API_CreateCommand_RequestSyntax) **   <a name="iot-CreateCommand-request-tags"></a>
Name-value pairs that are used as metadata to manage a command.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateCommand_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "commandArn": "string",
   "commandId": "string"
}
```

## Response Elements
<a name="API_CreateCommand_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commandArn](#API_CreateCommand_ResponseSyntax) **   <a name="iot-CreateCommand-response-commandArn"></a>
The Amazon Resource Number (ARN) of the command. For example, `arn:aws:iot:<region>:<accountid>:command/<commandId>`
Type: String

 ** [commandId](#API_CreateCommand_ResponseSyntax) **   <a name="iot-CreateCommand-response-commandId"></a>
The unique identifier for the command.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_CreateCommand_Errors"></a>

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
A resource with the same name already exists.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Service quota has been exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateCommand)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateCommand)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateCommand)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateCommand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateCommand)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateCommand)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateCommand)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateCommand)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateCommand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateCommand)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
