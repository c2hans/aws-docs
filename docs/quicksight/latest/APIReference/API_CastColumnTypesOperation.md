---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CastColumnTypesOperation.html
---

# CastColumnTypesOperation
<a name="API_CastColumnTypesOperation"></a>

A transform operation that changes the data types of one or more columns in the dataset.

## Contents
<a name="API_CastColumnTypesOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alias **   <a name="QS-Type-CastColumnTypesOperation-Alias"></a>
Alias for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** CastColumnTypeOperations **   <a name="QS-Type-CastColumnTypesOperation-CastColumnTypeOperations"></a>
The list of column type casting operations to perform.
Type: Array of [CastColumnTypeOperation](API_CastColumnTypeOperation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2048 items.
Required: Yes

 ** Source **   <a name="QS-Type-CastColumnTypesOperation-Source"></a>
The source transform operation that provides input data for the type casting.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: Yes

## See Also
<a name="API_CastColumnTypesOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CastColumnTypesOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CastColumnTypesOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CastColumnTypesOperation)
