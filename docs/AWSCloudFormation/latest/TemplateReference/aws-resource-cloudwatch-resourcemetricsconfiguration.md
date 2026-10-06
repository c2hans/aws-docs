---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-resourcemetricsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::ResourceMetricsConfiguration
<a name="aws-resource-cloudwatch-resourcemetricsconfiguration"></a>

Turns on CloudWatch detailed monitoring for an individual AWS resource. Also defines which detailed metrics CloudWatch collects for it. Detailed monitoring provides higher-resolution OpenTelemetry metrics for supported resources.

Each resource can have at most one `ResourceMetricsConfiguration`. The resource is identified by its Amazon Resource Name (ARN), and the ARN also serves as the identifier for this CloudFormation resource. Creating the resource turns on detailed monitoring. Deleting the resource turns detailed monitoring off, but it does not delete metric data that CloudWatch already collected.

For the list of resource types that support detailed monitoring, see [Supported resources for CloudWatch detailed monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/resource-metrics-configuration-supported.html) in the *Amazon CloudWatch User Guide*.

## Syntax
<a name="aws-resource-cloudwatch-resourcemetricsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-resourcemetricsconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::ResourceMetricsConfiguration",
  "Properties" : {
      "[MetricSelections](#cfn-cloudwatch-resourcemetricsconfiguration-metricselections)" : {{[ ResourceMetricSelection, ... ]}},
      "[ResourceArn](#cfn-cloudwatch-resourcemetricsconfiguration-resourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-resourcemetricsconfiguration-syntax.yaml"></a>

```
Type: AWS::CloudWatch::ResourceMetricsConfiguration
Properties:
  [MetricSelections](#cfn-cloudwatch-resourcemetricsconfiguration-metricselections): {{
    - ResourceMetricSelection}}
  [ResourceArn](#cfn-cloudwatch-resourcemetricsconfiguration-resourcearn): {{String}}
```

## Properties
<a name="aws-resource-cloudwatch-resourcemetricsconfiguration-properties"></a>

`MetricSelections`  <a name="cfn-cloudwatch-resourcemetricsconfiguration-metricselections"></a>
Specifies which metrics Amazon CloudWatch collects for the resource. If you omit this parameter, Amazon CloudWatch collects all available detailed metrics for the resource.
*Required*: No
*Type*: Array of [ResourceMetricSelection](aws-properties-cloudwatch-resourcemetricsconfiguration-resourcemetricselection.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-cloudwatch-resourcemetricsconfiguration-resourcearn"></a>
The Amazon Resource Name (ARN) of the AWS resource to enable detailed monitoring for.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudwatch-resourcemetricsconfiguration-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-resourcemetricsconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the monitored resource.

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-resourcemetricsconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-resourcemetricsconfiguration-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that detailed monitoring was turned on for the resource.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time that the configuration was last changed.
