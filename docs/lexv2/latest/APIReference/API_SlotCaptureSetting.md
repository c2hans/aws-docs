---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotCaptureSetting.html
---

# SlotCaptureSetting
<a name="API_SlotCaptureSetting"></a>

Settings used when Amazon Lex successfully captures a slot value from a user.

## Contents
<a name="API_SlotCaptureSetting_Contents"></a>

 ** captureConditional **   <a name="lexv2-Type-SlotCaptureSetting-captureConditional"></a>
A list of conditional branches to evaluate after the slot value is captured.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** captureNextStep **   <a name="lexv2-Type-SlotCaptureSetting-captureNextStep"></a>
Specifies the next step that the bot runs when the slot value is captured before the code hook times out.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** captureResponse **   <a name="lexv2-Type-SlotCaptureSetting-captureResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

 ** codeHook **   <a name="lexv2-Type-SlotCaptureSetting-codeHook"></a>
Code hook called after Amazon Lex successfully captures a slot value.
Type: [DialogCodeHookInvocationSetting](API_DialogCodeHookInvocationSetting.md) object
Required: No

 ** elicitationCodeHook **   <a name="lexv2-Type-SlotCaptureSetting-elicitationCodeHook"></a>
Code hook called when Amazon Lex doesn't capture a slot value.
Type: [ElicitationCodeHookInvocationSetting](API_ElicitationCodeHookInvocationSetting.md) object
Required: No

 ** failureConditional **   <a name="lexv2-Type-SlotCaptureSetting-failureConditional"></a>
A list of conditional branches to evaluate when the slot value isn't captured.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** failureNextStep **   <a name="lexv2-Type-SlotCaptureSetting-failureNextStep"></a>
Specifies the next step that the bot runs when the slot value code is not recognized.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** failureResponse **   <a name="lexv2-Type-SlotCaptureSetting-failureResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

## See Also
<a name="API_SlotCaptureSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SlotCaptureSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SlotCaptureSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SlotCaptureSetting)
