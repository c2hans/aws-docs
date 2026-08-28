---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotValueOverride.html
---

# SlotValueOverride
<a name="API_SlotValueOverride"></a>

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

## Contents
<a name="API_SlotValueOverride_Contents"></a>

 ** shape **   <a name="lexv2-Type-SlotValueOverride-shape"></a>
When the shape value is `List`, it indicates that the `values` field contains a list of slot values. When the value is `Scalar`, it indicates that the `value` field contains a single value.
Type: String
Valid Values: `Scalar | List`
Required: No

 ** value **   <a name="lexv2-Type-SlotValueOverride-value"></a>
The current value of the slot.
Type: [SlotValue](API_SlotValue.md) object
Required: No

 ** values **   <a name="lexv2-Type-SlotValueOverride-values"></a>
A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be "pepperoni" and "pineapple."
Type: Array of [SlotValueOverride](#API_SlotValueOverride) objects
Required: No

## See Also
<a name="API_SlotValueOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SlotValueOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SlotValueOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SlotValueOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
