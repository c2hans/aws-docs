---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConversationLevelIntentClassificationResultItem.html
---

# ConversationLevelIntentClassificationResultItem
<a name="API_ConversationLevelIntentClassificationResultItem"></a>

The item listing the evaluation of intent level success or failure.

## Contents
<a name="API_ConversationLevelIntentClassificationResultItem_Contents"></a>

 ** intentName **   <a name="lexv2-Type-ConversationLevelIntentClassificationResultItem-intentName"></a>
The intent name used in the evaluation of intent level success or failure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** matchResult **   <a name="lexv2-Type-ConversationLevelIntentClassificationResultItem-matchResult"></a>
The number of times the specific intent is used in the evaluation of intent level success or failure.
Type: String
Valid Values: `Matched | Mismatched | ExecutionError`
Required: Yes

## See Also
<a name="API_ConversationLevelIntentClassificationResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ConversationLevelIntentClassificationResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ConversationLevelIntentClassificationResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ConversationLevelIntentClassificationResultItem)
