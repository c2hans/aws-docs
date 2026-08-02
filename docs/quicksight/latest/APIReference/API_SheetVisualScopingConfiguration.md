---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SheetVisualScopingConfiguration.html
---

# SheetVisualScopingConfiguration
<a name="API_SheetVisualScopingConfiguration"></a>

The filter that is applied to the options.

## Contents
<a name="API_SheetVisualScopingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Scope **   <a name="QS-Type-SheetVisualScopingConfiguration-Scope"></a>
The scope of the applied entities. Choose one of the following options:
+  `ALL_VISUALS`
+  `SELECTED_VISUALS`
Type: String
Valid Values: `ALL_VISUALS | SELECTED_VISUALS`
Required: Yes

 ** SheetId **   <a name="QS-Type-SheetVisualScopingConfiguration-SheetId"></a>
The selected sheet that the filter is applied to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** VisualIds **   <a name="QS-Type-SheetVisualScopingConfiguration-VisualIds"></a>
The selected visuals that the filter is applied to.
Type: Array of strings
Array Members: Maximum number of 75 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

## See Also
<a name="API_SheetVisualScopingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SheetVisualScopingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SheetVisualScopingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SheetVisualScopingConfiguration)
