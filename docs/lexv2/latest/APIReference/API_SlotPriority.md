---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotPriority.html
---

# SlotPriority
<a name="API_SlotPriority"></a>

Sets the priority that Amazon Lex should use when eliciting slot values from a user.

## Contents
<a name="API_SlotPriority_Contents"></a>

 ** priority **   <a name="lexv2-Type-SlotPriority-priority"></a>
The priority that Amazon Lex should apply to the slot.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** slotId **   <a name="lexv2-Type-SlotPriority-slotId"></a>
The unique identifier of the slot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## See Also
<a name="API_SlotPriority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SlotPriority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SlotPriority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SlotPriority)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
