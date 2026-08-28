---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_GetTranscript.html
---

# GetTranscript
<a name="API_connect-participant_GetTranscript"></a>

Retrieves a transcript of the session, including details about any attachments. For information about accessing past chat contact transcripts for a persistent chat, see [Enable persistent chat](https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html).

For security recommendations, see [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat).

If you have a process that consumes events in the transcript of an chat that has ended, note that chat transcripts contain the following event content types if the event has occurred during the chat session:
+  `application/vnd.amazonaws.connect.event.participant.invited`
+  `application/vnd.amazonaws.connect.event.participant.joined`
+  `application/vnd.amazonaws.connect.event.participant.left`
+  `application/vnd.amazonaws.connect.event.chat.ended`
+  `application/vnd.amazonaws.connect.event.transfer.succeeded`
+  `application/vnd.amazonaws.connect.event.transfer.failed`

**Note**
 `ConnectionToken` is used for invoking this API instead of `ParticipantToken`.

The Amazon Connect Participant Service APIs do not use [Signature Version 4 authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Request Syntax
<a name="API_connect-participant_GetTranscript_RequestSyntax"></a>

```
POST /participant/transcript HTTP/1.1
X-Amz-Bearer: {{ConnectionToken}}
Content-type: application/json

{
   "ContactId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ScanDirection": "{{string}}",
   "SortOrder": "{{string}}",
   "StartPosition": {
      "AbsoluteTime": "{{string}}",
      "Id": "{{string}}",
      "MostRecent": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_connect-participant_GetTranscript_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionToken](#API_connect-participant_GetTranscript_RequestSyntax) **   <a name="connect-connect-participant_GetTranscript-request-ConnectionToken"></a>
The authentication token associated with the participant's connection.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_connect-participant_GetTranscript_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContactId](#API_connect-participant_GetTranscript_RequestSyntax) **   <a name="connect-connect-participant_GetTranscript-request-ContactId"></a>
The contactId from the current contact chain for which transcript is needed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [MaxResults](#API_connect-participant_GetTranscript_RequestSyntax) **   <a name="connect-connect-participant_GetTranscript-request-MaxResults"></a>
The maximum number of results to return in the page. Default: 10.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_connect-participant_GetTranscript_RequestSyntax) **   <a name="connect-connect-participant_GetTranscript-request-NextToken"></a>
The pagination token. Use the value returned previously in the next subsequent request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [ScanDirection](#API_connect-participant_GetTranscript_RequestSyntax) **   <a name="connect-connect-participant_GetTranscript-request-ScanDirection"></a>
The direction from StartPosition from which to retrieve message. Default: BACKWARD when no StartPosition is provided, FORWARD with StartPosition.
Type: String
Valid Values: `FORWARD | BACKWARD`
Required: No

 ** [SortOrder](#API_connect-participant_GetTranscript_RequestSyntax) **   <a name="connect-connect-participant_GetTranscript-request-SortOrder"></a>
The sort order for the records. Default: DESCENDING.
Type: String
Valid Values: `DESCENDING | ASCENDING`
Required: No

 ** [StartPosition](#API_connect-participant_GetTranscript_RequestSyntax) **   <a name="connect-connect-participant_GetTranscript-request-StartPosition"></a>
A filtering option for where to start.
Type: [StartPosition](API_connect-participant_StartPosition.md) object
Required: No

## Response Syntax
<a name="API_connect-participant_GetTranscript_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InitialContactId": "string",
   "NextToken": "string",
   "Transcript": [
      {
         "AbsoluteTime": "string",
         "Attachments": [
            {
               "AttachmentId": "string",
               "AttachmentName": "string",
               "ContentType": "string",
               "Status": "string"
            }
         ],
         "ContactId": "string",
         "Content": "string",
         "ContentType": "string",
         "DisplayName": "string",
         "Id": "string",
         "MessageMetadata": {
            "MessageId": "string",
            "MessageProcessingStatus": "string",
            "Receipts": [
               {
                  "DeliveredTimestamp": "string",
                  "ReadTimestamp": "string",
                  "RecipientParticipantId": "string"
               }
            ]
         },
         "ParticipantId": "string",
         "ParticipantRole": "string",
         "RelatedContactId": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-participant_GetTranscript_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InitialContactId](#API_connect-participant_GetTranscript_ResponseSyntax) **   <a name="connect-connect-participant_GetTranscript-response-InitialContactId"></a>
The initial contact ID for the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [NextToken](#API_connect-participant_GetTranscript_ResponseSyntax) **   <a name="connect-connect-participant_GetTranscript-response-NextToken"></a>
The pagination token. Use the value returned previously in the next subsequent request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [Transcript](#API_connect-participant_GetTranscript_ResponseSyntax) **   <a name="connect-connect-participant_GetTranscript-response-Transcript"></a>
The list of messages in the session.
Type: Array of [Item](API_connect-participant_Item.md) objects

## Errors
<a name="API_connect-participant_GetTranscript_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the Amazon Connect service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by Amazon Connect.
HTTP Status Code: 400

## See Also
<a name="API_connect-participant_GetTranscript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectparticipant-2018-09-07/GetTranscript)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectparticipant-2018-09-07/GetTranscript)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/GetTranscript)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectparticipant-2018-09-07/GetTranscript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/GetTranscript)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectparticipant-2018-09-07/GetTranscript)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectparticipant-2018-09-07/GetTranscript)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectparticipant-2018-09-07/GetTranscript)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectparticipant-2018-09-07/GetTranscript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/GetTranscript)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
