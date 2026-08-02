---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConversationLevelSlotResolutionResultItem.html
---

# ConversationLevelSlotResolutionResultItem
<a name="API_ConversationLevelSlotResolutionResultItem"></a>

The slots used for the slot resolution in the conversation.

## Contents
<a name="API_ConversationLevelSlotResolutionResultItem_Contents"></a>

 ** intentName **   <a name="lexv2-Type-ConversationLevelSlotResolutionResultItem-intentName"></a>
The intents used in the slots list for the slot resolution details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** matchResult **   <a name="lexv2-Type-ConversationLevelSlotResolutionResultItem-matchResult"></a>
The number of matching slots used in the slots listings for the slot resolution evaluation.
Type: String
Valid Values: `Matched | Mismatched | ExecutionError`
Required: Yes

 ** slotName **   <a name="lexv2-Type-ConversationLevelSlotResolutionResultItem-slotName"></a>
The slot name in the slots list for the slot resolution details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_.-]?)+$`
Required: Yes

## See Also
<a name="API_ConversationLevelSlotResolutionResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ConversationLevelSlotResolutionResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ConversationLevelSlotResolutionResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ConversationLevelSlotResolutionResultItem)
