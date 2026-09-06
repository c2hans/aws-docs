---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-requestbasedslimetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective RequestBasedSliMetric
<a name="aws-properties-applicationsignals-servicelevelobjective-requestbasedslimetric"></a>

This structure contains the information about the metric that is used for a request-based SLO.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-requestbasedslimetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-requestbasedslimetric-syntax.json"></a>

```
{
  "[CompositeSliConfig](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-compositesliconfig)" : {{CompositeSliConfig}},
  "[DependencyConfig](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-dependencyconfig)" : {{DependencyConfig}},
  "[KeyAttributes](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-keyattributes)" : {{String}},
  "[MetricName](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-metricname)" : {{String}},
  "[MetricSource](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-metricsource)" : {{MetricSource}},
  "[MetricType](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-metrictype)" : {{String}},
  "[MonitoredRequestCountMetric](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-monitoredrequestcountmetric)" : {{MonitoredRequestCountMetric}},
  "[OperationName](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-operationname)" : {{String}},
  "[TotalRequestCountMetric](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-totalrequestcountmetric)" : {{[ MetricDataQuery, ... ]}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-requestbasedslimetric-syntax.yaml"></a>

```
  [CompositeSliConfig](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-compositesliconfig): {{
    CompositeSliConfig}}
  [DependencyConfig](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-dependencyconfig): {{
    DependencyConfig}}
  [KeyAttributes](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-keyattributes): {{String}}
  [MetricName](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-metricname): {{String}}
  [MetricSource](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-metricsource): {{
    MetricSource}}
  [MetricType](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-metrictype): {{String}}
  [MonitoredRequestCountMetric](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-monitoredrequestcountmetric): {{
    MonitoredRequestCountMetric}}
  [OperationName](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-operationname): {{String}}
  [TotalRequestCountMetric](#cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-totalrequestcountmetric): {{
    - MetricDataQuery}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-requestbasedslimetric-properties"></a>

`CompositeSliConfig`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-compositesliconfig"></a>
Property description not available.
*Required*: No
*Type*: [CompositeSliConfig](aws-properties-applicationsignals-servicelevelobjective-compositesliconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DependencyConfig`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-dependencyconfig"></a>
Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName`.
*Required*: No
*Type*: [DependencyConfig](aws-properties-applicationsignals-servicelevelobjective-dependencyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyAttributes`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-keyattributes"></a>
This is a string-to-string map that contains information about the type of object that this SLO is related to. It can include the following fields.
+ `Type` designates the type of object that this SLO is related to.
+ `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource`.
+ `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service`, `RemoteService`, or `AWS::Service`.
+ `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource`.
+ `Environment` specifies the location where this object is hosted, or what it belongs to.
+ `AwsAccountId` allows you to create an SLO for an object that exists in another account.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-metricname"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricSource`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-metricsource"></a>
Property description not available.
*Required*: No
*Type*: [MetricSource](aws-properties-applicationsignals-servicelevelobjective-metricsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricType`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-metrictype"></a>
If the SLO monitors either the `LATENCY` or `AVAILABILITY` metric that Application Signals collects, this field displays which of those metrics is used.
*Required*: No
*Type*: String
*Allowed values*: `LATENCY | AVAILABILITY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MonitoredRequestCountMetric`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-monitoredrequestcountmetric"></a>
Use this structure to define the metric that you want to use as the "good request" or "bad request" value for a request-based SLO. This value observed for the metric defined in `TotalRequestCountMetric` will be divided by the number found for `MonitoredRequestCountMetric` to determine the percentage of successful requests that this SLO tracks.
*Required*: No
*Type*: [MonitoredRequestCountMetric](aws-properties-applicationsignals-servicelevelobjective-monitoredrequestcountmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperationName`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-operationname"></a>
If the SLO monitors a specific operation of the service, this field displays that operation name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalRequestCountMetric`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedslimetric-totalrequestcountmetric"></a>
This structure defines the metric that is used as the "total requests" number for a request-based SLO. The number observed for this metric is divided by the number of "good requests" or "bad requests" that is observed for the metric defined in `MonitoredRequestCountMetric`.
*Required*: No
*Type*: Array of [MetricDataQuery](aws-properties-applicationsignals-servicelevelobjective-metricdataquery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
