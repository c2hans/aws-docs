---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchGroupedFilterExpressions.html
---

# SearchGroupedFilterExpressions
<a name="API_SearchGroupedFilterExpressions"></a>

The search terms for a resource.

## Contents
<a name="API_SearchGroupedFilterExpressions_Contents"></a>

 ** filters **   <a name="deadlinecloud-Type-SearchGroupedFilterExpressions-filters"></a>
The filters to use for the search.
Type: Array of [SearchFilterExpression](API_SearchFilterExpression.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: Yes

 ** operator **   <a name="deadlinecloud-Type-SearchGroupedFilterExpressions-operator"></a>
The operators to include in the search.
Type: String
Valid Values: `AND | OR`
Required: Yes

## See Also
<a name="API_SearchGroupedFilterExpressions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchGroupedFilterExpressions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchGroupedFilterExpressions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchGroupedFilterExpressions)
