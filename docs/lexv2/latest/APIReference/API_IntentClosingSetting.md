---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_IntentClosingSetting.html
---

# IntentClosingSetting
<a name="API_IntentClosingSetting"></a>

Provides a statement the Amazon Lex conveys to the user when the intent is successfully fulfilled.

## Contents
<a name="API_IntentClosingSetting_Contents"></a>

 ** active **   <a name="lexv2-Type-IntentClosingSetting-active"></a>
Specifies whether an intent's closing response is used. When this field is false, the closing response isn't sent to the user. If the `active` field isn't specified, the default is true.
Type: Boolean
Required: No

 ** closingResponse **   <a name="lexv2-Type-IntentClosingSetting-closingResponse"></a>
The response that Amazon Lex sends to the user when the intent is complete.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

 ** conditional **   <a name="lexv2-Type-IntentClosingSetting-conditional"></a>
A list of conditional branches associated with the intent's closing response. These branches are executed when the `nextStep` attribute is set to `EvalutateConditional`.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** nextStep **   <a name="lexv2-Type-IntentClosingSetting-nextStep"></a>
Specifies the next step that the bot executes after playing the intent's closing response.
Type: [DialogState](API_DialogState.md) object
Required: No

## See Also
<a name="API_IntentClosingSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/IntentClosingSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/IntentClosingSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/IntentClosingSetting)
