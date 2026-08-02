---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TransformStep.html
---

# TransformStep
<a name="API_TransformStep"></a>

A step in data preparation that performs a specific operation on the data.

## Contents
<a name="API_TransformStep_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AggregateStep **   <a name="QS-Type-TransformStep-AggregateStep"></a>
A transform step that groups data and applies aggregation functions to calculate summary values.
Type: [AggregateOperation](API_AggregateOperation.md) object
Required: No

 ** AppendStep **   <a name="QS-Type-TransformStep-AppendStep"></a>
A transform step that combines rows from multiple sources by stacking them vertically.
Type: [AppendOperation](API_AppendOperation.md) object
Required: No

 ** CastColumnTypesStep **   <a name="QS-Type-TransformStep-CastColumnTypesStep"></a>
A transform step that changes the data types of one or more columns.
Type: [CastColumnTypesOperation](API_CastColumnTypesOperation.md) object
Required: No

 ** CreateColumnsStep **   <a name="QS-Type-TransformStep-CreateColumnsStep"></a>
A transform operation that creates calculated columns. Columns created in one such operation form a lexical closure.
Type: [CreateColumnsOperation](API_CreateColumnsOperation.md) object
Required: No

 ** FiltersStep **   <a name="QS-Type-TransformStep-FiltersStep"></a>
A transform step that applies filter conditions.
Type: [FiltersOperation](API_FiltersOperation.md) object
Required: No

 ** ImportTableStep **   <a name="QS-Type-TransformStep-ImportTableStep"></a>
A transform step that brings data from a source table.
Type: [ImportTableOperation](API_ImportTableOperation.md) object
Required: No

 ** JoinStep **   <a name="QS-Type-TransformStep-JoinStep"></a>
A transform step that combines data from two sources based on specified join conditions.
Type: [JoinOperation](API_JoinOperation.md) object
Required: No

 ** PivotStep **   <a name="QS-Type-TransformStep-PivotStep"></a>
A transform step that converts row values into columns to reshape the data structure.
Type: [PivotOperation](API_PivotOperation.md) object
Required: No

 ** ProjectStep **   <a name="QS-Type-TransformStep-ProjectStep"></a>
A transform operation that projects columns. Operations that come after a projection can only refer to projected columns.
Type: [ProjectOperation](API_ProjectOperation.md) object
Required: No

 ** RenameColumnsStep **   <a name="QS-Type-TransformStep-RenameColumnsStep"></a>
A transform step that changes the names of one or more columns.
Type: [RenameColumnsOperation](API_RenameColumnsOperation.md) object
Required: No

 ** UnpivotStep **   <a name="QS-Type-TransformStep-UnpivotStep"></a>
A transform step that converts columns into rows to normalize the data structure.
Type: [UnpivotOperation](API_UnpivotOperation.md) object
Required: No

## See Also
<a name="API_TransformStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TransformStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TransformStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TransformStep)
