---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_KeyFilter.html
---

# KeyFilter
<a name="API_KeyFilter"></a>

Key-value filter used for tags and attributes filtering. Multiple KeyFilters are AND'ed. Multiple values within a single KeyFilter are OR'ed. Values support pattern syntax: exact, negation (\!value), wildcard (\*value\*, value\*, \*value).

## Contents
<a name="API_KeyFilter_Contents"></a>

 ** key **   <a name="cloudwatchomni-Type-KeyFilter-key"></a>
The tag or attribute key to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** values **   <a name="cloudwatchomni-Type-KeyFilter-values"></a>
The values to match for this key, OR'ed together. Each supports exact, negation (\!value), and wildcard (\*value\*, value\*, \*value) syntax.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 259.
Required: No

## See Also
<a name="API_KeyFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/KeyFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/KeyFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/KeyFilter)
