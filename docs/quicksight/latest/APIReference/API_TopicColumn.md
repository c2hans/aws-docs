---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicColumn.html
---

# TopicColumn
<a name="API_TopicColumn"></a>

Represents a column in a dataset.

## Contents
<a name="API_TopicColumn_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnName **   <a name="QS-Type-TopicColumn-ColumnName"></a>
The name of the column.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** Aggregation **   <a name="QS-Type-TopicColumn-Aggregation"></a>
The type of aggregation that is performed on the column data when it's queried.
Type: String
Valid Values: `SUM | MAX | MIN | COUNT | DISTINCT_COUNT | AVERAGE | MEDIAN | STDEV | STDEVP | VAR | VARP`
Required: No

 ** AllowedAggregations **   <a name="QS-Type-TopicColumn-AllowedAggregations"></a>
The list of aggregation types that are allowed for the column. Valid values for this structure are `COUNT`, `DISTINCT_COUNT`, `MIN`, `MAX`, `MEDIAN`, `SUM`, `AVERAGE`, `STDEV`, `STDEVP`, `VAR`, `VARP`, and `PERCENTILE`.
Type: Array of strings
Valid Values: `COUNT | DISTINCT_COUNT | MIN | MAX | MEDIAN | SUM | AVERAGE | STDEV | STDEVP | VAR | VARP | PERCENTILE`
Required: No

 ** CellValueSynonyms **   <a name="QS-Type-TopicColumn-CellValueSynonyms"></a>
The other names or aliases for the column cell value.
Type: Array of [CellValueSynonym](API_CellValueSynonym.md) objects
Required: No

 ** ColumnDataRole **   <a name="QS-Type-TopicColumn-ColumnDataRole"></a>
The role of the column in the data. Valid values are `DIMENSION` and `MEASURE`.
Type: String
Valid Values: `DIMENSION | MEASURE`
Required: No

 ** ColumnDescription **   <a name="QS-Type-TopicColumn-ColumnDescription"></a>
A description of the column and its contents.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** ColumnFriendlyName **   <a name="QS-Type-TopicColumn-ColumnFriendlyName"></a>
A user-friendly name for the column.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** ColumnSynonyms **   <a name="QS-Type-TopicColumn-ColumnSynonyms"></a>
The other names or aliases for the column.
Type: Array of strings
Length Constraints: Maximum length of 256.
Required: No

 ** ComparativeOrder **   <a name="QS-Type-TopicColumn-ComparativeOrder"></a>
The order in which data is displayed for the column when it's used in a comparative context.
Type: [ComparativeOrder](API_ComparativeOrder.md) object
Required: No

 ** DefaultFormatting **   <a name="QS-Type-TopicColumn-DefaultFormatting"></a>
The default formatting used for values in the column.
Type: [DefaultFormatting](API_DefaultFormatting.md) object
Required: No

 ** DisableIndexing **   <a name="QS-Type-TopicColumn-DisableIndexing"></a>
A Boolean value that indicates whether the column shows in the autocomplete functionality.
Type: Boolean
Required: No

 ** IsIncludedInTopic **   <a name="QS-Type-TopicColumn-IsIncludedInTopic"></a>
A Boolean value that indicates whether the column is included in the query results.
Type: Boolean
Required: No

 ** NeverAggregateInFilter **   <a name="QS-Type-TopicColumn-NeverAggregateInFilter"></a>
A Boolean value that indicates whether to aggregate the column data when it's used in a filter context.
Type: Boolean
Required: No

 ** NonAdditive **   <a name="QS-Type-TopicColumn-NonAdditive"></a>
The non additive value for the column.
Type: Boolean
Required: No

 ** NotAllowedAggregations **   <a name="QS-Type-TopicColumn-NotAllowedAggregations"></a>
The list of aggregation types that are not allowed for the column. Valid values for this structure are `COUNT`, `DISTINCT_COUNT`, `MIN`, `MAX`, `MEDIAN`, `SUM`, `AVERAGE`, `STDEV`, `STDEVP`, `VAR`, `VARP`, and `PERCENTILE`.
Type: Array of strings
Valid Values: `COUNT | DISTINCT_COUNT | MIN | MAX | MEDIAN | SUM | AVERAGE | STDEV | STDEVP | VAR | VARP | PERCENTILE`
Required: No

 ** SemanticType **   <a name="QS-Type-TopicColumn-SemanticType"></a>
The semantic type of data contained in the column.
Type: [SemanticType](API_SemanticType.md) object
Required: No

 ** TimeGranularity **   <a name="QS-Type-TopicColumn-TimeGranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
Type: String
Valid Values: `SECOND | MINUTE | HOUR | DAY | WEEK | MONTH | QUARTER | YEAR`
Required: No

## See Also
<a name="API_TopicColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicColumn)
