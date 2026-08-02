---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotTypeSummary.html
---

# SlotTypeSummary
<a name="API_SlotTypeSummary"></a>

Provides summary information about a slot type.

## Contents
<a name="API_SlotTypeSummary_Contents"></a>

 ** description **   <a name="lexv2-Type-SlotTypeSummary-description"></a>
The description of the slot type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** lastUpdatedDateTime **   <a name="lexv2-Type-SlotTypeSummary-lastUpdatedDateTime"></a>
A timestamp of the date and time that the slot type was last updated.
Type: Timestamp
Required: No

 ** parentSlotTypeSignature **   <a name="lexv2-Type-SlotTypeSummary-parentSlotTypeSignature"></a>
If the slot type is derived from a built-on slot type, the name of the parent slot type.
Type: String
Required: No

 ** slotTypeCategory **   <a name="lexv2-Type-SlotTypeSummary-slotTypeCategory"></a>
Indicates the type of the slot type.
+  `Custom` - A slot type that you created using custom values. For more information, see [Creating custom slot types](https://docs.aws.amazon.com/lexv2/latest/dg/custom-slot-types.html).
+  `Extended` - A slot type created by extending the `AMAZON.AlphaNumeric` built-in slot type. For more information, see [https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-alphanumerice.html](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-alphanumerice.html).
+  `ExternalGrammar` - A slot type using a custom GRXML grammar to define values. For more information, see [Using a custom grammar slot type](https://docs.aws.amazon.com/lexv2/latest/dg/building-grxml.html).
Type: String
Valid Values: `Custom | Extended | ExternalGrammar | Composite`
Required: No

 ** slotTypeId **   <a name="lexv2-Type-SlotTypeSummary-slotTypeId"></a>
The unique identifier assigned to the slot type.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** slotTypeName **   <a name="lexv2-Type-SlotTypeSummary-slotTypeName"></a>
The name of the slot type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

## See Also
<a name="API_SlotTypeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SlotTypeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SlotTypeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SlotTypeSummary)
