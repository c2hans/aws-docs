---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DialogCodeHookInvocationSetting.html
---

# DialogCodeHookInvocationSetting
<a name="API_DialogCodeHookInvocationSetting"></a>

Settings that specify the dialog code hook that is called by Amazon Lex at a step of the conversation.

## Contents
<a name="API_DialogCodeHookInvocationSetting_Contents"></a>

 ** active **   <a name="lexv2-Type-DialogCodeHookInvocationSetting-active"></a>
Determines whether a dialog code hook is used when the intent is activated.
Type: Boolean
Required: Yes

 ** enableCodeHookInvocation **   <a name="lexv2-Type-DialogCodeHookInvocationSetting-enableCodeHookInvocation"></a>
Indicates whether a Lambda function should be invoked for the dialog.
Type: Boolean
Required: Yes

 ** postCodeHookSpecification **   <a name="lexv2-Type-DialogCodeHookInvocationSetting-postCodeHookSpecification"></a>
Contains the responses and actions that Amazon Lex takes after the Lambda function is complete.
Type: [PostDialogCodeHookInvocationSpecification](API_PostDialogCodeHookInvocationSpecification.md) object
Required: Yes

 ** invocationLabel **   <a name="lexv2-Type-DialogCodeHookInvocationSetting-invocationLabel"></a>
A label that indicates the dialog step from which the dialog code hook is happening.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

## See Also
<a name="API_DialogCodeHookInvocationSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DialogCodeHookInvocationSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DialogCodeHookInvocationSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DialogCodeHookInvocationSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
