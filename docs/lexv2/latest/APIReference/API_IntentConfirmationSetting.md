---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_IntentConfirmationSetting.html
---

# IntentConfirmationSetting
<a name="API_IntentConfirmationSetting"></a>

Provides a prompt for making sure that the user is ready for the intent to be fulfilled.

## Contents
<a name="API_IntentConfirmationSetting_Contents"></a>

 ** promptSpecification **   <a name="lexv2-Type-IntentConfirmationSetting-promptSpecification"></a>
Prompts the user to confirm the intent. This question should have a yes or no answer.
Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the `OrderPizza` intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information.
Type: [PromptSpecification](API_PromptSpecification.md) object
Required: Yes

 ** active **   <a name="lexv2-Type-IntentConfirmationSetting-active"></a>
Specifies whether the intent's confirmation is sent to the user. When this field is false, confirmation and declination responses aren't sent. If the `active` field isn't specified, the default is true.
Type: Boolean
Required: No

 ** codeHook **   <a name="lexv2-Type-IntentConfirmationSetting-codeHook"></a>
The `DialogCodeHookInvocationSetting` object associated with intent's confirmation step. The dialog code hook is triggered based on these invocation settings when the confirmation next step or declination next step or failure next step is `InvokeDialogCodeHook`.
Type: [DialogCodeHookInvocationSetting](API_DialogCodeHookInvocationSetting.md) object
Required: No

 ** confirmationConditional **   <a name="lexv2-Type-IntentConfirmationSetting-confirmationConditional"></a>
A list of conditional branches to evaluate after the intent is closed.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** confirmationNextStep **   <a name="lexv2-Type-IntentConfirmationSetting-confirmationNextStep"></a>
Specifies the next step that the bot executes when the customer confirms the intent.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** confirmationResponse **   <a name="lexv2-Type-IntentConfirmationSetting-confirmationResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

 ** declinationConditional **   <a name="lexv2-Type-IntentConfirmationSetting-declinationConditional"></a>
A list of conditional branches to evaluate after the intent is declined.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** declinationNextStep **   <a name="lexv2-Type-IntentConfirmationSetting-declinationNextStep"></a>
Specifies the next step that the bot executes when the customer declines the intent.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** declinationResponse **   <a name="lexv2-Type-IntentConfirmationSetting-declinationResponse"></a>
When the user answers "no" to the question defined in `promptSpecification`, Amazon Lex responds with this response to acknowledge that the intent was canceled.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

 ** elicitationCodeHook **   <a name="lexv2-Type-IntentConfirmationSetting-elicitationCodeHook"></a>
The `DialogCodeHookInvocationSetting` used when the code hook is invoked during confirmation prompt retries.
Type: [ElicitationCodeHookInvocationSetting](API_ElicitationCodeHookInvocationSetting.md) object
Required: No

 ** failureConditional **   <a name="lexv2-Type-IntentConfirmationSetting-failureConditional"></a>
Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** failureNextStep **   <a name="lexv2-Type-IntentConfirmationSetting-failureNextStep"></a>
The next step to take in the conversation if the confirmation step fails.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** failureResponse **   <a name="lexv2-Type-IntentConfirmationSetting-failureResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

## See Also
<a name="API_IntentConfirmationSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/IntentConfirmationSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/IntentConfirmationSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/IntentConfirmationSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
