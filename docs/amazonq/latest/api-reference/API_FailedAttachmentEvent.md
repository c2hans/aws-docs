---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_FailedAttachmentEvent.html
---

# FailedAttachmentEvent
<a name="API_FailedAttachmentEvent"></a>

A failed file upload during web experience chat.

## Contents
<a name="API_FailedAttachmentEvent_Contents"></a>

 ** attachment **   <a name="qbusiness-Type-FailedAttachmentEvent-attachment"></a>
The details of a file uploaded during chat.
Type: [AttachmentOutput](API_AttachmentOutput.md) object
Required: No

 ** conversationId **   <a name="qbusiness-Type-FailedAttachmentEvent-conversationId"></a>
 The identifier of the conversation associated with the failed file upload.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** systemMessageId **   <a name="qbusiness-Type-FailedAttachmentEvent-systemMessageId"></a>
The identifier of the AI-generated message associated with the file upload.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** userMessageId **   <a name="qbusiness-Type-FailedAttachmentEvent-userMessageId"></a>
The identifier of the end user chat message associated with the file upload.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

## See Also
<a name="API_FailedAttachmentEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/FailedAttachmentEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/FailedAttachmentEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/FailedAttachmentEvent)
