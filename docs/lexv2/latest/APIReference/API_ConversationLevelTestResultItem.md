---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConversationLevelTestResultItem.html
---

# ConversationLevelTestResultItem
<a name="API_ConversationLevelTestResultItem"></a>

The test result evaluation item at the conversation level.

## Contents
<a name="API_ConversationLevelTestResultItem_Contents"></a>

 ** conversationId **   <a name="lexv2-Type-ConversationLevelTestResultItem-conversationId"></a>
The conversation Id of the test result evaluation item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^([0-9a-zA-Z][_-]?)+$`
Required: Yes

 ** endToEndResult **   <a name="lexv2-Type-ConversationLevelTestResultItem-endToEndResult"></a>
The end-to-end success or failure of the test result evaluation item.
Type: String
Valid Values: `Matched | Mismatched | ExecutionError`
Required: Yes

 ** intentClassificationResults **   <a name="lexv2-Type-ConversationLevelTestResultItem-intentClassificationResults"></a>
The intent classification of the test result evaluation item.
Type: Array of [ConversationLevelIntentClassificationResultItem](API_ConversationLevelIntentClassificationResultItem.md) objects
Required: Yes

 ** slotResolutionResults **   <a name="lexv2-Type-ConversationLevelTestResultItem-slotResolutionResults"></a>
The slot success or failure of the test result evaluation item.
Type: Array of [ConversationLevelSlotResolutionResultItem](API_ConversationLevelSlotResolutionResultItem.md) objects
Required: Yes

 ** speechTranscriptionResult **   <a name="lexv2-Type-ConversationLevelTestResultItem-speechTranscriptionResult"></a>
The speech transcription success or failure of the test result evaluation item.
Type: String
Valid Values: `Matched | Mismatched | ExecutionError`
Required: No

## See Also
<a name="API_ConversationLevelTestResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ConversationLevelTestResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ConversationLevelTestResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ConversationLevelTestResultItem)
