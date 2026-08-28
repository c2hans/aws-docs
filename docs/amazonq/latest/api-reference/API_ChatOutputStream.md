---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatOutputStream.html
---

# ChatOutputStream
<a name="API_ChatOutputStream"></a>

The streaming output for the `Chat` API.

## Contents
<a name="API_ChatOutputStream_Contents"></a>

 ** actionReviewEvent **   <a name="qbusiness-Type-ChatOutputStream-actionReviewEvent"></a>
A request from Amazon Q Business to the end user for information Amazon Q Business needs to successfully complete a requested plugin action.
Type: [ActionReviewEvent](API_ActionReviewEvent.md) object
Required: No

 ** authChallengeRequestEvent **   <a name="qbusiness-Type-ChatOutputStream-authChallengeRequestEvent"></a>
An authentication verification event activated by an end user request to use a custom plugin.
Type: [AuthChallengeRequestEvent](API_AuthChallengeRequestEvent.md) object
Required: No

 ** failedAttachmentEvent **   <a name="qbusiness-Type-ChatOutputStream-failedAttachmentEvent"></a>
A failed file upload event during a web experience chat.
Type: [FailedAttachmentEvent](API_FailedAttachmentEvent.md) object
Required: No

 ** metadataEvent **   <a name="qbusiness-Type-ChatOutputStream-metadataEvent"></a>
A metadata event for a AI-generated text output message in a Amazon Q Business conversation.
Type: [MetadataEvent](API_MetadataEvent.md) object
Required: No

 ** textEvent **   <a name="qbusiness-Type-ChatOutputStream-textEvent"></a>
Information about the payload of the `ChatOutputStream` event containing the AI-generated message output.
Type: [TextOutputEvent](API_TextOutputEvent.md) object
Required: No

## See Also
<a name="API_ChatOutputStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ChatOutputStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ChatOutputStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ChatOutputStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
