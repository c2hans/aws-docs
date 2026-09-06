---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterGroup.html
---

# FilterGroup
<a name="API_FilterGroup"></a>

A grouping of individual filters. Filter groups are applied to the same group of visuals.

For more information, see [Adding filter conditions (group filters) with AND and OR operators](https://docs.aws.amazon.com/quicksight/latest/user/add-a-compound-filter.html) in the *Amazon Quick Suite User Guide*.

## Contents
<a name="API_FilterGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CrossDataset **   <a name="QS-Type-FilterGroup-CrossDataset"></a>
The filter new feature which can apply filter group to all data sets. Choose one of the following options:
+  `ALL_DATASETS`
+  `SINGLE_DATASET`
Type: String
Valid Values: `ALL_DATASETS | SINGLE_DATASET`
Required: Yes

 ** FilterGroupId **   <a name="QS-Type-FilterGroup-FilterGroupId"></a>
The value that uniquely identifies a `FilterGroup` within a dashboard, template, or analysis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Filters **   <a name="QS-Type-FilterGroup-Filters"></a>
The list of filters that are present in a `FilterGroup`.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Maximum number of 20 items.
Required: Yes

 ** ScopeConfiguration **   <a name="QS-Type-FilterGroup-ScopeConfiguration"></a>
The configuration that specifies what scope to apply to a `FilterGroup`.
This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
Type: [FilterScopeConfiguration](API_FilterScopeConfiguration.md) object
Required: Yes

 ** Status **   <a name="QS-Type-FilterGroup-Status"></a>
The status of the `FilterGroup`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_FilterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterGroup)
