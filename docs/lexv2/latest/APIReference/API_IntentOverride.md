---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_IntentOverride.html
---

# IntentOverride
<a name="API_IntentOverride"></a>

Override settings to configure the intent state.

## Contents
<a name="API_IntentOverride_Contents"></a>

 ** name **   <a name="lexv2-Type-IntentOverride-name"></a>
The name of the intent. Only required when you're switching intents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

 ** slots **   <a name="lexv2-Type-IntentOverride-slots"></a>
A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map aren't overridden.
Type: String to [SlotValueOverride](API_SlotValueOverride.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

## See Also
<a name="API_IntentOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/IntentOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/IntentOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/IntentOverride)
