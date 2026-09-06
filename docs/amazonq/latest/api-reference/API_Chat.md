---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Chat.html
---

# Chat
<a name="API_Chat"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Starts or continues a streaming Amazon Q Business conversation.

## Request Syntax
<a name="API_Chat_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/conversations?clientToken={{clientToken}}&conversationId={{conversationId}}&parentMessageId={{parentMessageId}}&userGroups={{userGroups}}&userId={{userId}} HTTP/1.1
Content-type: application/json

{
   "actionExecutionEvent": {
      "payload": {
         "{{string}}" : {
            "value": {{JSON value}}
         }
      },
      "payloadFieldNameSeparator": "{{string}}",
      "pluginId": "{{string}}"
   },
   "attachmentEvent": {
      "attachment": {
         "copyFrom": { ... },
         "data": {{blob}},
         "name": "{{string}}"
      }
   },
   "authChallengeResponseEvent": {
      "responseMap": {
         "{{string}}" : "{{string}}"
      }
   },
   "configurationEvent": {
      "attributeFilter": {
         "andAllFilters": [
            "AttributeFilter"
         ],
         "containsAll": {
            "name": "{{string}}",
            "value": { ... }
         },
         "containsAny": {
            "name": "{{string}}",
            "value": { ... }
         },
         "equalsTo": {
            "name": "{{string}}",
            "value": { ... }
         },
         "greaterThan": {
            "name": "{{string}}",
            "value": { ... }
         },
         "greaterThanOrEquals": {
            "name": "{{string}}",
            "value": { ... }
         },
         "lessThan": {
            "name": "{{string}}",
            "value": { ... }
         },
         "lessThanOrEquals": {
            "name": "{{string}}",
            "value": { ... }
         },
         "notFilter": "AttributeFilter",
         "orAllFilters": [
            "AttributeFilter"
         ]
      },
      "chatMode": "{{string}}",
      "chatModeConfiguration": { ... }
   },
   "endOfInputEvent": {
   },
   "textEvent": {
      "userMessage": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_Chat_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application linked to a streaming Amazon Q Business conversation.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [clientToken](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-uri-clientToken"></a>
A token that you provide to identify the chat input.
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [conversationId](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-uri-conversationId"></a>
The identifier of the Amazon Q Business conversation.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [parentMessageId](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-uri-parentMessageId"></a>
The identifier used to associate a user message with a AI generated response.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [userGroups](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-uri-userGroups"></a>
The group names that a user associated with the chat input belongs to.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [userId](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-uri-userId"></a>
The identifier of the user attached to the chat input.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`

## Request Body
<a name="API_Chat_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionExecutionEvent](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-actionExecutionEvent"></a>
A request from an end user to perform an Amazon Q Business plugin action.
Type: [ActionExecutionEvent](API_ActionExecutionEvent.md) object
Required: No

 ** [attachmentEvent](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-attachmentEvent"></a>
A request by an end user to upload a file during chat.
Type: [AttachmentInputEvent](API_AttachmentInputEvent.md) object
Required: No

 ** [authChallengeResponseEvent](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-authChallengeResponseEvent"></a>
An authentication verification event response by a third party authentication server to Amazon Q Business.
Type: [AuthChallengeResponseEvent](API_AuthChallengeResponseEvent.md) object
Required: No

 ** [configurationEvent](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-configurationEvent"></a>
A configuration event activated by an end user request to select a specific chat mode.
Type: [ConfigurationEvent](API_ConfigurationEvent.md) object
Required: No

 ** [endOfInputEvent](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-endOfInputEvent"></a>
The end of the streaming input for the `Chat` API.
Type: [EndOfInputEvent](API_EndOfInputEvent.md) object
Required: No

 ** [textEvent](#API_Chat_RequestSyntax) **   <a name="qbusiness-Chat-request-textEvent"></a>
Information about the payload of the `ChatInputStream` event containing the end user message input.
Type: [TextInputEvent](API_TextInputEvent.md) object
Required: No

## Response Syntax
<a name="API_Chat_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionReviewEvent": {
      "conversationId": "string",
      "payload": {
         "string" : {
            "allowedFormat": "string",
            "allowedValues": [
               {
                  "displayValue": JSON value,
                  "value": JSON value
               }
            ],
            "arrayItemJsonSchema": JSON value,
            "displayDescription": "string",
            "displayName": "string",
            "displayOrder": number,
            "required": boolean,
            "type": "string",
            "value": JSON value
         }
      },
      "payloadFieldNameSeparator": "string",
      "pluginId": "string",
      "pluginType": "string",
      "systemMessageId": "string",
      "userMessageId": "string"
   },
   "authChallengeRequestEvent": {
      "authorizationUrl": "string"
   },
   "failedAttachmentEvent": {
      "attachment": {
         "attachmentId": "string",
         "conversationId": "string",
         "error": {
            "errorCode": "string",
            "errorMessage": "string"
         },
         "name": "string",
         "status": "string"
      },
      "conversationId": "string",
      "systemMessageId": "string",
      "userMessageId": "string"
   },
   "metadataEvent": {
      "conversationId": "string",
      "finalTextMessage": "string",
      "sourceAttributions": [
         {
            "citationNumber": number,
            "datasourceId": "string",
            "documentId": "string",
            "indexId": "string",
            "snippet": "string",
            "textMessageSegments": [
               {
                  "beginOffset": number,
                  "endOffset": number,
                  "mediaId": "string",
                  "mediaMimeType": "string",
                  "snippetExcerpt": {
                     "text": "string"
                  },
                  "sourceDetails": { ... }
               }
            ],
            "title": "string",
            "updatedAt": number,
            "url": "string"
         }
      ],
      "systemMessageId": "string",
      "userMessageId": "string"
   },
   "textEvent": {
      "conversationId": "string",
      "systemMessage": "string",
      "systemMessageId": "string",
      "systemMessageType": "string",
      "userMessageId": "string"
   }
}
```

## Response Elements
<a name="API_Chat_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionReviewEvent](#API_Chat_ResponseSyntax) **   <a name="qbusiness-Chat-response-actionReviewEvent"></a>
A request from Amazon Q Business to the end user for information Amazon Q Business needs to successfully complete a requested plugin action.
Type: [ActionReviewEvent](API_ActionReviewEvent.md) object

 ** [authChallengeRequestEvent](#API_Chat_ResponseSyntax) **   <a name="qbusiness-Chat-response-authChallengeRequestEvent"></a>
An authentication verification event activated by an end user request to use a custom plugin.
Type: [AuthChallengeRequestEvent](API_AuthChallengeRequestEvent.md) object

 ** [failedAttachmentEvent](#API_Chat_ResponseSyntax) **   <a name="qbusiness-Chat-response-failedAttachmentEvent"></a>
A failed file upload event during a web experience chat.
Type: [FailedAttachmentEvent](API_FailedAttachmentEvent.md) object

 ** [metadataEvent](#API_Chat_ResponseSyntax) **   <a name="qbusiness-Chat-response-metadataEvent"></a>
A metadata event for a AI-generated text output message in a Amazon Q Business conversation.
Type: [MetadataEvent](API_MetadataEvent.md) object

 ** [textEvent](#API_Chat_ResponseSyntax) **   <a name="qbusiness-Chat-response-textEvent"></a>
Information about the payload of the `ChatOutputStream` event containing the AI-generated message output.
Type: [TextOutputEvent](API_TextOutputEvent.md) object

## Errors
<a name="API_Chat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** ConflictException **
You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.
 ** message **
The message describing a `ConflictException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 409

 ** ExternalResourceException **
An external resource that you configured with your application is returning errors and preventing this operation from succeeding. Fix those errors and try again.
HTTP Status Code: 424

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** LicenseNotFoundException **
You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_Chat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/Chat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/Chat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/Chat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/Chat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/Chat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/Chat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/Chat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/Chat)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/Chat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/Chat)
