---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConversationLevelResultDetail.html
---

# ConversationLevelResultDetail
<a name="API_ConversationLevelResultDetail"></a>

The conversation level details of the conversation used in the test set.

## Contents
<a name="API_ConversationLevelResultDetail_Contents"></a>

 ** endToEndResult **   <a name="lexv2-Type-ConversationLevelResultDetail-endToEndResult"></a>
The success or failure of the streaming of the conversation.
Type: String
Valid Values: `Matched | Mismatched | ExecutionError`
Required: Yes

 ** speechTranscriptionResult **   <a name="lexv2-Type-ConversationLevelResultDetail-speechTranscriptionResult"></a>
The speech transcription success or failure details of the conversation.
Type: String
Valid Values: `Matched | Mismatched | ExecutionError`
Required: No

## See Also
<a name="API_ConversationLevelResultDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ConversationLevelResultDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ConversationLevelResultDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ConversationLevelResultDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
