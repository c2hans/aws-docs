---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

With a `Filter`, you can remove portions of data from a particular visual or view.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_Filter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CategoryFilter **   <a name="QS-Type-Filter-CategoryFilter"></a>
A `CategoryFilter` filters text values.
For more information, see [Adding text filters](https://docs.aws.amazon.com/quicksight/latest/user/add-a-text-filter-data-prep.html) in the *Amazon Quick Suite User Guide*.
Type: [CategoryFilter](API_CategoryFilter.md) object
Required: No

 ** NestedFilter **   <a name="QS-Type-Filter-NestedFilter"></a>
A `NestedFilter` filters data with a subset of data that is defined by the nested inner filter.
Type: [NestedFilter](API_NestedFilter.md) object
Required: No

 ** NumericEqualityFilter **   <a name="QS-Type-Filter-NumericEqualityFilter"></a>
A `NumericEqualityFilter` filters numeric values that equal or do not equal a given numeric value.
Type: [NumericEqualityFilter](API_NumericEqualityFilter.md) object
Required: No

 ** NumericRangeFilter **   <a name="QS-Type-Filter-NumericRangeFilter"></a>
A `NumericRangeFilter` filters numeric values that are either inside or outside a given numeric range.
Type: [NumericRangeFilter](API_NumericRangeFilter.md) object
Required: No

 ** RelativeDatesFilter **   <a name="QS-Type-Filter-RelativeDatesFilter"></a>
A `RelativeDatesFilter` filters date values that are relative to a given date.
Type: [RelativeDatesFilter](API_RelativeDatesFilter.md) object
Required: No

 ** TimeEqualityFilter **   <a name="QS-Type-Filter-TimeEqualityFilter"></a>
A `TimeEqualityFilter` filters date-time values that equal or do not equal a given date/time value.
Type: [TimeEqualityFilter](API_TimeEqualityFilter.md) object
Required: No

 ** TimeRangeFilter **   <a name="QS-Type-Filter-TimeRangeFilter"></a>
A `TimeRangeFilter` filters date-time values that are either inside or outside a given date/time range.
Type: [TimeRangeFilter](API_TimeRangeFilter.md) object
Required: No

 ** TopBottomFilter **   <a name="QS-Type-Filter-TopBottomFilter"></a>
A `TopBottomFilter` filters data to the top or bottom values for a given column.
Type: [TopBottomFilter](API_TopBottomFilter.md) object
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Filter)
