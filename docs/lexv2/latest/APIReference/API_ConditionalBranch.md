---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConditionalBranch.html
---

# ConditionalBranch
<a name="API_ConditionalBranch"></a>

A set of actions that Amazon Lex should run if the condition is matched.

## Contents
<a name="API_ConditionalBranch_Contents"></a>

 ** condition **   <a name="lexv2-Type-ConditionalBranch-condition"></a>
Contains the expression to evaluate. If the condition is true, the branch's actions are taken.
Type: [Condition](API_Condition.md) object
Required: Yes

 ** name **   <a name="lexv2-Type-ConditionalBranch-name"></a>
The name of the branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** nextStep **   <a name="lexv2-Type-ConditionalBranch-nextStep"></a>
The next step in the conversation.
Type: [DialogState](API_DialogState.md) object
Required: Yes

 ** response **   <a name="lexv2-Type-ConditionalBranch-response"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

## See Also
<a name="API_ConditionalBranch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ConditionalBranch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ConditionalBranch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ConditionalBranch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
