---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotValueSelectionSetting.html
---

# SlotValueSelectionSetting
<a name="API_SlotValueSelectionSetting"></a>

Contains settings used by Amazon Lex to select a slot value.

## Contents
<a name="API_SlotValueSelectionSetting_Contents"></a>

 ** resolutionStrategy **   <a name="lexv2-Type-SlotValueSelectionSetting-resolutionStrategy"></a>
Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:
+  `ORIGINAL_VALUE` - Returns the value entered by the user, if the user value is similar to the slot value.
+  `TOP_RESOLUTION` - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.
If you don't specify the `valueSelectionStrategy`, the default is `ORIGINAL_VALUE`.
Type: String
Valid Values: `OriginalValue | TopResolution | Concatenation`
Required: Yes

 ** advancedRecognitionSetting **   <a name="lexv2-Type-SlotValueSelectionSetting-advancedRecognitionSetting"></a>
Provides settings that enable advanced recognition settings for slot values. You can use this to enable using slot values as a custom vocabulary for recognizing user utterances.
Type: [AdvancedRecognitionSetting](API_AdvancedRecognitionSetting.md) object
Required: No

 ** regexFilter **   <a name="lexv2-Type-SlotValueSelectionSetting-regexFilter"></a>
A regular expression used to validate the value of a slot.
Type: [SlotValueRegexFilter](API_SlotValueRegexFilter.md) object
Required: No

## See Also
<a name="API_SlotValueSelectionSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SlotValueSelectionSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SlotValueSelectionSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SlotValueSelectionSetting)
