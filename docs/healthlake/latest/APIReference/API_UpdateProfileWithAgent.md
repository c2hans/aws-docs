---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_UpdateProfileWithAgent.html
---

# UpdateProfileWithAgent
<a name="API_UpdateProfileWithAgent"></a>

Updates a data transformation profile using chat-based interaction with an agent. Supports multi-turn conversations for iteratively customizing profiles.

## Request Syntax
<a name="API_UpdateProfileWithAgent_RequestSyntax"></a>

```
{
   "ConversationId": "{{string}}",
   "InputMessage": {
      "Body": "{{string}}",
      "Type": "{{string}}"
   },
   "ProfileId": "{{string}}",
   "SourceFormat": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProfileWithAgent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConversationId](#API_UpdateProfileWithAgent_RequestSyntax) **   <a name="HealthLake-UpdateProfileWithAgent-request-ConversationId"></a>
The conversation identifier for multi-turn interactions. Omit to start a new conversation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: No

 ** [InputMessage](#API_UpdateProfileWithAgent_RequestSyntax) **   <a name="HealthLake-UpdateProfileWithAgent-request-InputMessage"></a>
The message to send to the agent.
Type: [AgentInputMessage](API_AgentInputMessage.md) object
Required: Yes

 ** [ProfileId](#API_UpdateProfileWithAgent_RequestSyntax) **   <a name="HealthLake-UpdateProfileWithAgent-request-ProfileId"></a>
The unique identifier of the profile to update via the agent.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** [SourceFormat](#API_UpdateProfileWithAgent_RequestSyntax) **   <a name="HealthLake-UpdateProfileWithAgent-request-SourceFormat"></a>
The source data format for the transformation.
Type: String
Valid Values: `CCDA | CSV`
Required: Yes

## Response Syntax
<a name="API_UpdateProfileWithAgent_ResponseSyntax"></a>

```
{
   "AgentResponse": {
      "Body": "string",
      "OptionsList": [ "string" ],
      "Type": "string"
   },
   "ConversationId": "string"
}
```

## Response Elements
<a name="API_UpdateProfileWithAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentResponse](#API_UpdateProfileWithAgent_ResponseSyntax) **   <a name="HealthLake-UpdateProfileWithAgent-response-AgentResponse"></a>
The response message from the agent.
Type: [AgentOutputMessage](API_AgentOutputMessage.md) object

 ** [ConversationId](#API_UpdateProfileWithAgent_ResponseSyntax) **   <a name="HealthLake-UpdateProfileWithAgent-response-ConversationId"></a>
The conversation identifier to use for follow-up messages in this conversation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.

## Errors
<a name="API_UpdateProfileWithAgent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** AgentMessageOutOfContextException **
The agent message does not fit within the current conversation context. Start a new conversation or provide a message that relates to the current profile customization session.
HTTP Status Code: 400

 ** ConversationNotFoundException **
The specified conversation identifier does not exist. Verify the conversation ID or omit it to start a new conversation.
HTTP Status Code: 400

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** NotImplementedOperationException **
The requested operation is not yet available. Check the service documentation for a list of supported operations.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested data store was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to make this request. Verify that your AWS credentials are valid and that you have the required permissions.
HTTP Status Code: 400

 ** UnsupportedMIMETypeException **
The content type in your request is not supported. Use a supported content type for this operation.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProfileWithAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/UpdateProfileWithAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/UpdateProfileWithAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/UpdateProfileWithAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/UpdateProfileWithAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/UpdateProfileWithAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/UpdateProfileWithAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/UpdateProfileWithAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/UpdateProfileWithAgent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/UpdateProfileWithAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/UpdateProfileWithAgent)
