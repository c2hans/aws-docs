---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_HierarchyFilterListControl.html
---

# HierarchyFilterListControl
<a name="API_HierarchyFilterListControl"></a>

A control from a hierarchy filter that displays the hierarchy as a list. You can expand a value to see and select the values beneath it, and select either a single value or multiple values.

## Contents
<a name="API_HierarchyFilterListControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterControlId **   <a name="QS-Type-HierarchyFilterListControl-FilterControlId"></a>
The ID of the `HierarchyFilterListControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceFilterId **   <a name="QS-Type-HierarchyFilterListControl-SourceFilterId"></a>
The source filter ID of the `HierarchyFilterListControl`. This must be the `FilterId` of a `HierarchyFilter`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** CommitMode **   <a name="QS-Type-HierarchyFilterListControl-CommitMode"></a>
The visibility configuration of the Apply button on a `HierarchyFilterListControl`.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** ControlSortConfigurations **   <a name="QS-Type-HierarchyFilterListControl-ControlSortConfigurations"></a>
The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.
Type: Array of [ControlSortConfiguration](API_ControlSortConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** ControlTitleFormatText **   <a name="QS-Type-HierarchyFilterListControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-HierarchyFilterListControl-DisplayOptions"></a>
The display options of a control.
Type: [HierarchyFilterListControlDisplayOptions](API_HierarchyFilterListControlDisplayOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-HierarchyFilterListControl-Title"></a>
The title of the `HierarchyFilterListControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Type **   <a name="QS-Type-HierarchyFilterListControl-Type"></a>
The type of the `HierarchyFilterListControl`. Choose one of the following options:
+  `MULTI_SELECT`: The user can select multiple entries from the list.
+  `SINGLE_SELECT`: The user can select a single entry from the list.
Type: String
Valid Values: `MULTI_SELECT | SINGLE_SELECT`
Required: No

## See Also
<a name="API_HierarchyFilterListControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/HierarchyFilterListControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/HierarchyFilterListControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/HierarchyFilterListControl)
