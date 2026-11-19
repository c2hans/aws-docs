---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ChecklistItem.html
---

# ChecklistItem

Contains a checklist item and its discussion status.

## Contents
<a name="API_ChecklistItem_Contents"></a>

 ** itemKey **   <a name="connecthealth-Type-ChecklistItem-itemKey"></a>
The key that uniquely identifies the item within the checklist. For a managed note template, this value is a service-defined section key, such as `CHIEF_COMPLAINT`. For a custom note template, this value is the `sectionHeader` of the section that you defined.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** status **   <a name="connecthealth-Type-ChecklistItem-status"></a>
The discussion status of the checklist item. The following values are valid:
+  `DISCUSSED`: The conversation has covered the item.
+  `PARTIALLY_DISCUSSED`: The conversation has covered part of the item.
+  `NOT_DISCUSSED`: The conversation has not covered the item.
The status usually progresses toward `DISCUSSED`, but it can return to `NOT_DISCUSSED` if a speaker retracts a statement.
Type: String
Valid Values: `DISCUSSED | PARTIALLY_DISCUSSED | NOT_DISCUSSED`
Required: Yes

## See Also
<a name="API_ChecklistItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/ChecklistItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/ChecklistItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/ChecklistItem)
