---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EntityAggregateFilter.html
---

# EntityAggregateFilter

A filter for narrowing down the entity aggregates returned by DescribeEntityAggregates.

## Contents
<a name="API_EntityAggregateFilter_Contents"></a>

 ** tags **   <a name="AWSHealth-Type-EntityAggregateFilter-tags"></a>
A map of tag keys to lists of tag values. A tag matches when its key is in the map and its value is one of the values listed for that key. Matching is case sensitive, and the filter matches when at least one key in the map matches.
Only entities whose tags match are included in the aggregates.
Type: String to array of strings map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 127.
Key Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{1,127}`
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{0,255}`
Required: No

## See Also
<a name="API_EntityAggregateFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EntityAggregateFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EntityAggregateFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EntityAggregateFilter)
