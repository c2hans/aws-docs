---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ImportTableOperationSource.html
---

# ImportTableOperationSource
<a name="API_ImportTableOperationSource"></a>

Specifies the source table and column mappings for an import table operation.

## Contents
<a name="API_ImportTableOperationSource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SourceTableId **   <a name="QS-Type-ImportTableOperationSource-SourceTableId"></a>
The identifier of the source table to import data from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-]*`
Required: Yes

 ** ColumnIdMappings **   <a name="QS-Type-ImportTableOperationSource-ColumnIdMappings"></a>
The mappings between source column identifiers and target column identifiers during the import.
Type: Array of [DataSetColumnIdMapping](API_DataSetColumnIdMapping.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2048 items.
Required: No

## See Also
<a name="API_ImportTableOperationSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ImportTableOperationSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ImportTableOperationSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ImportTableOperationSource)
