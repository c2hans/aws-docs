---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_Checklist.html
---

# Checklist
<a name="API_Checklist"></a>

Contains the sections of a note template checklist and the discussion status of each section.

## Contents
<a name="API_Checklist_Contents"></a>

 ** checklistId **   <a name="connecthealth-Type-Checklist-checklistId"></a>
The identifier of the checklist. For a managed note template, this value is the template type, such as `HISTORY_AND_PHYSICAL`. For a custom note template, this value is `CUSTOM_` followed by the template base, such as `CUSTOM_GIRPP`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** items **   <a name="connecthealth-Type-Checklist-items"></a>
The checklist items in template order. The list contains one item for each checklist section, including sections that have not been discussed.
Type: Array of [ChecklistItem](API_ChecklistItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

## See Also
<a name="API_Checklist_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/Checklist)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/Checklist)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/Checklist)
