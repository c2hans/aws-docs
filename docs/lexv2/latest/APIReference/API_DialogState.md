---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DialogState.html
---

# DialogState
<a name="API_DialogState"></a>

The current state of the conversation with the user.

## Contents
<a name="API_DialogState_Contents"></a>

 ** dialogAction **   <a name="lexv2-Type-DialogState-dialogAction"></a>
Defines the action that the bot executes at runtime when the conversation reaches this step.
Type: [DialogAction](API_DialogAction.md) object
Required: No

 ** intent **   <a name="lexv2-Type-DialogState-intent"></a>
Override settings to configure the intent state.
Type: [IntentOverride](API_IntentOverride.md) object
Required: No

 ** sessionAttributes **   <a name="lexv2-Type-DialogState-sessionAttributes"></a>
Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_DialogState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DialogState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DialogState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DialogState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
