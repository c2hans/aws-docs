---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_RuntimeHintDetails.html
---

# RuntimeHintDetails
<a name="API_RuntimeHintDetails"></a>

Provides an array of phrases that should be given preference when resolving values for a slot.

## Contents
<a name="API_RuntimeHintDetails_Contents"></a>

 ** runtimeHintValues **   <a name="lexv2-Type-RuntimeHintDetails-runtimeHintValues"></a>
One or more strings that Amazon Lex should look for in the input to the bot. Each phrase is given preference when deciding on slot values.
Type: Array of [RuntimeHintValue](API_RuntimeHintValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** subSlotHints **   <a name="lexv2-Type-RuntimeHintDetails-subSlotHints"></a>
A map of constituent sub slot names inside a composite slot in the intent and the phrases that should be added for each sub slot. Inside each composite slot hints, this structure provides a mechanism to add granular sub slot phrases. Only sub slot hints are supported for composite slots. The intent name, composite slot name and the constituent sub slot names must exist.
Type: String to [RuntimeHintDetails](#API_RuntimeHintDetails) object map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

## See Also
<a name="API_RuntimeHintDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/RuntimeHintDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/RuntimeHintDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/RuntimeHintDetails)
