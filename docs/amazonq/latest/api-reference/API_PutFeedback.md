---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutFeedback.html
---

# PutFeedback
<a name="API_PutFeedback"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Enables your end user to provide feedback on their Amazon Q Business generated chat responses.

## Request Syntax
<a name="API_PutFeedback_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/conversations/{{conversationId}}/messages/{{messageId}}/feedback?userId={{userId}} HTTP/1.1
Content-type: application/json

{
   "messageCopiedAt": {{number}},
   "messageUsefulness": {
      "comment": "{{string}}",
      "reason": "{{string}}",
      "submittedAt": {{number}},
      "usefulness": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_PutFeedback_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_PutFeedback_RequestSyntax) **   <a name="qbusiness-PutFeedback-request-uri-applicationId"></a>
The identifier of the application associated with the feedback.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [conversationId](#API_PutFeedback_RequestSyntax) **   <a name="qbusiness-PutFeedback-request-uri-conversationId"></a>
The identifier of the conversation the feedback is attached to.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [messageId](#API_PutFeedback_RequestSyntax) **   <a name="qbusiness-PutFeedback-request-uri-messageId"></a>
The identifier of the chat message that the feedback was given for.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [userId](#API_PutFeedback_RequestSyntax) **   <a name="qbusiness-PutFeedback-request-uri-userId"></a>
The identifier of the user giving the feedback.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`

## Request Body
<a name="API_PutFeedback_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [messageCopiedAt](#API_PutFeedback_RequestSyntax) **   <a name="qbusiness-PutFeedback-request-messageCopiedAt"></a>
The timestamp for when the feedback was recorded.
Type: Timestamp
Required: No

 ** [messageUsefulness](#API_PutFeedback_RequestSyntax) **   <a name="qbusiness-PutFeedback-request-messageUsefulness"></a>
The feedback usefulness value given by the user to the chat message.
Type: [MessageUsefulnessFeedback](API_MessageUsefulnessFeedback.md) object
Required: No

## Response Syntax
<a name="API_PutFeedback_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutFeedback_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

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
<a name="API_PutFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/PutFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/PutFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/PutFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/PutFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/PutFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/PutFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/PutFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/PutFeedback)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/PutFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/PutFeedback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
