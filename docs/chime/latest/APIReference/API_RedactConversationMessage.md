---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_RedactConversationMessage.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# RedactConversationMessage
<a name="API_RedactConversationMessage"></a>

Redacts the specified message from the specified Amazon Chime conversation.

## Request Syntax
<a name="API_RedactConversationMessage_RequestSyntax"></a>

```
POST /accounts/{{accountId}}/conversations/{{conversationId}}/messages/{messageId}?operation=redact HTTP/1.1
```

## URI Request Parameters
<a name="API_RedactConversationMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_RedactConversationMessage_RequestSyntax) **   <a name="chime-RedactConversationMessage-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

 ** [conversationId](#API_RedactConversationMessage_RequestSyntax) **   <a name="chime-RedactConversationMessage-request-uri-ConversationId"></a>
The conversation ID.
Pattern: `.*\S.*`
Required: Yes

 ** [messageId](#API_RedactConversationMessage_RequestSyntax) **   <a name="chime-RedactConversationMessage-request-uri-MessageId"></a>
The message ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_RedactConversationMessage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RedactConversationMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_RedactConversationMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RedactConversationMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_RedactConversationMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/RedactConversationMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/RedactConversationMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/RedactConversationMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/RedactConversationMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/RedactConversationMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/RedactConversationMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/RedactConversationMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/RedactConversationMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/RedactConversationMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/RedactConversationMessage)
