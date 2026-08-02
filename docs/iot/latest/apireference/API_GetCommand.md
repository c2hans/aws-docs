---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetCommand.html
---

# GetCommand
<a name="API_GetCommand"></a>

Gets information about the specified command.

## Request Syntax
<a name="API_GetCommand_RequestSyntax"></a>

```
GET /commands/{{commandId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCommand_RequestParameters"></a>

The request uses the following URI parameters.

 ** [commandId](#API_GetCommand_RequestSyntax) **   <a name="iot-GetCommand-request-uri-commandId"></a>
The unique identifier of the command for which you want to retrieve information.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_GetCommand_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCommand_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "commandArn": "string",
   "commandId": "string",
   "createdAt": number,
   "deprecated": boolean,
   "description": "string",
   "displayName": "string",
   "lastUpdatedAt": number,
   "mandatoryParameters": [
      {
         "defaultValue": {
            "B": boolean,
            "BIN": blob,
            "D": number,
            "I": number,
            "L": number,
            "S": "string",
            "UL": "string"
         },
         "description": "string",
         "name": "string",
         "type": "string",
         "value": {
            "B": boolean,
            "BIN": blob,
            "D": number,
            "I": number,
            "L": number,
            "S": "string",
            "UL": "string"
         },
         "valueConditions": [
            {
               "comparisonOperator": "string",
               "operand": {
                  "number": "string",
                  "numberRange": {
                     "max": "string",
                     "min": "string"
                  },
                  "numbers": [ "string" ],
                  "string": "string",
                  "strings": [ "string" ]
               }
            }
         ]
      }
   ],
   "namespace": "string",
   "payload": {
      "content": blob,
      "contentType": "string"
   },
   "payloadTemplate": "string",
   "pendingDeletion": boolean,
   "preprocessor": {
      "awsJsonSubstitution": {
         "outputFormat": "string"
      }
   },
   "roleArn": "string"
}
```

## Response Elements
<a name="API_GetCommand_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commandArn](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-commandArn"></a>
The Amazon Resource Number (ARN) of the command. For example, `arn:aws:iot:<region>:<accountid>:command/<commandId>`
Type: String

 ** [commandId](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-commandId"></a>
The unique identifier of the command.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [createdAt](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-createdAt"></a>
The timestamp, when the command was created.
Type: Timestamp

 ** [deprecated](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-deprecated"></a>
Indicates whether the command has been deprecated.
Type: Boolean

 ** [description](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-description"></a>
A short text description of the command.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]*`

 ** [displayName](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-displayName"></a>
The user-friendly name in the console for the command.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[^\p{C}]*`

 ** [lastUpdatedAt](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-lastUpdatedAt"></a>
The timestamp, when the command was last updated.
Type: Timestamp

 ** [mandatoryParameters](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-mandatoryParameters"></a>
A list of parameters for the command created.
Type: Array of [CommandParameter](API_CommandParameter.md) objects
Array Members: Minimum number of 1 item.

 ** [namespace](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-namespace"></a>
The namespace of the command.
Type: String
Valid Values: `AWS-IoT | AWS-IoT-FleetWise`

 ** [payload](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-payload"></a>
The payload object that you provided for the command.
Type: [CommandPayload](API_CommandPayload.md) object

 ** [payloadTemplate](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-payloadTemplate"></a>
The payload template for the dynamic command.
Type: String
Length Constraints: Maximum length of 32768.

 ** [pendingDeletion](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-pendingDeletion"></a>
Indicates whether the command is being deleted.
Type: Boolean

 ** [preprocessor](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-preprocessor"></a>
Configuration that determines how `payloadTemplate` is processed to generate command execution payload.
Type: [CommandPreprocessor](API_CommandPreprocessor.md) object

 ** [roleArn](#API_GetCommand_ResponseSyntax) **   <a name="iot-GetCommand-response-roleArn"></a>
The IAM role that you provided when creating the command with `AWS-IoT-FleetWise` as the namespace.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_GetCommand_Errors"></a>

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
<a name="API_GetCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetCommand)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetCommand)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetCommand)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetCommand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetCommand)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetCommand)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetCommand)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetCommand)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetCommand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetCommand)
