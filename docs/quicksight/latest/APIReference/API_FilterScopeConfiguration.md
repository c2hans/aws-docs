---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterScopeConfiguration.html
---

# FilterScopeConfiguration
<a name="API_FilterScopeConfiguration"></a>

The scope configuration for a `FilterGroup`.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_FilterScopeConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllSheets **   <a name="QS-Type-FilterScopeConfiguration-AllSheets"></a>
The configuration that applies a filter to all sheets. When you choose `AllSheets` as the value for a `FilterScopeConfiguration`, this filter is applied to all visuals of all sheets in an Analysis, Dashboard, or Template. The `AllSheetsFilterScopeConfiguration` is chosen.
Type: [AllSheetsFilterScopeConfiguration](API_AllSheetsFilterScopeConfiguration.md) object
Required: No

 ** SelectedSheets **   <a name="QS-Type-FilterScopeConfiguration-SelectedSheets"></a>
The configuration for applying a filter to specific sheets.
Type: [SelectedSheetsFilterScopeConfiguration](API_SelectedSheetsFilterScopeConfiguration.md) object
Required: No

## See Also
<a name="API_FilterScopeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterScopeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterScopeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterScopeConfiguration)
