---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-metricdataquery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective MetricDataQuery
<a name="aws-properties-applicationsignals-servicelevelobjective-metricdataquery"></a>

Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

Each `MetricDataQuery` in the `MetricDataQueries` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single `MetricDataQueries` array can include as many as 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, exactly one must have true as the value for `ReturnData`. The result of this expression used for the SLO.

For more information about metric math expressions, see [Use metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html).

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-metricdataquery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-metricdataquery-syntax.json"></a>

```
{
  "[AccountId](#cfn-applicationsignals-servicelevelobjective-metricdataquery-accountid)" : {{String}},
  "[Expression](#cfn-applicationsignals-servicelevelobjective-metricdataquery-expression)" : {{String}},
  "[Id](#cfn-applicationsignals-servicelevelobjective-metricdataquery-id)" : {{String}},
  "[MetricStat](#cfn-applicationsignals-servicelevelobjective-metricdataquery-metricstat)" : {{MetricStat}},
  "[ReturnData](#cfn-applicationsignals-servicelevelobjective-metricdataquery-returndata)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-metricdataquery-syntax.yaml"></a>

```
  [AccountId](#cfn-applicationsignals-servicelevelobjective-metricdataquery-accountid): {{String}}
  [Expression](#cfn-applicationsignals-servicelevelobjective-metricdataquery-expression): {{String}}
  [Id](#cfn-applicationsignals-servicelevelobjective-metricdataquery-id): {{String}}
  [MetricStat](#cfn-applicationsignals-servicelevelobjective-metricdataquery-metricstat): {{
    MetricStat}}
  [ReturnData](#cfn-applicationsignals-servicelevelobjective-metricdataquery-returndata): {{Boolean}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-metricdataquery-properties"></a>

`AccountId`  <a name="cfn-applicationsignals-servicelevelobjective-metricdataquery-accountid"></a>
The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-applicationsignals-servicelevelobjective-metricdataquery-expression"></a>
This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this `MetricDataQueries` structure.
A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide*.
Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-applicationsignals-servicelevelobjective-metricdataquery-id"></a>
A short name used to tie this object to the results in the response. This `Id` must be unique within a `MetricDataQueries` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricStat`  <a name="cfn-applicationsignals-servicelevelobjective-metricdataquery-metricstat"></a>
A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.
Within one `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.
*Required*: No
*Type*: [MetricStat](aws-properties-applicationsignals-servicelevelobjective-metricstat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReturnData`  <a name="cfn-applicationsignals-servicelevelobjective-metricdataquery-returndata"></a>
Use this only if you are using a metric math expression for the SLO. Specify `true` for `ReturnData` for only the one expression result to use as the alarm. For all other metrics and expressions in the same `CreateServiceLevelObjective` operation, specify `ReturnData` as `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
