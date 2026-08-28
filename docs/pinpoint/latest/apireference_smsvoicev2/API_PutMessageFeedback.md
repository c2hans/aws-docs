---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutMessageFeedback.html
---

# PutMessageFeedback
<a name="API_PutMessageFeedback"></a>

Set the MessageFeedbackStatus as `RECEIVED` or `FAILED` for the passed in MessageId.

If you use message feedback then you must update message feedback record. When you receive a signal that a user has received the message you must use `PutMessageFeedback` to set the message feedback record as `RECEIVED`; Otherwise, an hour after the message feedback record is set to `FAILED`.

## Request Syntax
<a name="API_PutMessageFeedback_RequestSyntax"></a>

```
{
   "MessageFeedbackStatus": "{{string}}",
   "MessageId": "{{string}}"
}
```

## Request Parameters
<a name="API_PutMessageFeedback_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MessageFeedbackStatus](#API_PutMessageFeedback_RequestSyntax) **   <a name="pinpoint-PutMessageFeedback-request-MessageFeedbackStatus"></a>
Set the message feedback to be either `RECEIVED` or `FAILED`.
Type: String
Valid Values: `RECEIVED | FAILED`
Required: Yes

 ** [MessageId](#API_PutMessageFeedback_RequestSyntax) **   <a name="pinpoint-PutMessageFeedback-request-MessageId"></a>
The unique identifier for the message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_PutMessageFeedback_ResponseSyntax"></a>

```
{
   "MessageFeedbackStatus": "string",
   "MessageId": "string"
}
```

## Response Elements
<a name="API_PutMessageFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MessageFeedbackStatus](#API_PutMessageFeedback_ResponseSyntax) **   <a name="pinpoint-PutMessageFeedback-response-MessageFeedbackStatus"></a>
The current status of the message.
Type: String
Valid Values: `RECEIVED | FAILED`

 ** [MessageId](#API_PutMessageFeedback_ResponseSyntax) **   <a name="pinpoint-PutMessageFeedback-response-MessageId"></a>
The unique identifier for the message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_:/-]+`

## Errors
<a name="API_PutMessageFeedback_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_PutMessageFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/PutMessageFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/PutMessageFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/PutMessageFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/PutMessageFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/PutMessageFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/PutMessageFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/PutMessageFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/PutMessageFeedback)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/PutMessageFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/PutMessageFeedback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
