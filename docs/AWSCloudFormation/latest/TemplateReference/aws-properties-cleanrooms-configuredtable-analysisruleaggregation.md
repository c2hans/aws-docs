---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable AnalysisRuleAggregation
<a name="aws-properties-cleanrooms-configuredtable-analysisruleaggregation"></a>

A type of analysis rule that enables query structure and specified queries that produce aggregate statistics.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-analysisruleaggregation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-analysisruleaggregation-syntax.json"></a>

```
{
  "[AdditionalAnalyses](#cfn-cleanrooms-configuredtable-analysisruleaggregation-additionalanalyses)" : {{String}},
  "[AggregateColumns](#cfn-cleanrooms-configuredtable-analysisruleaggregation-aggregatecolumns)" : {{[ AggregateColumn, ... ]}},
  "[AllowedJoinOperators](#cfn-cleanrooms-configuredtable-analysisruleaggregation-allowedjoinoperators)" : {{[ String, ... ]}},
  "[DimensionColumns](#cfn-cleanrooms-configuredtable-analysisruleaggregation-dimensioncolumns)" : {{[ String, ... ]}},
  "[JoinColumns](#cfn-cleanrooms-configuredtable-analysisruleaggregation-joincolumns)" : {{[ String, ... ]}},
  "[JoinRequired](#cfn-cleanrooms-configuredtable-analysisruleaggregation-joinrequired)" : {{String}},
  "[OutputConstraints](#cfn-cleanrooms-configuredtable-analysisruleaggregation-outputconstraints)" : {{[ AggregationConstraint, ... ]}},
  "[ScalarFunctions](#cfn-cleanrooms-configuredtable-analysisruleaggregation-scalarfunctions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-analysisruleaggregation-syntax.yaml"></a>

```
  [AdditionalAnalyses](#cfn-cleanrooms-configuredtable-analysisruleaggregation-additionalanalyses): {{String}}
  [AggregateColumns](#cfn-cleanrooms-configuredtable-analysisruleaggregation-aggregatecolumns): {{
    - AggregateColumn}}
  [AllowedJoinOperators](#cfn-cleanrooms-configuredtable-analysisruleaggregation-allowedjoinoperators): {{
    - String}}
  [DimensionColumns](#cfn-cleanrooms-configuredtable-analysisruleaggregation-dimensioncolumns): {{
    - String}}
  [JoinColumns](#cfn-cleanrooms-configuredtable-analysisruleaggregation-joincolumns): {{
    - String}}
  [JoinRequired](#cfn-cleanrooms-configuredtable-analysisruleaggregation-joinrequired): {{String}}
  [OutputConstraints](#cfn-cleanrooms-configuredtable-analysisruleaggregation-outputconstraints): {{
    - AggregationConstraint}}
  [ScalarFunctions](#cfn-cleanrooms-configuredtable-analysisruleaggregation-scalarfunctions): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-analysisruleaggregation-properties"></a>

`AdditionalAnalyses`  <a name="cfn-cleanrooms-configuredtable-analysisruleaggregation-additionalanalyses"></a>
 An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.
The `additionalAnalyses` parameter is currently supported for the list analysis rule (`AnalysisRuleList`) and the custom analysis rule (`AnalysisRuleCustom`).
*Required*: No
*Type*: String
*Allowed values*: `ALLOWED | REQUIRED | NOT_ALLOWED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AggregateColumns`  <a name="cfn-cleanrooms-configuredtable-analysisruleaggregation-aggregatecolumns"></a>
The columns that query runners are allowed to use in aggregation queries.
*Required*: Yes
*Type*: Array of [AggregateColumn](aws-properties-cleanrooms-configuredtable-aggregatecolumn.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedJoinOperators`  <a name="cfn-cleanrooms-configuredtable-analysisruleaggregation-allowedjoinoperators"></a>
Which logical operators (if any) are to be used in an INNER JOIN match condition. Default is `AND`.
*Required*: No
*Type*: Array of String
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DimensionColumns`  <a name="cfn-cleanrooms-configuredtable-analysisruleaggregation-dimensioncolumns"></a>
The columns that query runners are allowed to select, group by, or filter by.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JoinColumns`  <a name="cfn-cleanrooms-configuredtable-analysisruleaggregation-joincolumns"></a>
Columns in configured table that can be used in join statements and/or as aggregate columns. They can never be outputted directly.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JoinRequired`  <a name="cfn-cleanrooms-configuredtable-analysisruleaggregation-joinrequired"></a>
Control that requires member who runs query to do a join with their configured table and/or other configured table in query.
*Required*: No
*Type*: String
*Allowed values*: `QUERY_RUNNER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputConstraints`  <a name="cfn-cleanrooms-configuredtable-analysisruleaggregation-outputconstraints"></a>
Columns that must meet a specific threshold value (after an aggregation function is applied to it) for each output row to be returned.
*Required*: Yes
*Type*: Array of [AggregationConstraint](aws-properties-cleanrooms-configuredtable-aggregationconstraint.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalarFunctions`  <a name="cfn-cleanrooms-configuredtable-analysisruleaggregation-scalarfunctions"></a>
Set of scalar functions that are allowed to be used on dimension columns and the output of aggregation of metrics.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
