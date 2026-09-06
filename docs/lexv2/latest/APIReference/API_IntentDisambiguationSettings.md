---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_IntentDisambiguationSettings.html
---

# IntentDisambiguationSettings
<a name="API_IntentDisambiguationSettings"></a>

Configures the Intent Disambiguation feature that helps resolve ambiguous user inputs when multiple intents could match. When enabled, the system presents clarifying questions to users, helping them specify their exact intent for improved conversation accuracy.

## Contents
<a name="API_IntentDisambiguationSettings_Contents"></a>

 ** enabled **   <a name="lexv2-Type-IntentDisambiguationSettings-enabled"></a>
Determines whether the Intent Disambiguation feature is enabled. When set to `true`, Amazon Lex will present disambiguation options to users when multiple intents could match their input, with the default being `false`.
Type: Boolean
Required: Yes

 ** customDisambiguationMessage **   <a name="lexv2-Type-IntentDisambiguationSettings-customDisambiguationMessage"></a>
Provides a custom message that will be displayed before presenting the disambiguation options to users. This message helps set the context for users and can be customized to match your bot's tone and brand. If not specified, a default message will be used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** maxDisambiguationIntents **   <a name="lexv2-Type-IntentDisambiguationSettings-maxDisambiguationIntents"></a>
Specifies the maximum number of intent options (2-5) to present to users when disambiguation is needed. This setting determines how many intent options will be shown to users when the system detects ambiguous input. The default value is 3.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 5.
Required: No

## See Also
<a name="API_IntentDisambiguationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/IntentDisambiguationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/IntentDisambiguationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/IntentDisambiguationSettings)
