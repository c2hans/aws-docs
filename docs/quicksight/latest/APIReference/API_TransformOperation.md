---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TransformOperation.html
---

# TransformOperation
<a name="API_TransformOperation"></a>

A data transformation on a logical table. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

## Contents
<a name="API_TransformOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CastColumnTypeOperation **   <a name="QS-Type-TransformOperation-CastColumnTypeOperation"></a>
A transform operation that casts a column to a different type.
Type: [CastColumnTypeOperation](API_CastColumnTypeOperation.md) object
Required: No

 ** CreateColumnsOperation **   <a name="QS-Type-TransformOperation-CreateColumnsOperation"></a>
An operation that creates calculated columns. Columns created in one such operation form a lexical closure.
Type: [CreateColumnsOperation](API_CreateColumnsOperation.md) object
Required: No

 ** FilterOperation **   <a name="QS-Type-TransformOperation-FilterOperation"></a>
An operation that filters rows based on some condition.
Type: [FilterOperation](API_FilterOperation.md) object
Required: No

 ** OverrideDatasetParameterOperation **   <a name="QS-Type-TransformOperation-OverrideDatasetParameterOperation"></a>
A transform operation that overrides the dataset parameter values that are defined in another dataset.
Type: [OverrideDatasetParameterOperation](API_OverrideDatasetParameterOperation.md) object
Required: No

 ** ProjectOperation **   <a name="QS-Type-TransformOperation-ProjectOperation"></a>
An operation that projects columns. Operations that come after a projection can only refer to projected columns.
Type: [ProjectOperation](API_ProjectOperation.md) object
Required: No

 ** RenameColumnOperation **   <a name="QS-Type-TransformOperation-RenameColumnOperation"></a>
An operation that renames a column.
Type: [RenameColumnOperation](API_RenameColumnOperation.md) object
Required: No

 ** TagColumnOperation **   <a name="QS-Type-TransformOperation-TagColumnOperation"></a>
An operation that tags a column with additional information.
Type: [TagColumnOperation](API_TagColumnOperation.md) object
Required: No

 ** UntagColumnOperation **   <a name="QS-Type-TransformOperation-UntagColumnOperation"></a>
A transform operation that removes tags associated with a column.
Type: [UntagColumnOperation](API_UntagColumnOperation.md) object
Required: No

## See Also
<a name="API_TransformOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TransformOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TransformOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TransformOperation)
