---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_Value.html
---

# Value
<a name="API_runtime_Value"></a>

Information about the value provided for a slot and Amazon Lex's interpretation.

## Contents
<a name="API_runtime_Value_Contents"></a>

 ** interpretedValue **   <a name="lexv2-Type-runtime_Value-interpretedValue"></a>
The value that Amazon Lex determines for the slot, given the user input. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** originalValue **   <a name="lexv2-Type-runtime_Value-originalValue"></a>
The part of the user's response to the slot elicitation that Amazon Lex determines is relevant to the slot value.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** resolvedValues **   <a name="lexv2-Type-runtime_Value-resolvedValues"></a>
A list of values that Amazon Lex determines are possible resolutions for the user input. The first value matches the `interpretedValue`.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_runtime_Value_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.lex.v2-2020-08-07/Value)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.lex.v2-2020-08-07/Value)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.lex.v2-2020-08-07/Value)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
