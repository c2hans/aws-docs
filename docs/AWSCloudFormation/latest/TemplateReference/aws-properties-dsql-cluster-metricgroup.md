---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dsql-cluster-metricgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DSQL::Cluster MetricGroup

An advanced monitoring metric group to enable on the cluster.

## Syntax
<a name="aws-properties-dsql-cluster-metricgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dsql-cluster-metricgroup-syntax.json"></a>

```json
{
  "[MetricGroup](#cfn-dsql-cluster-metricgroup-metricgroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-dsql-cluster-metricgroup-syntax.yaml"></a>

```yaml
  [MetricGroup](#cfn-dsql-cluster-metricgroup-metricgroup): {{String}}
```

## Properties
<a name="aws-properties-dsql-cluster-metricgroup-properties"></a>

`MetricGroup`  <a name="cfn-dsql-cluster-metricgroup-metricgroup"></a>
The name of the metric group.
*Required*: Yes
*Type*: [String](aws-properties-dsql-cluster-metricgroup.md)
*Allowed values*: `STATEMENT_STATISTICS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
