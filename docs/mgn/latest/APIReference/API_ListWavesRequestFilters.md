---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListWavesRequestFilters.html
---

# ListWavesRequestFilters
<a name="API_ListWavesRequestFilters"></a>

Waves list filters.

## Contents
<a name="API_ListWavesRequestFilters_Contents"></a>

 ** isArchived **   <a name="mgn-Type-ListWavesRequestFilters-isArchived"></a>
Filter waves list by archival status.
Type: Boolean
Required: No

 ** waveIDs **   <a name="mgn-Type-ListWavesRequestFilters-waveIDs"></a>
Filter waves list by wave ID.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 22.
Pattern: `wave-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_ListWavesRequestFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListWavesRequestFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListWavesRequestFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListWavesRequestFilters)
