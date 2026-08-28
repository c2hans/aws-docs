---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatSync.html
---

# ChatSync
<a name="API_ChatSync"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Starts or continues a non-streaming Amazon Q Business conversation.

## Request Syntax
<a name="API_ChatSync_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/conversations?sync&userGroups={{userGroups}}&userId={{userId}} HTTP/1.1
Content-type: application/json

{
   "actionExecution": {
      "payload": {
         "{{string}}" : {
            "value": {{JSON value}}
         }
      },
      "payloadFieldNameSeparator": "{{string}}",
      "pluginId": "{{string}}"
   },
   "attachments": [
      {
         "copyFrom": { ... },
         "data": {{blob}},
         "name": "{{string}}"
      }
   ],
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
   "authChallengeResponse": {
      "responseMap": {
         "{{string}}" : "{{string}}"
      }
   },
   "chatMode": "{{string}}",
   "chatModeConfiguration": { ... },
   "clientToken": "{{string}}",
   "conversationId": "{{string}}",
   "parentMessageId": "{{string}}",
   "userMessage": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ChatSync_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application linked to the Amazon Q Business conversation.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [userGroups](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-uri-userGroups"></a>
The group names that a user associated with the chat input belongs to.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [userId](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-uri-userId"></a>
The identifier of the user attached to the chat input.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`

## Request Body
<a name="API_ChatSync_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionExecution](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-actionExecution"></a>
A request from an end user to perform an Amazon Q Business plugin action.
Type: [ActionExecution](API_ActionExecution.md) object
Required: No

 ** [attachments](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-attachments"></a>
A list of files uploaded directly during chat. You can upload a maximum of 5 files of upto 10 MB each.
Type: Array of [AttachmentInput](API_AttachmentInput.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [attributeFilter](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-attributeFilter"></a>
Enables filtering of Amazon Q Business web experience responses based on document attributes or metadata fields.
Type: [AttributeFilter](API_AttributeFilter.md) object
Required: No

 ** [authChallengeResponse](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-authChallengeResponse"></a>
An authentication verification event response by a third party authentication server to Amazon Q Business.
Type: [AuthChallengeResponse](API_AuthChallengeResponse.md) object
Required: No

 ** [chatMode](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-chatMode"></a>
The `chatMode` parameter determines the chat modes available to Amazon Q Business users:
+  `RETRIEVAL_MODE` - If you choose this mode, Amazon Q generates responses solely from the data sources connected and indexed by the application. If an answer is not found in the data sources or there are no data sources available, Amazon Q will respond with a "*No Answer Found*" message, unless LLM knowledge has been enabled. In that case, Amazon Q will generate a response from the LLM knowledge
+  `CREATOR_MODE` - By selecting this mode, you can choose to generate responses only from the LLM knowledge. You can also attach files and have Amazon Q generate a response based on the data in those files. If the attached files do not contain an answer for the query, Amazon Q will automatically fall back to generating a response from the LLM knowledge.
+  `PLUGIN_MODE` - By selecting this mode, users can choose to use plugins in chat to get their responses.
If none of the modes are selected, Amazon Q will only respond using the information from the attached files.
For more information, see [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html), [Plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html), and [Response sources](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html#chat-source-scope).
Type: String
Valid Values: `RETRIEVAL_MODE | CREATOR_MODE | PLUGIN_MODE`
Required: No

 ** [chatModeConfiguration](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-chatModeConfiguration"></a>
The chat mode configuration for an Amazon Q Business application.
Type: [ChatModeConfiguration](API_ChatModeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [clientToken](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-clientToken"></a>
A token that you provide to identify a chat request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [conversationId](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-conversationId"></a>
The identifier of the Amazon Q Business conversation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** [parentMessageId](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-parentMessageId"></a>
The identifier of the previous system message in a conversation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** [userMessage](#API_ChatSync_RequestSyntax) **   <a name="qbusiness-ChatSync-request-userMessage"></a>
A end user message in a conversation.
Type: String
Required: No

## Response Syntax
<a name="API_ChatSync_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionReview": {
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
      "pluginType": "string"
   },
   "authChallengeRequest": {
      "authorizationUrl": "string"
   },
   "conversationId": "string",
   "failedAttachments": [
      {
         "attachmentId": "string",
         "conversationId": "string",
         "error": {
            "errorCode": "string",
            "errorMessage": "string"
         },
         "name": "string",
         "status": "string"
      }
   ],
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
   "systemMessage": "string",
   "systemMessageId": "string",
   "userMessageId": "string"
}
```

## Response Elements
<a name="API_ChatSync_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionReview](#API_ChatSync_ResponseSyntax) **   <a name="qbusiness-ChatSync-response-actionReview"></a>
A request from Amazon Q Business to the end user for information Amazon Q Business needs to successfully complete a requested plugin action.
Type: [ActionReview](API_ActionReview.md) object

 ** [authChallengeRequest](#API_ChatSync_ResponseSyntax) **   <a name="qbusiness-ChatSync-response-authChallengeRequest"></a>
An authentication verification event activated by an end user request to use a custom plugin.
Type: [AuthChallengeRequest](API_AuthChallengeRequest.md) object

 ** [conversationId](#API_ChatSync_ResponseSyntax) **   <a name="qbusiness-ChatSync-response-conversationId"></a>
The identifier of the Amazon Q Business conversation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [failedAttachments](#API_ChatSync_ResponseSyntax) **   <a name="qbusiness-ChatSync-response-failedAttachments"></a>
A list of files which failed to upload during chat.
Type: Array of [AttachmentOutput](API_AttachmentOutput.md) objects

 ** [sourceAttributions](#API_ChatSync_ResponseSyntax) **   <a name="qbusiness-ChatSync-response-sourceAttributions"></a>
The source documents used to generate the conversation response.
Type: Array of [SourceAttribution](API_SourceAttribution.md) objects

 ** [systemMessage](#API_ChatSync_ResponseSyntax) **   <a name="qbusiness-ChatSync-response-systemMessage"></a>
An AI-generated message in a conversation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [systemMessageId](#API_ChatSync_ResponseSyntax) **   <a name="qbusiness-ChatSync-response-systemMessageId"></a>
The identifier of an Amazon Q Business AI generated message within the conversation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [userMessageId](#API_ChatSync_ResponseSyntax) **   <a name="qbusiness-ChatSync-response-userMessageId"></a>
The identifier of an Amazon Q Business end user text input message within the conversation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

## Errors
<a name="API_ChatSync_Errors"></a>

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
<a name="API_ChatSync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/ChatSync)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/ChatSync)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ChatSync)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/ChatSync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ChatSync)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/ChatSync)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/ChatSync)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/ChatSync)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/ChatSync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ChatSync)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
