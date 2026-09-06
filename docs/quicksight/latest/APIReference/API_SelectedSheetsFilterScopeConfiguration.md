---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SelectedSheetsFilterScopeConfiguration.html
---

# SelectedSheetsFilterScopeConfiguration
<a name="API_SelectedSheetsFilterScopeConfiguration"></a>

The configuration for applying a filter to specific sheets or visuals. You can apply this filter to multiple visuals that are on one sheet or to all visuals on a sheet.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_SelectedSheetsFilterScopeConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SheetVisualScopingConfigurations **   <a name="QS-Type-SelectedSheetsFilterScopeConfiguration-SheetVisualScopingConfigurations"></a>
The sheet ID and visual IDs of the sheet and visuals that the filter is applied to.
Type: Array of [SheetVisualScopingConfiguration](API_SheetVisualScopingConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 75 items.
Required: No

## See Also
<a name="API_SelectedSheetsFilterScopeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SelectedSheetsFilterScopeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SelectedSheetsFilterScopeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SelectedSheetsFilterScopeConfiguration)
