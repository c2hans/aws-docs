---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicCalculatedField.html
---

# TopicCalculatedField
<a name="API_TopicCalculatedField"></a>

A structure that represents a calculated field.

## Contents
<a name="API_TopicCalculatedField_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CalculatedFieldName **   <a name="QS-Type-TopicCalculatedField-CalculatedFieldName"></a>
The calculated field name.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** Expression **   <a name="QS-Type-TopicCalculatedField-Expression"></a>
The calculated field expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** Aggregation **   <a name="QS-Type-TopicCalculatedField-Aggregation"></a>
The default aggregation. Valid values for this structure are `SUM`, `MAX`, `MIN`, `COUNT`, `DISTINCT_COUNT`, and `AVERAGE`.
Type: String
Valid Values: `SUM | MAX | MIN | COUNT | DISTINCT_COUNT | AVERAGE | MEDIAN | STDEV | STDEVP | VAR | VARP`
Required: No

 ** AllowedAggregations **   <a name="QS-Type-TopicCalculatedField-AllowedAggregations"></a>
The list of aggregation types that are allowed for the calculated field. Valid values for this structure are `COUNT`, `DISTINCT_COUNT`, `MIN`, `MAX`, `MEDIAN`, `SUM`, `AVERAGE`, `STDEV`, `STDEVP`, `VAR`, `VARP`, and `PERCENTILE`.
Type: Array of strings
Valid Values: `COUNT | DISTINCT_COUNT | MIN | MAX | MEDIAN | SUM | AVERAGE | STDEV | STDEVP | VAR | VARP | PERCENTILE`
Required: No

 ** CalculatedFieldDescription **   <a name="QS-Type-TopicCalculatedField-CalculatedFieldDescription"></a>
The calculated field description.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** CalculatedFieldSynonyms **   <a name="QS-Type-TopicCalculatedField-CalculatedFieldSynonyms"></a>
The other names or aliases for the calculated field.
Type: Array of strings
Length Constraints: Maximum length of 256.
Required: No

 ** CellValueSynonyms **   <a name="QS-Type-TopicCalculatedField-CellValueSynonyms"></a>
The other names or aliases for the calculated field cell value.
Type: Array of [CellValueSynonym](API_CellValueSynonym.md) objects
Required: No

 ** ColumnDataRole **   <a name="QS-Type-TopicCalculatedField-ColumnDataRole"></a>
The column data role for a calculated field. Valid values for this structure are `DIMENSION` and `MEASURE`.
Type: String
Valid Values: `DIMENSION | MEASURE`
Required: No

 ** ComparativeOrder **   <a name="QS-Type-TopicCalculatedField-ComparativeOrder"></a>
The order in which data is displayed for the calculated field when it's used in a comparative context.
Type: [ComparativeOrder](API_ComparativeOrder.md) object
Required: No

 ** DefaultFormatting **   <a name="QS-Type-TopicCalculatedField-DefaultFormatting"></a>
The default formatting definition.
Type: [DefaultFormatting](API_DefaultFormatting.md) object
Required: No

 ** DisableIndexing **   <a name="QS-Type-TopicCalculatedField-DisableIndexing"></a>
A Boolean value that indicates if a calculated field is visible in the autocomplete.
Type: Boolean
Required: No

 ** IsIncludedInTopic **   <a name="QS-Type-TopicCalculatedField-IsIncludedInTopic"></a>
A boolean value that indicates if a calculated field is included in the topic.
Type: Boolean
Required: No

 ** NeverAggregateInFilter **   <a name="QS-Type-TopicCalculatedField-NeverAggregateInFilter"></a>
A Boolean value that indicates whether to never aggregate calculated field in filters.
Type: Boolean
Required: No

 ** NonAdditive **   <a name="QS-Type-TopicCalculatedField-NonAdditive"></a>
The non additive for the table style target.
Type: Boolean
Required: No

 ** NotAllowedAggregations **   <a name="QS-Type-TopicCalculatedField-NotAllowedAggregations"></a>
The list of aggregation types that are not allowed for the calculated field. Valid values for this structure are `COUNT`, `DISTINCT_COUNT`, `MIN`, `MAX`, `MEDIAN`, `SUM`, `AVERAGE`, `STDEV`, `STDEVP`, `VAR`, `VARP`, and `PERCENTILE`.
Type: Array of strings
Valid Values: `COUNT | DISTINCT_COUNT | MIN | MAX | MEDIAN | SUM | AVERAGE | STDEV | STDEVP | VAR | VARP | PERCENTILE`
Required: No

 ** SemanticType **   <a name="QS-Type-TopicCalculatedField-SemanticType"></a>
The semantic type.
Type: [SemanticType](API_SemanticType.md) object
Required: No

 ** TimeGranularity **   <a name="QS-Type-TopicCalculatedField-TimeGranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
Type: String
Valid Values: `SECOND | MINUTE | HOUR | DAY | WEEK | MONTH | QUARTER | YEAR`
Required: No

## See Also
<a name="API_TopicCalculatedField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicCalculatedField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicCalculatedField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicCalculatedField)
