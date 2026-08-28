---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-metricscollection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup MetricsCollection
<a name="aws-properties-autoscaling-autoscalinggroup-metricscollection"></a>

`MetricsCollection` is a property of the [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html) resource that describes the group metrics that an Amazon EC2 Auto Scaling group sends to Amazon CloudWatch. These metrics describe the group rather than any of its instances.

For more information, see [Monitor CloudWatch metrics for your Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html) in the *Amazon EC2 Auto Scaling User Guide*. You can find a sample template snippet in the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#aws-resource-autoscaling-autoscalinggroup--examples) section of the `AWS::AutoScaling::AutoScalingGroup` resource.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-metricscollection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-metricscollection-syntax.json"></a>

```
{
  "[Granularity](#cfn-autoscaling-autoscalinggroup-metricscollection-granularity)" : {{String}},
  "[Metrics](#cfn-autoscaling-autoscalinggroup-metricscollection-metrics)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-metricscollection-syntax.yaml"></a>

```
  [Granularity](#cfn-autoscaling-autoscalinggroup-metricscollection-granularity): {{String}}
  [Metrics](#cfn-autoscaling-autoscalinggroup-metricscollection-metrics): {{
    - String}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-metricscollection-properties"></a>

`Granularity`  <a name="cfn-autoscaling-autoscalinggroup-metricscollection-granularity"></a>
The frequency at which Amazon EC2 Auto Scaling sends aggregated data to CloudWatch. The only valid value is `1Minute`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metrics`  <a name="cfn-autoscaling-autoscalinggroup-metricscollection-metrics"></a>
Identifies the metrics to enable.
You can specify one or more of the following metrics:
+  `GroupMinSize`
+  `GroupMaxSize`
+  `GroupDesiredCapacity`
+  `GroupInServiceInstances`
+  `GroupPendingInstances`
+  `GroupStandbyInstances`
+  `GroupTerminatingInstances`
+  `GroupTotalInstances`
+  `GroupInServiceCapacity`
+  `GroupPendingCapacity`
+  `GroupStandbyCapacity`
+  `GroupTerminatingCapacity`
+  `GroupTotalCapacity`
+  `WarmPoolDesiredCapacity`
+  `WarmPoolWarmedCapacity`
+  `WarmPoolPendingCapacity`
+  `WarmPoolTerminatingCapacity`
+  `WarmPoolTotalCapacity`
+  `GroupAndWarmPoolDesiredCapacity`
+  `GroupAndWarmPoolTotalCapacity`
If you specify `Granularity` and don't specify any metrics, all metrics are enabled.
For more information, see [Amazon CloudWatch metrics for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-metrics.html) in the *Amazon EC2 Auto Scaling User Guide*.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
