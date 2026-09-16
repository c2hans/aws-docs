---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCommand.html
---

# UpdateCommand
<a name="API_UpdateCommand"></a>

Update information about a command or mark a command for deprecation.

## Request Syntax
<a name="API_UpdateCommand_RequestSyntax"></a>

```
PATCH /commands/{{commandId}} HTTP/1.1
Content-type: application/json

{
   "deprecated": {{boolean}},
   "description": "{{string}}",
   "displayName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCommand_RequestParameters"></a>

The request uses the following URI parameters.

 ** [commandId](#API_UpdateCommand_RequestSyntax) **   <a name="iot-UpdateCommand-request-uri-commandId"></a>
The unique identifier of the command to be updated.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_UpdateCommand_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deprecated](#API_UpdateCommand_RequestSyntax) **   <a name="iot-UpdateCommand-request-deprecated"></a>
A boolean that you can use to specify whether to deprecate a command.
Type: Boolean
Required: No

 ** [description](#API_UpdateCommand_RequestSyntax) **   <a name="iot-UpdateCommand-request-description"></a>
A short text description of the command.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]*`
Required: No

 ** [displayName](#API_UpdateCommand_RequestSyntax) **   <a name="iot-UpdateCommand-request-displayName"></a>
The new user-friendly name to use in the console for the command.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[^\p{C}]*`
Required: No

## Response Syntax
<a name="API_UpdateCommand_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "commandId": "string",
   "deprecated": boolean,
   "description": "string",
   "displayName": "string",
   "lastUpdatedAt": number
}
```

## Response Elements
<a name="API_UpdateCommand_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commandId](#API_UpdateCommand_ResponseSyntax) **   <a name="iot-UpdateCommand-response-commandId"></a>
The unique identifier of the command.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [deprecated](#API_UpdateCommand_ResponseSyntax) **   <a name="iot-UpdateCommand-response-deprecated"></a>
The boolean that indicates whether the command was deprecated.
Type: Boolean

 ** [description](#API_UpdateCommand_ResponseSyntax) **   <a name="iot-UpdateCommand-response-description"></a>
The updated text description of the command.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]*`

 ** [displayName](#API_UpdateCommand_ResponseSyntax) **   <a name="iot-UpdateCommand-response-displayName"></a>
The updated user-friendly display name in the console for the command.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[^\p{C}]*`

 ** [lastUpdatedAt](#API_UpdateCommand_ResponseSyntax) **   <a name="iot-UpdateCommand-response-lastUpdatedAt"></a>
The date and time (epoch timestamp in seconds) when the command was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateCommand_Errors"></a>

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
A resource with the same name already exists.
HTTP Status Code: 409

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
<a name="API_UpdateCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateCommand)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateCommand)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateCommand)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateCommand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateCommand)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateCommand)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateCommand)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateCommand)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateCommand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateCommand)
