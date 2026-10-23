---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DefaultHierarchyFilterListControlOptions.html
---

# DefaultHierarchyFilterListControlOptions
<a name="API_DefaultHierarchyFilterListControlOptions"></a>

The default options that correspond to the `HierarchyList` filter control type.

## Contents
<a name="API_DefaultHierarchyFilterListControlOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CommitMode **   <a name="QS-Type-DefaultHierarchyFilterListControlOptions-CommitMode"></a>
The visibility configuration of the Apply button on a `HierarchyFilterListControl`.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** ControlSortConfigurations **   <a name="QS-Type-DefaultHierarchyFilterListControlOptions-ControlSortConfigurations"></a>
The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.
Type: Array of [ControlSortConfiguration](API_ControlSortConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** ControlTitleFormatText **   <a name="QS-Type-DefaultHierarchyFilterListControlOptions-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-DefaultHierarchyFilterListControlOptions-DisplayOptions"></a>
The display options of a control.
Type: [HierarchyFilterListControlDisplayOptions](API_HierarchyFilterListControlDisplayOptions.md) object
Required: No

 ** Type **   <a name="QS-Type-DefaultHierarchyFilterListControlOptions-Type"></a>
The type of the `DefaultHierarchyFilterListControlOptions`. Choose one of the following options:
+  `MULTI_SELECT`: The user can select multiple entries from the list.
+  `SINGLE_SELECT`: The user can select a single entry from the list.
Type: String
Valid Values: `MULTI_SELECT | SINGLE_SELECT`
Required: No

## See Also
<a name="API_DefaultHierarchyFilterListControlOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DefaultHierarchyFilterListControlOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DefaultHierarchyFilterListControlOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DefaultHierarchyFilterListControlOptions)
