---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-intermediatetable-aggregationthreshold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IntermediateTable AggregationThreshold
<a name="aws-properties-cleanrooms-intermediatetable-aggregationthreshold"></a>

Specifies the minimum number of distinct identities that each query output group must represent.

## Syntax
<a name="aws-properties-cleanrooms-intermediatetable-aggregationthreshold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-intermediatetable-aggregationthreshold-syntax.json"></a>

```
{
  "[AllowedAggregateExpressionType](#cfn-cleanrooms-intermediatetable-aggregationthreshold-allowedaggregateexpressiontype)" : {{String}},
  "[IdentityColumns](#cfn-cleanrooms-intermediatetable-aggregationthreshold-identitycolumns)" : {{[ String, ... ]}},
  "[MinimumIdentityCount](#cfn-cleanrooms-intermediatetable-aggregationthreshold-minimumidentitycount)" : {{Integer}},
  "[OutputColumnThresholds](#cfn-cleanrooms-intermediatetable-aggregationthreshold-outputcolumnthresholds)" : {{[ OutputColumnThreshold, ... ]}},
  "[Type](#cfn-cleanrooms-intermediatetable-aggregationthreshold-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-intermediatetable-aggregationthreshold-syntax.yaml"></a>

```
  [AllowedAggregateExpressionType](#cfn-cleanrooms-intermediatetable-aggregationthreshold-allowedaggregateexpressiontype): {{String}}
  [IdentityColumns](#cfn-cleanrooms-intermediatetable-aggregationthreshold-identitycolumns): {{
    - String}}
  [MinimumIdentityCount](#cfn-cleanrooms-intermediatetable-aggregationthreshold-minimumidentitycount): {{Integer}}
  [OutputColumnThresholds](#cfn-cleanrooms-intermediatetable-aggregationthreshold-outputcolumnthresholds): {{
    - OutputColumnThreshold}}
  [Type](#cfn-cleanrooms-intermediatetable-aggregationthreshold-type): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-intermediatetable-aggregationthreshold-properties"></a>

`AllowedAggregateExpressionType`  <a name="cfn-cleanrooms-intermediatetable-aggregationthreshold-allowedaggregateexpressiontype"></a>
Specifies whether a query can aggregate a transformed column. This applies to the arguments of both aggregate and window functions. Valid values are:
`COLUMNS_ONLY` – A query can aggregate only a direct column reference, such as `SUM(amount)`, or a constant. AWS Clean Rooms rejects a query that transforms a column and then aggregates it, such as `SUM(amount * 2)` or `SUM(ROUND(amount))`.
`ANY_EXPRESSION` – A query can aggregate any expression. This includes arithmetic, such as `SUM(price * quantity)`; a cast, such as `SUM(CAST(amount AS DECIMAL))`; a nested function call, such as `SUM(COALESCE(amount, 0))`; and a conditional, such as `SUM(CASE WHEN region = 'EU' THEN amount ELSE 0 END)`.
*Required*: Yes
*Type*: String
*Allowed values*: `COLUMNS_ONLY | ANY_EXPRESSION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityColumns`  <a name="cfn-cleanrooms-intermediatetable-aggregationthreshold-identitycolumns"></a>
The identity column, such as `user_id`, whose distinct values AWS Clean Rooms counts to enforce minimum aggregation thresholds. Currently, you can specify only one column, and its data type must be string, varchar, or char.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumIdentityCount`  <a name="cfn-cleanrooms-intermediatetable-aggregationthreshold-minimumidentitycount"></a>
The minimum number of distinct identities that each query output group must represent. This threshold applies to all output columns in the table. To override this threshold for a specific column, use `outputColumnThresholds`.
*Required*: Yes
*Type*: Integer
*Minimum*: `2`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputColumnThresholds`  <a name="cfn-cleanrooms-intermediatetable-aggregationthreshold-outputcolumnthresholds"></a>
The per-column overrides of `minimumIdentityCount`. An output column without an override uses `minimumIdentityCount`.
*Required*: No
*Type*: Array of [OutputColumnThreshold](aws-properties-cleanrooms-intermediatetable-outputcolumnthreshold.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cleanrooms-intermediatetable-aggregationthreshold-type"></a>
The type of aggregation that the threshold enforces. Currently, the only supported value is `COUNT_DISTINCT`, which counts the distinct values in the identity column.
*Required*: Yes
*Type*: String
*Allowed values*: `COUNT_DISTINCT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
