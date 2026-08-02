---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_NluImprovementSpecification.html
---

# NluImprovementSpecification
<a name="API_NluImprovementSpecification"></a>

Configures the Assisted Natural Language Understanding (NLU) feature for your bot. This specification determines whether enhanced intent recognition and utterance understanding capabilities are active.

## Contents
<a name="API_NluImprovementSpecification_Contents"></a>

 ** enabled **   <a name="lexv2-Type-NluImprovementSpecification-enabled"></a>
Determines whether the Assisted NLU feature is enabled for the bot. When set to `true`, Amazon Lex uses advanced models to improve intent recognition and slot resolution, with the default being `false`.
Type: Boolean
Required: Yes

 ** assistedNluMode **   <a name="lexv2-Type-NluImprovementSpecification-assistedNluMode"></a>
Specifies the mode for Assisted NLU operation. Use `Primary` to make Assisted NLU the primary intent recognition method, or `Fallback` to use it only when standard NLU confidence is low.
Type: String
Valid Values: `Primary | Fallback`
Required: No

 ** intentDisambiguationSettings **   <a name="lexv2-Type-NluImprovementSpecification-intentDisambiguationSettings"></a>
An object containing specifications for the Intent Disambiguation feature within the Assisted NLU settings. These settings determine how the bot handles ambiguous user inputs that could match multiple intents.
Type: [IntentDisambiguationSettings](API_IntentDisambiguationSettings.md) object
Required: No

## See Also
<a name="API_NluImprovementSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/NluImprovementSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/NluImprovementSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/NluImprovementSpecification)
