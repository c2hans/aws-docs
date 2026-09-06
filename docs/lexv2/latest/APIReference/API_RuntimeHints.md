---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_RuntimeHints.html
---

# RuntimeHints
<a name="API_RuntimeHints"></a>

You can provide Amazon Lex with hints to the phrases that a customer is likely to use for a slot. When a slot with hints is resolved, the phrases in the runtime hints are preferred in the resolution. You can provide hints for a maximum of 100 intents. You can provide a maximum of 100 slots.

Before you can use runtime hints with an existing bot, you must first rebuild the bot.

For more information, see [Using runtime hints to improve recognition of slot values](https://docs.aws.amazon.com/lexv2/latest/dg/using-hints.html).

## Contents
<a name="API_RuntimeHints_Contents"></a>

 ** slotHints **   <a name="lexv2-Type-RuntimeHints-slotHints"></a>
A list of the slots in the intent that should have runtime hints added, and the phrases that should be added for each slot.
The first level of the `slotHints` map is the name of the intent. The second level is the name of the slot within the intent. For more information, see [Using hints to improve accuracy](https://docs.aws.amazon.com/lexv2/latest/dg/using-hints.html).
The intent name and slot name must exist.
Type: String to string to [RuntimeHintDetails](API_RuntimeHintDetails.md) object map map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

## See Also
<a name="API_RuntimeHints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/RuntimeHints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/RuntimeHints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/RuntimeHints)
