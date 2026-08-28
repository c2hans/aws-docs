---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SubSlotSetting.html
---

# SubSlotSetting
<a name="API_SubSlotSetting"></a>

Specifications for the constituent sub slots and the expression for the composite slot.

## Contents
<a name="API_SubSlotSetting_Contents"></a>

 ** expression **   <a name="lexv2-Type-SubSlotSetting-expression"></a>
The expression text for defining the constituent sub slots in the composite slot using logical AND and OR operators.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 640.
Pattern: `[0-9A-Za-z_\-\s\(\)]+`
Required: No

 ** slotSpecifications **   <a name="lexv2-Type-SubSlotSetting-slotSpecifications"></a>
Specifications for the constituent sub slots of a composite slot.
Type: String to [Specifications](API_Specifications.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 6 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

## See Also
<a name="API_SubSlotSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SubSlotSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SubSlotSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SubSlotSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
