---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchFilterExpression.html
---

# SearchFilterExpression
<a name="API_SearchFilterExpression"></a>

The type of search filter to apply.

## Contents
<a name="API_SearchFilterExpression_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dateTimeFilter **   <a name="deadlinecloud-Type-SearchFilterExpression-dateTimeFilter"></a>
Filters based on date and time.
Type: [DateTimeFilterExpression](API_DateTimeFilterExpression.md) object
Required: No

 ** groupFilter **   <a name="deadlinecloud-Type-SearchFilterExpression-groupFilter"></a>
Filters by group.
Type: [SearchGroupedFilterExpressions](API_SearchGroupedFilterExpressions.md) object
Required: No

 ** parameterFilter **   <a name="deadlinecloud-Type-SearchFilterExpression-parameterFilter"></a>
Filters by parameter.
Type: [ParameterFilterExpression](API_ParameterFilterExpression.md) object
Required: No

 ** searchTermFilter **   <a name="deadlinecloud-Type-SearchFilterExpression-searchTermFilter"></a>
Filters by a specified search term.
Type: [SearchTermFilterExpression](API_SearchTermFilterExpression.md) object
Required: No

 ** stringFilter **   <a name="deadlinecloud-Type-SearchFilterExpression-stringFilter"></a>
Filters by a string.
Type: [StringFilterExpression](API_StringFilterExpression.md) object
Required: No

 ** stringListFilter **   <a name="deadlinecloud-Type-SearchFilterExpression-stringListFilter"></a>
Filters by a list of strings.
Type: [StringListFilterExpression](API_StringListFilterExpression.md) object
Required: No

## See Also
<a name="API_SearchFilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchFilterExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchFilterExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchFilterExpression)
