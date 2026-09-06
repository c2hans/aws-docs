---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-metricfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::MetricFilter
<a name="aws-resource-logs-metricfilter"></a>

The `AWS::Logs::MetricFilter` resource specifies a metric filter that describes how CloudWatch Logs extracts information from logs and transforms it into Amazon CloudWatch metrics. If you have multiple metric filters that are associated with a log group, all the filters are applied to the log streams in that group.

The maximum number of metric filters that can be associated with a log group is 100.

## Syntax
<a name="aws-resource-logs-metricfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-metricfilter-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::MetricFilter",
  "Properties" : {
      "[ApplyOnTransformedLogs](#cfn-logs-metricfilter-applyontransformedlogs)" : {{Boolean}},
      "[EmitSystemFieldDimensions](#cfn-logs-metricfilter-emitsystemfielddimensions)" : {{[ String, ... ]}},
      "[FieldSelectionCriteria](#cfn-logs-metricfilter-fieldselectioncriteria)" : {{String}},
      "[FilterName](#cfn-logs-metricfilter-filtername)" : {{String}},
      "[FilterPattern](#cfn-logs-metricfilter-filterpattern)" : {{String}},
      "[LogGroupName](#cfn-logs-metricfilter-loggroupname)" : {{String}},
      "[MetricTransformations](#cfn-logs-metricfilter-metrictransformations)" : {{[ MetricTransformation, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-logs-metricfilter-syntax.yaml"></a>

```
Type: AWS::Logs::MetricFilter
Properties:
  [ApplyOnTransformedLogs](#cfn-logs-metricfilter-applyontransformedlogs): {{Boolean}}
  [EmitSystemFieldDimensions](#cfn-logs-metricfilter-emitsystemfielddimensions): {{
    - String}}
  [FieldSelectionCriteria](#cfn-logs-metricfilter-fieldselectioncriteria): {{String}}
  [FilterName](#cfn-logs-metricfilter-filtername): {{String}}
  [FilterPattern](#cfn-logs-metricfilter-filterpattern): {{String}}
  [LogGroupName](#cfn-logs-metricfilter-loggroupname): {{String}}
  [MetricTransformations](#cfn-logs-metricfilter-metrictransformations): {{
    - MetricTransformation}}
```

## Properties
<a name="aws-resource-logs-metricfilter-properties"></a>

`ApplyOnTransformedLogs`  <a name="cfn-logs-metricfilter-applyontransformedlogs"></a>
This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see [PutTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html).
If this value is `true`, the metric filter is applied on the transformed version of the log events instead of the original ingested log events.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmitSystemFieldDimensions`  <a name="cfn-logs-metricfilter-emitsystemfielddimensions"></a>
The list of system fields that are emitted as additional dimensions in the generated metrics. Returns the `emitSystemFieldDimensions` value if it was specified when the metric filter was created.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldSelectionCriteria`  <a name="cfn-logs-metricfilter-fieldselectioncriteria"></a>
The filter expression that specifies which log events are processed by this metric filter based on system fields. Returns the `fieldSelectionCriteria` value if it was specified when the metric filter was created.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterName`  <a name="cfn-logs-metricfilter-filtername"></a>
The name of the metric filter.
*Required*: No
*Type*: String
*Pattern*: `^[^:*]{1,512}`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterPattern`  <a name="cfn-logs-metricfilter-filterpattern"></a>
A filter pattern for extracting metric data out of ingested log events. For more information, see [Filter and Pattern Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).
*Required*: Yes
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupName`  <a name="cfn-logs-metricfilter-loggroupname"></a>
The name of an existing log group that you want to associate with this metric filter.
*Required*: Yes
*Type*: String
*Pattern*: `^[.\-_/#A-Za-z0-9]{1,512}`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricTransformations`  <a name="cfn-logs-metricfilter-metrictransformations"></a>
The metric transformations.
*Required*: Yes
*Type*: Array of [MetricTransformation](aws-properties-logs-metricfilter-metrictransformation.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-resource-logs-metricfilter--examples"></a>

### Create a Metric Filter
<a name="aws-resource-logs-metricfilter--examples--Create_a_Metric_Filter"></a>

The following example sends a value of `1` to the `404Count` metric whenever the status code field includes a `404` value.

#### JSON
<a name="aws-resource-logs-metricfilter--examples--Create_a_Metric_Filter--json"></a>

```
"404MetricFilter": {
    "Type": "AWS::Logs::MetricFilter",
    "Properties": {
        "LogGroupName": { "Ref": "myLogGroup" },
        "FilterPattern": "[ip, identity, user_id, timestamp, request, status_code = 404, size]",
        "MetricTransformations": [
            {
                "MetricValue": "1",
                "MetricNamespace": "WebServer/404s",
                "MetricName": "404Count"
            }
        ]
    }
}
```

#### YAML
<a name="aws-resource-logs-metricfilter--examples--Create_a_Metric_Filter--yaml"></a>

```
404MetricFilter:
  Type: AWS::Logs::MetricFilter
  Properties:
    LogGroupName:
      Ref: "myLogGroup"
    FilterPattern: "[ip, identity, user_id, timestamp, request, status_code = 404, size]"
    MetricTransformations:
      -
        MetricValue: "1"
        MetricNamespace: "WebServer/404s"
        MetricName: "404Count"
```
