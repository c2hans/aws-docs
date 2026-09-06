---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-metric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Metric
<a name="aws-resource-connect-metric"></a>

Creates a new metric definition for the specified Connect Customer instance. You can create custom metrics that use formulas referencing existing AWS-managed metrics, optionally with filters applied.

## Syntax
<a name="aws-resource-connect-metric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-metric-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::Metric",
  "Properties" : {
      "[Description](#cfn-connect-metric-description)" : {{String}},
      "[InstanceArn](#cfn-connect-metric-instancearn)" : {{String}},
      "[MetricCalculation](#cfn-connect-metric-metriccalculation)" : {{MetricCalculation}},
      "[Name](#cfn-connect-metric-name)" : {{String}},
      "[PositiveTrendIndicator](#cfn-connect-metric-positivetrendindicator)" : {{String}},
      "[Status](#cfn-connect-metric-status)" : {{String}},
      "[Tags](#cfn-connect-metric-tags)" : {{[ Tag, ... ]}},
      "[Unit](#cfn-connect-metric-unit)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-metric-syntax.yaml"></a>

```
Type: AWS::Connect::Metric
Properties:
  [Description](#cfn-connect-metric-description): {{String}}
  [InstanceArn](#cfn-connect-metric-instancearn): {{String}}
  [MetricCalculation](#cfn-connect-metric-metriccalculation): {{
    MetricCalculation}}
  [Name](#cfn-connect-metric-name): {{String}}
  [PositiveTrendIndicator](#cfn-connect-metric-positivetrendindicator): {{String}}
  [Status](#cfn-connect-metric-status): {{String}}
  [Tags](#cfn-connect-metric-tags): {{
    - Tag}}
  [Unit](#cfn-connect-metric-unit): {{String}}
```

## Properties
<a name="aws-resource-connect-metric-properties"></a>

`Description`  <a name="cfn-connect-metric-description"></a>
The description of the metric.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-metric-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricCalculation`  <a name="cfn-connect-metric-metriccalculation"></a>
The calculation definition for the metric.
*Required*: No
*Type*: [MetricCalculation](aws-properties-connect-metric-metriccalculation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-metric-name"></a>
The name of the metric.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PositiveTrendIndicator`  <a name="cfn-connect-metric-positivetrendindicator"></a>
How an increase in the metric value should be interpreted. Valid values: `POSITIVE`, `NEUTRAL`, `NEGATIVE`.
*Required*: No
*Type*: String
*Allowed values*: `POSITIVE | NEGATIVE | NEUTRAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-connect-metric-status"></a>
The publish status of the metric. Valid values: `PUBLISHED` \| `SAVED`.
*Required*: No
*Type*: String
*Allowed values*: `SAVED | PUBLISHED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-connect-metric-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-metric-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-connect-metric-unit"></a>
The display unit for the metric's data.
*Required*: No
*Type*: String
*Allowed values*: `INTEGER | DOUBLE | PERCENT | SECONDS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-metric-return-values"></a>

### Ref
<a name="aws-resource-connect-metric-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-metric-return-values-fn--getatt"></a>

####
<a name="aws-resource-connect-metric-return-values-fn--getatt-fn--getatt"></a>

`Category`  <a name="Category-fn::getatt"></a>
The category of the metric.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The timestamp of when the metric was created.

`CreationMethod`  <a name="CreationMethod-fn::getatt"></a>
The method used to create the metric. Valid values: `SERVICE_LEVEL_BUILDER` (created with the guided service-level experience) \| `METRIC_BUILDER` (created with the free-form metric builder).

`EffectiveTime`  <a name="EffectiveTime-fn::getatt"></a>
The earliest time that can be queried for this metric.

`Filters`  <a name="Filters-fn::getatt"></a>
The filters applied to the metric.

`Groupings`  <a name="Groupings-fn::getatt"></a>
The groupings available for this metric.

`LastModifiedRegion`  <a name="LastModifiedRegion-fn::getatt"></a>
The region where the metric was last modified.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The timestamp of when the metric was last modified.

`MetricArn`  <a name="MetricArn-fn::getatt"></a>
Property description not available.

`PrimaryEventSource`  <a name="PrimaryEventSource-fn::getatt"></a>
The primary event source for the metric data.

`PrimaryEventSourceEffectiveTimestampType`  <a name="PrimaryEventSourceEffectiveTimestampType-fn::getatt"></a>
The timestamp type that determines where the metric appears on a time series.

`RefreshRate`  <a name="RefreshRate-fn::getatt"></a>
The minimum interval, in seconds, between data refreshes for this metric.

`SupportedStats`  <a name="SupportedStats-fn::getatt"></a>
The stat aggregations available for this metric.

`SupportsCustomCalculation`  <a name="SupportsCustomCalculation-fn::getatt"></a>
Specifies whether the metric can be used as a component of custom metrics.

`SupportsPreaggregateCalculation`  <a name="SupportsPreaggregateCalculation-fn::getatt"></a>
Specifies whether the metric can be used inside aggregating statistical functions (SUM, AVG, etc.) in custom metric calculations.

`Type`  <a name="Type-fn::getatt"></a>
The type of the metric. Valid values: `AWS_MANAGED` \| `CUSTOMER_MANAGED`.
