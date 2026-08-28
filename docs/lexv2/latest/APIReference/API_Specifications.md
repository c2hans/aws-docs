---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_Specifications.html
---

# Specifications
<a name="API_Specifications"></a>

Subslot specifications.

## Contents
<a name="API_Specifications_Contents"></a>

 ** slotTypeId **   <a name="lexv2-Type-Specifications-slotTypeId"></a>
The unique identifier assigned to the slot type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^((AMAZON\.)[a-zA-Z_]+?|[0-9a-zA-Z]+)$`
Required: Yes

 ** valueElicitationSetting **   <a name="lexv2-Type-Specifications-valueElicitationSetting"></a>
Specifies the elicitation setting details for constituent sub slots of a composite slot.
Type: [SubSlotValueElicitationSetting](API_SubSlotValueElicitationSetting.md) object
Required: Yes

## See Also
<a name="API_Specifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/Specifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/Specifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/Specifications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
