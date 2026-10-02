---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PreferenceEntry.html
---

# PreferenceEntry
<a name="API_PreferenceEntry"></a>

A single Well-Architected Agent preference and its current state.

## Contents
<a name="API_PreferenceEntry_Contents"></a>

 ** key **   <a name="wellarchitected-Type-PreferenceEntry-key"></a>
Which preference this entry describes.
Type: String
Valid Values: `ORG_INTEGRATION | COST_EXPLORER_ENABLED | COST_EXPLORER_DAILY_RESOURCE_LEVEL_DATA`
Required: Yes

 ** status **   <a name="wellarchitected-Type-PreferenceEntry-status"></a>
Current state of the preference. ENABLED and DISABLED reflect the result of the most recent successful change. FAILED reflects a stored failure surfaced on a read and is accompanied by a detail message.
Type: String
Valid Values: `ENABLED | DISABLED | FAILED`
Required: Yes

 ** detail **   <a name="wellarchitected-Type-PreferenceEntry-detail"></a>
A human-readable explanation present only when status is FAILED, describing what went wrong and how to recover.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_PreferenceEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/PreferenceEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/PreferenceEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/PreferenceEntry)
