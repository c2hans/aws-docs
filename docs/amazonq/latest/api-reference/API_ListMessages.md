---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListMessages.html
---

# ListMessages
<a name="API_ListMessages"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Gets a list of messages associated with an Amazon Q Business web experience.

## Request Syntax
<a name="API_ListMessages_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/conversations/{{conversationId}}?maxResults={{maxResults}}&nextToken={{nextToken}}&userId={{userId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMessages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListMessages_RequestSyntax) **   <a name="qbusiness-ListMessages-request-uri-applicationId"></a>
The identifier for the Amazon Q Business application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [conversationId](#API_ListMessages_RequestSyntax) **   <a name="qbusiness-ListMessages-request-uri-conversationId"></a>
The identifier of the Amazon Q Business web experience conversation.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [maxResults](#API_ListMessages_RequestSyntax) **   <a name="qbusiness-ListMessages-request-uri-maxResults"></a>
The maximum number of messages to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListMessages_RequestSyntax) **   <a name="qbusiness-ListMessages-request-uri-nextToken"></a>
If the number of messages returned exceeds `maxResults`, Amazon Q Business returns a next token as a pagination token to retrieve the next set of messages.
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [userId](#API_ListMessages_RequestSyntax) **   <a name="qbusiness-ListMessages-request-uri-userId"></a>
The identifier of the user involved in the Amazon Q Business web experience conversation.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`

## Request Body
<a name="API_ListMessages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMessages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "messages": [
      {
         "actionExecution": {
            "payload": {
               "string" : {
                  "value": JSON value
               }
            },
            "payloadFieldNameSeparator": "string",
            "pluginId": "string"
         },
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
         "attachments": [
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
         "body": "string",
         "messageId": "string",
         "sourceAttribution": [
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
         "time": number,
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMessages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messages](#API_ListMessages_ResponseSyntax) **   <a name="qbusiness-ListMessages-response-messages"></a>
An array of information on one or more messages.
Type: Array of [Message](API_Message.md) objects

 ** [nextToken](#API_ListMessages_ResponseSyntax) **   <a name="qbusiness-ListMessages-response-nextToken"></a>
If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of messages.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

## Errors
<a name="API_ListMessages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

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
<a name="API_ListMessages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/ListMessages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/ListMessages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ListMessages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/ListMessages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ListMessages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/ListMessages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/ListMessages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/ListMessages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/ListMessages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ListMessages)
