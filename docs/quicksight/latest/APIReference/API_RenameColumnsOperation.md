---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RenameColumnsOperation.html
---

# RenameColumnsOperation
<a name="API_RenameColumnsOperation"></a>

A transform operation that renames one or more columns in the dataset.

## Contents
<a name="API_RenameColumnsOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alias **   <a name="QS-Type-RenameColumnsOperation-Alias"></a>
Alias for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** RenameColumnOperations **   <a name="QS-Type-RenameColumnsOperation-RenameColumnOperations"></a>
The list of column rename operations to perform, specifying old and new column names.
Type: Array of [RenameColumnOperation](API_RenameColumnOperation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2048 items.
Required: Yes

 ** Source **   <a name="QS-Type-RenameColumnsOperation-Source"></a>
The source transform operation that provides input data for column renaming.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: Yes

## See Also
<a name="API_RenameColumnsOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RenameColumnsOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RenameColumnsOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RenameColumnsOperation)
