---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AppendOperation.html
---

# AppendOperation
<a name="API_AppendOperation"></a>

A transform operation that combines rows from two data sources by stacking them vertically (union operation).

## Contents
<a name="API_AppendOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alias **   <a name="QS-Type-AppendOperation-Alias"></a>
Alias for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** AppendedColumns **   <a name="QS-Type-AppendOperation-AppendedColumns"></a>
The list of columns to include in the appended result, mapping columns from both sources.
Type: Array of [AppendedColumn](API_AppendedColumn.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2048 items.
Required: Yes

 ** FirstSource **   <a name="QS-Type-AppendOperation-FirstSource"></a>
The first data source to be included in the append operation.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: No

 ** SecondSource **   <a name="QS-Type-AppendOperation-SecondSource"></a>
The second data source to be appended to the first source.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: No

## See Also
<a name="API_AppendOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AppendOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AppendOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AppendOperation)
