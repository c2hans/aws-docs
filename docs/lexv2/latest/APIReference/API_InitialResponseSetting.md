---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_InitialResponseSetting.html
---

# InitialResponseSetting
<a name="API_InitialResponseSetting"></a>

Configuration setting for a response sent to the user before Amazon Lex starts eliciting slots.

## Contents
<a name="API_InitialResponseSetting_Contents"></a>

 ** codeHook **   <a name="lexv2-Type-InitialResponseSetting-codeHook"></a>
Settings that specify the dialog code hook that is called by Amazon Lex at a step of the conversation.
Type: [DialogCodeHookInvocationSetting](API_DialogCodeHookInvocationSetting.md) object
Required: No

 ** conditional **   <a name="lexv2-Type-InitialResponseSetting-conditional"></a>
Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** initialResponse **   <a name="lexv2-Type-InitialResponseSetting-initialResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

 ** nextStep **   <a name="lexv2-Type-InitialResponseSetting-nextStep"></a>
The next step in the conversation.
Type: [DialogState](API_DialogState.md) object
Required: No

## See Also
<a name="API_InitialResponseSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/InitialResponseSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/InitialResponseSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/InitialResponseSetting)
