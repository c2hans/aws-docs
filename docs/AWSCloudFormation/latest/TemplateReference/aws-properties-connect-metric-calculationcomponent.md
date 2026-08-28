---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-metric-calculationcomponent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Metric CalculationComponent
<a name="aws-properties-connect-metric-calculationcomponent"></a>

Represents a component metric referenced in a custom metric calculation formula.

## Syntax
<a name="aws-properties-connect-metric-calculationcomponent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-metric-calculationcomponent-syntax.json"></a>

```
{
  "[Alias](#cfn-connect-metric-calculationcomponent-alias)" : {{String}},
  "[MetricFilters](#cfn-connect-metric-calculationcomponent-metricfilters)" : {{[ MetricFilter, ... ]}},
  "[MetricId](#cfn-connect-metric-calculationcomponent-metricid)" : {{String}},
  "[MetricName](#cfn-connect-metric-calculationcomponent-metricname)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-metric-calculationcomponent-syntax.yaml"></a>

```
  [Alias](#cfn-connect-metric-calculationcomponent-alias): {{String}}
  [MetricFilters](#cfn-connect-metric-calculationcomponent-metricfilters): {{
    - MetricFilter}}
  [MetricId](#cfn-connect-metric-calculationcomponent-metricid): {{String}}
  [MetricName](#cfn-connect-metric-calculationcomponent-metricname): {{String}}
```

## Properties
<a name="aws-properties-connect-metric-calculationcomponent-properties"></a>

`Alias`  <a name="cfn-connect-metric-calculationcomponent-alias"></a>
The alias used to reference this component in the calculation expression.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z_][a-zA-Z0-9_]*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricFilters`  <a name="cfn-connect-metric-calculationcomponent-metricfilters"></a>
The filters applied to the calculation component.
*Required*: No
*Type*: Array of [MetricFilter](aws-properties-connect-metric-metricfilter.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricId`  <a name="cfn-connect-metric-calculationcomponent-metricid"></a>
The ARN of an AWS-managed metric used in this calculation component. Mutually exclusive with `MetricName`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-connect-metric-calculationcomponent-metricname"></a>
The name of an AWS-managed metric used in this calculation component (for example, `CONTACTS_HANDLED`). Mutually exclusive with `MetricId`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
