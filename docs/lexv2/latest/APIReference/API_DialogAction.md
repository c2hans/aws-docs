---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DialogAction.html
---

# DialogAction
<a name="API_DialogAction"></a>

Defines the action that the bot executes at runtime when the conversation reaches this step.

## Contents
<a name="API_DialogAction_Contents"></a>

 ** type **   <a name="lexv2-Type-DialogAction-type"></a>
The action that the bot should execute.
Type: String
Valid Values: `ElicitIntent | StartIntent | ElicitSlot | EvaluateConditional | InvokeDialogCodeHook | ConfirmIntent | FulfillIntent | CloseIntent | EndConversation`
Required: Yes

 ** slotToElicit **   <a name="lexv2-Type-DialogAction-slotToElicit"></a>
If the dialog action is `ElicitSlot`, defines the slot to elicit from the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

 ** suppressNextMessage **   <a name="lexv2-Type-DialogAction-suppressNextMessage"></a>
When true the next message for the intent is not used.
Type: Boolean
Required: No

## See Also
<a name="API_DialogAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DialogAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DialogAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DialogAction)
