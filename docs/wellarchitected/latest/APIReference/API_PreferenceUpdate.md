---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PreferenceUpdate.html
---

# PreferenceUpdate
<a name="API_PreferenceUpdate"></a>

A caller's requested change to one preference, supplied to PutAgentPreferences.

## Contents
<a name="API_PreferenceUpdate_Contents"></a>

 ** key **   <a name="wellarchitected-Type-PreferenceUpdate-key"></a>
Which preference to update.
Type: String
Valid Values: `ORG_INTEGRATION | COST_EXPLORER_ENABLED | COST_EXPLORER_DAILY_RESOURCE_LEVEL_DATA`
Required: Yes

 ** state **   <a name="wellarchitected-Type-PreferenceUpdate-state"></a>
State to set the preference to. FAILED is an observed state only and cannot be requested.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_PreferenceUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/PreferenceUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/PreferenceUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/PreferenceUpdate)
