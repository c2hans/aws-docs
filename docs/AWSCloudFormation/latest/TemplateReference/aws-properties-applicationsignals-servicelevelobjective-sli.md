---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-sli.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective Sli
<a name="aws-properties-applicationsignals-servicelevelobjective-sli"></a>

This structure specifies the information about the service and the performance metric that an SLO is to monitor.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-sli-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-sli-syntax.json"></a>

```
{
  "[ComparisonOperator](#cfn-applicationsignals-servicelevelobjective-sli-comparisonoperator)" : {{String}},
  "[MetricThreshold](#cfn-applicationsignals-servicelevelobjective-sli-metricthreshold)" : {{Number}},
  "[SliMetric](#cfn-applicationsignals-servicelevelobjective-sli-slimetric)" : {{SliMetric}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-sli-syntax.yaml"></a>

```
  [ComparisonOperator](#cfn-applicationsignals-servicelevelobjective-sli-comparisonoperator): {{String}}
  [MetricThreshold](#cfn-applicationsignals-servicelevelobjective-sli-metricthreshold): {{Number}}
  [SliMetric](#cfn-applicationsignals-servicelevelobjective-sli-slimetric): {{
    SliMetric}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-sli-properties"></a>

`ComparisonOperator`  <a name="cfn-applicationsignals-servicelevelobjective-sli-comparisonoperator"></a>
The arithmetic operation to use when comparing the specified metric to the threshold.
*Required*: Yes
*Type*: String
*Allowed values*: `GreaterThanOrEqualTo | LessThanOrEqualTo | LessThan | GreaterThan`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricThreshold`  <a name="cfn-applicationsignals-servicelevelobjective-sli-metricthreshold"></a>
The value that the SLI metric is compared to.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SliMetric`  <a name="cfn-applicationsignals-servicelevelobjective-sli-slimetric"></a>
Use this structure to specify the metric to be used for the SLO.
*Required*: Yes
*Type*: [SliMetric](aws-properties-applicationsignals-servicelevelobjective-slimetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
