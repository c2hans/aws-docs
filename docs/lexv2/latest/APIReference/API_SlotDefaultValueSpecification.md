---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotDefaultValueSpecification.html
---

# SlotDefaultValueSpecification
<a name="API_SlotDefaultValueSpecification"></a>

Defines a list of values that Amazon Lex should use as the default value for a slot.

## Contents
<a name="API_SlotDefaultValueSpecification_Contents"></a>

 ** defaultValueList **   <a name="lexv2-Type-SlotDefaultValueSpecification-defaultValueList"></a>
A list of default values. Amazon Lex chooses the default value to use in the order that they are presented in the list.
Type: Array of [SlotDefaultValue](API_SlotDefaultValue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_SlotDefaultValueSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SlotDefaultValueSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SlotDefaultValueSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SlotDefaultValueSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
