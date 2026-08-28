---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-requestbasedsli.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective RequestBasedSli
<a name="aws-properties-applicationsignals-servicelevelobjective-requestbasedsli"></a>

This structure contains information about the performance metric that a request-based SLO monitors.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-requestbasedsli-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-requestbasedsli-syntax.json"></a>

```
{
  "[ComparisonOperator](#cfn-applicationsignals-servicelevelobjective-requestbasedsli-comparisonoperator)" : {{String}},
  "[MetricThreshold](#cfn-applicationsignals-servicelevelobjective-requestbasedsli-metricthreshold)" : {{Number}},
  "[RequestBasedSliMetric](#cfn-applicationsignals-servicelevelobjective-requestbasedsli-requestbasedslimetric)" : {{RequestBasedSliMetric}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-requestbasedsli-syntax.yaml"></a>

```
  [ComparisonOperator](#cfn-applicationsignals-servicelevelobjective-requestbasedsli-comparisonoperator): {{String}}
  [MetricThreshold](#cfn-applicationsignals-servicelevelobjective-requestbasedsli-metricthreshold): {{Number}}
  [RequestBasedSliMetric](#cfn-applicationsignals-servicelevelobjective-requestbasedsli-requestbasedslimetric): {{
    RequestBasedSliMetric}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-requestbasedsli-properties"></a>

`ComparisonOperator`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedsli-comparisonoperator"></a>
The arithmetic operation used when comparing the specified metric to the threshold.
*Required*: No
*Type*: String
*Allowed values*: `GreaterThanOrEqualTo | LessThanOrEqualTo | LessThan | GreaterThan`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricThreshold`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedsli-metricthreshold"></a>
This value is the threshold that the observed metric values of the SLI metric are compared to.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequestBasedSliMetric`  <a name="cfn-applicationsignals-servicelevelobjective-requestbasedsli-requestbasedslimetric"></a>
A structure that contains information about the metric that the SLO monitors.
*Required*: Yes
*Type*: [RequestBasedSliMetric](aws-properties-applicationsignals-servicelevelobjective-requestbasedslimetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
