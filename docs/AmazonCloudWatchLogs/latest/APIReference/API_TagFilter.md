---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagFilter.html
---

# TagFilter
<a name="API_TagFilter"></a>

A tag filter that specifies a tag key and optional tag values for filtering log groups by tags.

## Contents
<a name="API_TagFilter_Contents"></a>

 ** key **   <a name="CWL-Type-TagFilter-key"></a>
The tag key to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Required: Yes

 ** values **   <a name="CWL-Type-TagFilter-values"></a>
An optional list of tag values to filter on.
+ If you specify a filter that contains more than one value for a key, the response returns log groups that match any of the specified values for that key.
+ If you don't specify values, the response returns all log groups that are tagged with that key, with any or no value.
+ Use `*` for wildcard matching. For example, `prod*` matches values that start with `prod`.
+ Use `!` as a prefix for negation. For example, `!prod` matches values that are not `prod`.
+ Exact matching and negation are case-sensitive. Wildcard matching is case-insensitive.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 259.
Pattern: `^!?\*?([\p{L}\p{Z}\p{N}_.:/=+\-@]*)\*?$`
Required: No

## See Also
<a name="API_TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/TagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/TagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/TagFilter)
