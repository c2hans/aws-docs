---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SearchFilterClause.html
---

# SearchFilterClause
<a name="API_SearchFilterClause"></a>

A filter clause that supports nested boolean logic. Exactly one of `andAllFilters`, `orAnyFilters`, `attributeFilter`, or `mapFilter` must be specified.

## Contents
<a name="API_SearchFilterClause_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AndAllFilters **   <a name="Glue-Type-SearchFilterClause-AndAllFilters"></a>
A list of filter clauses that must all match (logical AND).
Type: Array of [SearchFilterClause](#API_SearchFilterClause) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** AttributeFilter **   <a name="Glue-Type-SearchFilterClause-AttributeFilter"></a>
A filter on a single attribute value.
Type: [SearchAttributeFilter](API_SearchAttributeFilter.md) object
Required: No

 ** MapFilter **   <a name="Glue-Type-SearchFilterClause-MapFilter"></a>
A filter on a map attribute's key-value pair.
Type: [SearchMapFilter](API_SearchMapFilter.md) object
Required: No

 ** OrAnyFilters **   <a name="Glue-Type-SearchFilterClause-OrAnyFilters"></a>
A list of filter clauses where at least one must match (logical OR).
Type: Array of [SearchFilterClause](#API_SearchFilterClause) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_SearchFilterClause_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SearchFilterClause)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SearchFilterClause)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SearchFilterClause)
