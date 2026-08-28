---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PostDialogCodeHookInvocationSpecification.html
---

# PostDialogCodeHookInvocationSpecification
<a name="API_PostDialogCodeHookInvocationSpecification"></a>

Specifies next steps to run after the dialog code hook finishes.

## Contents
<a name="API_PostDialogCodeHookInvocationSpecification_Contents"></a>

 ** failureConditional **   <a name="lexv2-Type-PostDialogCodeHookInvocationSpecification-failureConditional"></a>
A list of conditional branches to evaluate after the dialog code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed`.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** failureNextStep **   <a name="lexv2-Type-PostDialogCodeHookInvocationSpecification-failureNextStep"></a>
Specifies the next step the bot runs after the dialog code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed`.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** failureResponse **   <a name="lexv2-Type-PostDialogCodeHookInvocationSpecification-failureResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

 ** successConditional **   <a name="lexv2-Type-PostDialogCodeHookInvocationSpecification-successConditional"></a>
A list of conditional branches to evaluate after the dialog code hook finishes successfully.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** successNextStep **   <a name="lexv2-Type-PostDialogCodeHookInvocationSpecification-successNextStep"></a>
Specifics the next step the bot runs after the dialog code hook finishes successfully.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** successResponse **   <a name="lexv2-Type-PostDialogCodeHookInvocationSpecification-successResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

 ** timeoutConditional **   <a name="lexv2-Type-PostDialogCodeHookInvocationSpecification-timeoutConditional"></a>
A list of conditional branches to evaluate if the code hook times out.
Type: [ConditionalSpecification](API_ConditionalSpecification.md) object
Required: No

 ** timeoutNextStep **   <a name="lexv2-Type-PostDialogCodeHookInvocationSpecification-timeoutNextStep"></a>
Specifies the next step that the bot runs when the code hook times out.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** timeoutResponse **   <a name="lexv2-Type-PostDialogCodeHookInvocationSpecification-timeoutResponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

## See Also
<a name="API_PostDialogCodeHookInvocationSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/PostDialogCodeHookInvocationSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/PostDialogCodeHookInvocationSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/PostDialogCodeHookInvocationSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
