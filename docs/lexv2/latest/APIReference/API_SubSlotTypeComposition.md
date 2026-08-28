---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SubSlotTypeComposition.html
---

# SubSlotTypeComposition
<a name="API_SubSlotTypeComposition"></a>

Subslot type composition.

## Contents
<a name="API_SubSlotTypeComposition_Contents"></a>

 ** name **   <a name="lexv2-Type-SubSlotTypeComposition-name"></a>
Name of a constituent sub slot inside a composite slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** slotTypeId **   <a name="lexv2-Type-SubSlotTypeComposition-slotTypeId"></a>
The unique identifier assigned to a slot type. This refers to either a built-in slot type or the unique slotTypeId of a custom slot type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^((AMAZON\.)[a-zA-Z_]+?|[0-9a-zA-Z]+)$`
Required: Yes

## See Also
<a name="API_SubSlotTypeComposition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SubSlotTypeComposition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SubSlotTypeComposition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SubSlotTypeComposition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
