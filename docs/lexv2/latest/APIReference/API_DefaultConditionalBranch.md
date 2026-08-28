---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DefaultConditionalBranch.html
---

# DefaultConditionalBranch
<a name="API_DefaultConditionalBranch"></a>

A set of actions that Amazon Lex should run if none of the other conditions are met.

## Contents
<a name="API_DefaultConditionalBranch_Contents"></a>

 ** nextStep **   <a name="lexv2-Type-DefaultConditionalBranch-nextStep"></a>
The next step in the conversation.
Type: [DialogState](API_DialogState.md) object
Required: No

 ** response **   <a name="lexv2-Type-DefaultConditionalBranch-response"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
Type: [ResponseSpecification](API_ResponseSpecification.md) object
Required: No

## See Also
<a name="API_DefaultConditionalBranch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DefaultConditionalBranch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DefaultConditionalBranch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DefaultConditionalBranch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
