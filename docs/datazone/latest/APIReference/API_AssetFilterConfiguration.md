---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetFilterConfiguration.html
---

# AssetFilterConfiguration
<a name="API_AssetFilterConfiguration"></a>

The configuration details of the asset filter.

## Contents
<a name="API_AssetFilterConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** columnConfiguration **   <a name="datazone-Type-AssetFilterConfiguration-columnConfiguration"></a>
The column configuration of the asset filter.
Type: [ColumnFilterConfiguration](API_ColumnFilterConfiguration.md) object
Required: No

 ** rowConfiguration **   <a name="datazone-Type-AssetFilterConfiguration-rowConfiguration"></a>
The row configuration of the asset filter.
Type: [RowFilterConfiguration](API_RowFilterConfiguration.md) object
Required: No

## See Also
<a name="API_AssetFilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetFilterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetFilterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetFilterConfiguration)
