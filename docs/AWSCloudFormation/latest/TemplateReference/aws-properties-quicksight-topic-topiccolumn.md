---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-topiccolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic TopicColumn
<a name="aws-properties-quicksight-topic-topiccolumn"></a>

Represents a column in a dataset.

## Syntax
<a name="aws-properties-quicksight-topic-topiccolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-topiccolumn-syntax.json"></a>

```
{
  "[Aggregation](#cfn-quicksight-topic-topiccolumn-aggregation)" : {{String}},
  "[AllowedAggregations](#cfn-quicksight-topic-topiccolumn-allowedaggregations)" : {{[ String, ... ]}},
  "[CellValueSynonyms](#cfn-quicksight-topic-topiccolumn-cellvaluesynonyms)" : {{[ CellValueSynonym, ... ]}},
  "[ColumnDataRole](#cfn-quicksight-topic-topiccolumn-columndatarole)" : {{String}},
  "[ColumnDescription](#cfn-quicksight-topic-topiccolumn-columndescription)" : {{String}},
  "[ColumnFriendlyName](#cfn-quicksight-topic-topiccolumn-columnfriendlyname)" : {{String}},
  "[ColumnName](#cfn-quicksight-topic-topiccolumn-columnname)" : {{String}},
  "[ColumnSynonyms](#cfn-quicksight-topic-topiccolumn-columnsynonyms)" : {{[ String, ... ]}},
  "[ComparativeOrder](#cfn-quicksight-topic-topiccolumn-comparativeorder)" : {{ComparativeOrder}},
  "[DefaultFormatting](#cfn-quicksight-topic-topiccolumn-defaultformatting)" : {{DefaultFormatting}},
  "[DisableIndexing](#cfn-quicksight-topic-topiccolumn-disableindexing)" : {{Boolean}},
  "[IsIncludedInTopic](#cfn-quicksight-topic-topiccolumn-isincludedintopic)" : {{Boolean}},
  "[NeverAggregateInFilter](#cfn-quicksight-topic-topiccolumn-neveraggregateinfilter)" : {{Boolean}},
  "[NonAdditive](#cfn-quicksight-topic-topiccolumn-nonadditive)" : {{Boolean}},
  "[NotAllowedAggregations](#cfn-quicksight-topic-topiccolumn-notallowedaggregations)" : {{[ String, ... ]}},
  "[SemanticType](#cfn-quicksight-topic-topiccolumn-semantictype)" : {{SemanticType}},
  "[TimeGranularity](#cfn-quicksight-topic-topiccolumn-timegranularity)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-topiccolumn-syntax.yaml"></a>

```
  [Aggregation](#cfn-quicksight-topic-topiccolumn-aggregation): {{String}}
  [AllowedAggregations](#cfn-quicksight-topic-topiccolumn-allowedaggregations): {{
    - String}}
  [CellValueSynonyms](#cfn-quicksight-topic-topiccolumn-cellvaluesynonyms): {{
    - CellValueSynonym}}
  [ColumnDataRole](#cfn-quicksight-topic-topiccolumn-columndatarole): {{String}}
  [ColumnDescription](#cfn-quicksight-topic-topiccolumn-columndescription): {{String}}
  [ColumnFriendlyName](#cfn-quicksight-topic-topiccolumn-columnfriendlyname): {{String}}
  [ColumnName](#cfn-quicksight-topic-topiccolumn-columnname): {{String}}
  [ColumnSynonyms](#cfn-quicksight-topic-topiccolumn-columnsynonyms): {{
    - String}}
  [ComparativeOrder](#cfn-quicksight-topic-topiccolumn-comparativeorder): {{
    ComparativeOrder}}
  [DefaultFormatting](#cfn-quicksight-topic-topiccolumn-defaultformatting): {{
    DefaultFormatting}}
  [DisableIndexing](#cfn-quicksight-topic-topiccolumn-disableindexing): {{Boolean}}
  [IsIncludedInTopic](#cfn-quicksight-topic-topiccolumn-isincludedintopic): {{Boolean}}
  [NeverAggregateInFilter](#cfn-quicksight-topic-topiccolumn-neveraggregateinfilter): {{Boolean}}
  [NonAdditive](#cfn-quicksight-topic-topiccolumn-nonadditive): {{Boolean}}
  [NotAllowedAggregations](#cfn-quicksight-topic-topiccolumn-notallowedaggregations): {{
    - String}}
  [SemanticType](#cfn-quicksight-topic-topiccolumn-semantictype): {{
    SemanticType}}
  [TimeGranularity](#cfn-quicksight-topic-topiccolumn-timegranularity): {{String}}
```

## Properties
<a name="aws-properties-quicksight-topic-topiccolumn-properties"></a>

`Aggregation`  <a name="cfn-quicksight-topic-topiccolumn-aggregation"></a>
The type of aggregation that is performed on the column data when it's queried.
*Required*: No
*Type*: String
*Allowed values*: `SUM | MAX | MIN | COUNT | DISTINCT_COUNT | AVERAGE | MEDIAN | STDEV | STDEVP | VAR | VARP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedAggregations`  <a name="cfn-quicksight-topic-topiccolumn-allowedaggregations"></a>
The list of aggregation types that are allowed for the column. Valid values for this structure are `COUNT`, `DISTINCT_COUNT`, `MIN`, `MAX`, `MEDIAN`, `SUM`, `AVERAGE`, `STDEV`, `STDEVP`, `VAR`, `VARP`, and `PERCENTILE`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CellValueSynonyms`  <a name="cfn-quicksight-topic-topiccolumn-cellvaluesynonyms"></a>
The other names or aliases for the column cell value.
*Required*: No
*Type*: Array of [CellValueSynonym](aws-properties-quicksight-topic-cellvaluesynonym.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnDataRole`  <a name="cfn-quicksight-topic-topiccolumn-columndatarole"></a>
The role of the column in the data. Valid values are `DIMENSION` and `MEASURE`.
*Required*: No
*Type*: String
*Allowed values*: `DIMENSION | MEASURE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnDescription`  <a name="cfn-quicksight-topic-topiccolumn-columndescription"></a>
A description of the column and its contents.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnFriendlyName`  <a name="cfn-quicksight-topic-topiccolumn-columnfriendlyname"></a>
A user-friendly name for the column.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnName`  <a name="cfn-quicksight-topic-topiccolumn-columnname"></a>
The name of the column.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnSynonyms`  <a name="cfn-quicksight-topic-topiccolumn-columnsynonyms"></a>
The other names or aliases for the column.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComparativeOrder`  <a name="cfn-quicksight-topic-topiccolumn-comparativeorder"></a>
The order in which data is displayed for the column when it's used in a comparative context.
*Required*: No
*Type*: [ComparativeOrder](aws-properties-quicksight-topic-comparativeorder.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultFormatting`  <a name="cfn-quicksight-topic-topiccolumn-defaultformatting"></a>
The default formatting used for values in the column.
*Required*: No
*Type*: [DefaultFormatting](aws-properties-quicksight-topic-defaultformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisableIndexing`  <a name="cfn-quicksight-topic-topiccolumn-disableindexing"></a>
A Boolean value that indicates whether the column shows in the autocomplete functionality.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsIncludedInTopic`  <a name="cfn-quicksight-topic-topiccolumn-isincludedintopic"></a>
A Boolean value that indicates whether the column is included in the query results.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NeverAggregateInFilter`  <a name="cfn-quicksight-topic-topiccolumn-neveraggregateinfilter"></a>
A Boolean value that indicates whether to aggregate the column data when it's used in a filter context.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NonAdditive`  <a name="cfn-quicksight-topic-topiccolumn-nonadditive"></a>
The non additive value for the column.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotAllowedAggregations`  <a name="cfn-quicksight-topic-topiccolumn-notallowedaggregations"></a>
The list of aggregation types that are not allowed for the column. Valid values for this structure are `COUNT`, `DISTINCT_COUNT`, `MIN`, `MAX`, `MEDIAN`, `SUM`, `AVERAGE`, `STDEV`, `STDEVP`, `VAR`, `VARP`, and `PERCENTILE`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SemanticType`  <a name="cfn-quicksight-topic-topiccolumn-semantictype"></a>
The semantic type of data contained in the column.
*Required*: No
*Type*: [SemanticType](aws-properties-quicksight-topic-semantictype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeGranularity`  <a name="cfn-quicksight-topic-topiccolumn-timegranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
*Required*: No
*Type*: String
*Allowed values*: `SECOND | MINUTE | HOUR | DAY | WEEK | MONTH | QUARTER | YEAR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
