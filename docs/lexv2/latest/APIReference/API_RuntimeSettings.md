---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_RuntimeSettings.html
---

# RuntimeSettings
<a name="API_RuntimeSettings"></a>

Contains specifications about the Amazon Lex runtime generative AI capabilities from Amazon Bedrock that you can turn on for your bot.

## Contents
<a name="API_RuntimeSettings_Contents"></a>

 ** nluImprovement **   <a name="lexv2-Type-RuntimeSettings-nluImprovement"></a>
An object containing specifications for the Assisted NLU feature within the bot's runtime settings. These settings determine how the bot processes and interprets user utterances during conversations.
Type: [NluImprovementSpecification](API_NluImprovementSpecification.md) object
Required: No

 ** slotResolutionImprovement **   <a name="lexv2-Type-RuntimeSettings-slotResolutionImprovement"></a>
An object containing specifications for the assisted slot resolution feature.
Type: [SlotResolutionImprovementSpecification](API_SlotResolutionImprovementSpecification.md) object
Required: No

## See Also
<a name="API_RuntimeSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/RuntimeSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/RuntimeSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/RuntimeSettings)
