---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-slimetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective SliMetric
<a name="aws-properties-applicationsignals-servicelevelobjective-slimetric"></a>

Use this structure to specify the metric to be used for the SLO.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-slimetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-slimetric-syntax.json"></a>

```
{
  "[CompositeSliConfig](#cfn-applicationsignals-servicelevelobjective-slimetric-compositesliconfig)" : {{CompositeSliConfig}},
  "[DependencyConfig](#cfn-applicationsignals-servicelevelobjective-slimetric-dependencyconfig)" : {{DependencyConfig}},
  "[KeyAttributes](#cfn-applicationsignals-servicelevelobjective-slimetric-keyattributes)" : {{String}},
  "[MetricDataQueries](#cfn-applicationsignals-servicelevelobjective-slimetric-metricdataqueries)" : {{[ MetricDataQuery, ... ]}},
  "[MetricName](#cfn-applicationsignals-servicelevelobjective-slimetric-metricname)" : {{String}},
  "[MetricSource](#cfn-applicationsignals-servicelevelobjective-slimetric-metricsource)" : {{MetricSource}},
  "[MetricType](#cfn-applicationsignals-servicelevelobjective-slimetric-metrictype)" : {{String}},
  "[OperationName](#cfn-applicationsignals-servicelevelobjective-slimetric-operationname)" : {{String}},
  "[PeriodSeconds](#cfn-applicationsignals-servicelevelobjective-slimetric-periodseconds)" : {{Integer}},
  "[Statistic](#cfn-applicationsignals-servicelevelobjective-slimetric-statistic)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-slimetric-syntax.yaml"></a>

```
  [CompositeSliConfig](#cfn-applicationsignals-servicelevelobjective-slimetric-compositesliconfig): {{
    CompositeSliConfig}}
  [DependencyConfig](#cfn-applicationsignals-servicelevelobjective-slimetric-dependencyconfig): {{
    DependencyConfig}}
  [KeyAttributes](#cfn-applicationsignals-servicelevelobjective-slimetric-keyattributes): {{String}}
  [MetricDataQueries](#cfn-applicationsignals-servicelevelobjective-slimetric-metricdataqueries): {{
    - MetricDataQuery}}
  [MetricName](#cfn-applicationsignals-servicelevelobjective-slimetric-metricname): {{String}}
  [MetricSource](#cfn-applicationsignals-servicelevelobjective-slimetric-metricsource): {{
    MetricSource}}
  [MetricType](#cfn-applicationsignals-servicelevelobjective-slimetric-metrictype): {{String}}
  [OperationName](#cfn-applicationsignals-servicelevelobjective-slimetric-operationname): {{String}}
  [PeriodSeconds](#cfn-applicationsignals-servicelevelobjective-slimetric-periodseconds): {{Integer}}
  [Statistic](#cfn-applicationsignals-servicelevelobjective-slimetric-statistic): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-slimetric-properties"></a>

`CompositeSliConfig`  <a name="cfn-applicationsignals-servicelevelobjective-slimetric-compositesliconfig"></a>
Property description not available.
*Required*: No
*Type*: [CompositeSliConfig](aws-properties-applicationsignals-servicelevelobjective-compositesliconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DependencyConfig`  <a name="cfn-applicationsignals-servicelevelobjective-slimetric-dependencyconfig"></a>
Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName`.
*Required*: No
*Type*: [DependencyConfig](aws-properties-applicationsignals-servicelevelobjective-dependencyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyAttributes`  <a name="cfn-applicationsignals-servicelevelobjective-slimetric-keyattributes"></a>
If this SLO is related to a metric collected by Application Signals, you must use this field to specify which service the SLO metric is related to. To do so, you must specify at least the `Type`, `Name`, and `Environment` attributes.
This is a string-to-string map. It can include the following fields.
+ `Type` designates the type of object this is.
+ `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource`.
+ `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service`, `RemoteService`, or `AWS::Service`.
+ `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource`.
+ `Environment` specifies the location where this object is hosted, or what it belongs to.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricDataQueries`  <a name="cfn-applicationsignals-servicelevelobjective-slimetric-metricdataqueries"></a>
If this SLO monitors a CloudWatch metric or the result of a CloudWatch metric math expression, use this structure to specify that metric or expression.
*Required*: No
*Type*: Array of [MetricDataQuery](aws-properties-applicationsignals-servicelevelobjective-metricdataquery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-applicationsignals-servicelevelobjective-slimetric-metricname"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricSource`  <a name="cfn-applicationsignals-servicelevelobjective-slimetric-metricsource"></a>
Property description not available.
*Required*: No
*Type*: [MetricSource](aws-properties-applicationsignals-servicelevelobjective-metricsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricType`  <a name="cfn-applicationsignals-servicelevelobjective-slimetric-metrictype"></a>
If the SLO is to monitor either the `LATENCY` or `AVAILABILITY` metric that Application Signals collects, use this field to specify which of those metrics is used.
*Required*: No
*Type*: String
*Allowed values*: `LATENCY | AVAILABILITY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperationName`  <a name="cfn-applicationsignals-servicelevelobjective-slimetric-operationname"></a>
If the SLO is to monitor a specific operation of the service, use this field to specify the name of that operation.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeriodSeconds`  <a name="cfn-applicationsignals-servicelevelobjective-slimetric-periodseconds"></a>
The number of seconds to use as the period for SLO evaluation. Your application's performance is compared to the SLI during each period. For each period, the application is determined to have either achieved or not achieved the necessary performance.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Statistic`  <a name="cfn-applicationsignals-servicelevelobjective-slimetric-statistic"></a>
The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
