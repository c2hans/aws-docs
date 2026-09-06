---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PersistentChat.html
---

# PersistentChat
<a name="API_PersistentChat"></a>

Enable persistent chats. For more information about enabling persistent chat, and for example use cases and how to configure for them, see [Enable persistent chat](https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html).

## Contents
<a name="API_PersistentChat_Contents"></a>

 ** RehydrationType **   <a name="connect-Type-PersistentChat-RehydrationType"></a>
The contactId that is used for rehydration depends on the rehydration type. RehydrationType is required for persistent chat.
+  `ENTIRE_PAST_SESSION`: Rehydrates a chat from the most recently terminated past chat contact of the specified past ended chat session. To use this type, provide the `initialContactId` of the past ended chat session in the `sourceContactId` field. In this type, Connect Customer determines the most recent chat contact on the specified chat session that has ended, and uses it to start a persistent chat.
+  `FROM_SEGMENT`: Rehydrates a chat from the past chat contact that is specified in the `sourceContactId` field.
The actual contactId used for rehydration is provided in the response of this API.
Type: String
Valid Values: `ENTIRE_PAST_SESSION | FROM_SEGMENT`
Required: No

 ** SourceContactId **   <a name="connect-Type-PersistentChat-SourceContactId"></a>
The contactId from which a persistent chat session must be started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_PersistentChat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PersistentChat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PersistentChat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PersistentChat)
