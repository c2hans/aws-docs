---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dsql-cluster-metricgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DSQL::Cluster MetricGroup
<a name="aws-properties-dsql-cluster-metricgroup"></a>

The name of an advanced monitoring metric group. Advanced monitoring collects detailed database metrics and logs to help you analyze and resolve performance issues. You choose which metric groups to collect for each cluster.

The following metric groups are available:

STATEMENT\_STATISTICS
Shows which SQL statements run most often or take the most time. Collects execution count, execution time, and rows for each statement.

## Syntax
<a name="aws-properties-dsql-cluster-metricgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dsql-cluster-metricgroup-syntax.json"></a>

```
{
  "[MetricGroup](#cfn-dsql-cluster-metricgroup-metricgroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-dsql-cluster-metricgroup-syntax.yaml"></a>

```
  [MetricGroup](#cfn-dsql-cluster-metricgroup-metricgroup): {{String}}
```

## Properties
<a name="aws-properties-dsql-cluster-metricgroup-properties"></a>

`MetricGroup`  <a name="cfn-dsql-cluster-metricgroup-metricgroup"></a>
Property description not available.
*Required*: Yes
*Type*: [String](#aws-properties-dsql-cluster-metricgroup)
*Allowed values*: `STATEMENT_STATISTICS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
