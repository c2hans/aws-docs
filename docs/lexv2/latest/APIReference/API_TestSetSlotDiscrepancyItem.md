---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestSetSlotDiscrepancyItem.html
---

# TestSetSlotDiscrepancyItem
<a name="API_TestSetSlotDiscrepancyItem"></a>

Contains information about discrepancy in a slot information between the test set and the bot.

## Contents
<a name="API_TestSetSlotDiscrepancyItem_Contents"></a>

 ** errorMessage **   <a name="lexv2-Type-TestSetSlotDiscrepancyItem-errorMessage"></a>
The error message for a discrepancy for an intent between the test set and the bot.
Type: String
Required: Yes

 ** intentName **   <a name="lexv2-Type-TestSetSlotDiscrepancyItem-intentName"></a>
The name of the intent associated with the slot in the discrepancy report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** slotName **   <a name="lexv2-Type-TestSetSlotDiscrepancyItem-slotName"></a>
The name of the slot in the discrepancy report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

## See Also
<a name="API_TestSetSlotDiscrepancyItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestSetSlotDiscrepancyItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestSetSlotDiscrepancyItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestSetSlotDiscrepancyItem)
