---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ConversationSource.html
---

# ConversationSource
<a name="API_ConversationSource"></a>

The source reference for an existing attachment in an existing conversation.

## Contents
<a name="API_ConversationSource_Contents"></a>

 ** attachmentId **   <a name="qbusiness-Type-ConversationSource-attachmentId"></a>
The unique identifier of the Amazon Q Business attachment.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** conversationId **   <a name="qbusiness-Type-ConversationSource-conversationId"></a>
The unique identifier of the Amazon Q Business conversation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## See Also
<a name="API_ConversationSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ConversationSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ConversationSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ConversationSource)
