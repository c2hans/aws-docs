---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_HierarchyFilter.html
---

# HierarchyFilter
<a name="API_HierarchyFilter"></a>

A `HierarchyFilter` filters data by drilling down through an ordered list of columns. Each level in the list narrows the data by one column, and the selected values at each level determine which values are available at the next.

## Contents
<a name="API_HierarchyFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-HierarchyFilter-Column"></a>
The column that anchors the filter. This column determines the dataset that the whole filter applies to, so every column in `HierarchyLevels` and in `HierarchyTree` must belong to the same dataset.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FilterId **   <a name="QS-Type-HierarchyFilter-FilterId"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** HierarchyLevels **   <a name="QS-Type-HierarchyFilter-HierarchyLevels"></a>
The ordered list of columns that defines the drill-down path of the filter. The first level is the top of the hierarchy. You can specify a maximum of 5 levels.
Type: Array of [HierarchyFilterLevel](API_HierarchyFilterLevel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** MatchOperator **   <a name="QS-Type-HierarchyFilter-MatchOperator"></a>
Determines whether the values selected in `HierarchyTree` are kept or removed. Choose one of the following options:
+  `INCLUDE`: Keep only the selected values.
+  `EXCLUDE`: Remove the selected values.
Type: String
Valid Values: `INCLUDE | EXCLUDE`
Required: Yes

 ** NullOption **   <a name="QS-Type-HierarchyFilter-NullOption"></a>
This option determines how null values should be treated when filtering data.
+  `ALL_VALUES`: Include null values in filtered results.
+  `NULLS_ONLY`: Only include null values in filtered results.
+  `NON_NULLS_ONLY`: Exclude null values from filtered results.
Type: String
Valid Values: `ALL_VALUES | NULLS_ONLY | NON_NULLS_ONLY`
Required: Yes

 ** DefaultFilterControlConfiguration **   <a name="QS-Type-HierarchyFilter-DefaultFilterControlConfiguration"></a>
The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.
Type: [DefaultFilterControlConfiguration](API_DefaultFilterControlConfiguration.md) object
Required: No

 ** HierarchyTree **   <a name="QS-Type-HierarchyFilter-HierarchyTree"></a>
The tree of selected values for the filter. Each node records the values that are selected at one level of the hierarchy, and its children record the selections beneath those values. Omit this attribute to define the drill-down path without restricting any values.
Type: [HierarchyFilterNode](API_HierarchyFilterNode.md) object
Required: No

## See Also
<a name="API_HierarchyFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/HierarchyFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/HierarchyFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/HierarchyFilter)
