---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ElicitationCodeHookInvocationSetting.html
---

# ElicitationCodeHookInvocationSetting
<a name="API_ElicitationCodeHookInvocationSetting"></a>

Settings that specify the dialog code hook that is called by Amazon Lex between eliciting slot values.

## Contents
<a name="API_ElicitationCodeHookInvocationSetting_Contents"></a>

 ** enableCodeHookInvocation **   <a name="lexv2-Type-ElicitationCodeHookInvocationSetting-enableCodeHookInvocation"></a>
Indicates whether a Lambda function should be invoked for the dialog.
Type: Boolean
Required: Yes

 ** invocationLabel **   <a name="lexv2-Type-ElicitationCodeHookInvocationSetting-invocationLabel"></a>
A label that indicates the dialog step from which the dialog code hook is happening.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

## See Also
<a name="API_ElicitationCodeHookInvocationSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ElicitationCodeHookInvocationSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ElicitationCodeHookInvocationSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ElicitationCodeHookInvocationSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
