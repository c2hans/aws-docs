---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatInputStream.html
---

# ChatInputStream
<a name="API_ChatInputStream"></a>

The streaming input for the `Chat` API.

## Contents
<a name="API_ChatInputStream_Contents"></a>

 ** actionExecutionEvent **   <a name="qbusiness-Type-ChatInputStream-actionExecutionEvent"></a>
A request from an end user to perform an Amazon Q Business plugin action.
Type: [ActionExecutionEvent](API_ActionExecutionEvent.md) object
Required: No

 ** attachmentEvent **   <a name="qbusiness-Type-ChatInputStream-attachmentEvent"></a>
A request by an end user to upload a file during chat.
Type: [AttachmentInputEvent](API_AttachmentInputEvent.md) object
Required: No

 ** authChallengeResponseEvent **   <a name="qbusiness-Type-ChatInputStream-authChallengeResponseEvent"></a>
An authentication verification event response by a third party authentication server to Amazon Q Business.
Type: [AuthChallengeResponseEvent](API_AuthChallengeResponseEvent.md) object
Required: No

 ** configurationEvent **   <a name="qbusiness-Type-ChatInputStream-configurationEvent"></a>
A configuration event activated by an end user request to select a specific chat mode.
Type: [ConfigurationEvent](API_ConfigurationEvent.md) object
Required: No

 ** endOfInputEvent **   <a name="qbusiness-Type-ChatInputStream-endOfInputEvent"></a>
The end of the streaming input for the `Chat` API.
Type: [EndOfInputEvent](API_EndOfInputEvent.md) object
Required: No

 ** textEvent **   <a name="qbusiness-Type-ChatInputStream-textEvent"></a>
Information about the payload of the `ChatInputStream` event containing the end user message input.
Type: [TextInputEvent](API_TextInputEvent.md) object
Required: No

## See Also
<a name="API_ChatInputStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ChatInputStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ChatInputStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ChatInputStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
