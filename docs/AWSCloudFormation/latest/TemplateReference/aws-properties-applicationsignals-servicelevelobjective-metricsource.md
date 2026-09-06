---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-metricsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective MetricSource
<a name="aws-properties-applicationsignals-servicelevelobjective-metricsource"></a>

Identifies the metric source for SLOs on resources other than Application Signals services.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-metricsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-metricsource-syntax.json"></a>

```
{
  "[MetricSourceAttributes](#cfn-applicationsignals-servicelevelobjective-metricsource-metricsourceattributes)" : {{String}},
  "[MetricSourceKeyAttributes](#cfn-applicationsignals-servicelevelobjective-metricsource-metricsourcekeyattributes)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-metricsource-syntax.yaml"></a>

```
  [MetricSourceAttributes](#cfn-applicationsignals-servicelevelobjective-metricsource-metricsourceattributes): {{String}}
  [MetricSourceKeyAttributes](#cfn-applicationsignals-servicelevelobjective-metricsource-metricsourcekeyattributes): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-metricsource-properties"></a>

`MetricSourceAttributes`  <a name="cfn-applicationsignals-servicelevelobjective-metricsource-metricsourceattributes"></a>
Additional attributes for the metric source.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricSourceKeyAttributes`  <a name="cfn-applicationsignals-servicelevelobjective-metricsource-metricsourcekeyattributes"></a>
Key attributes that identify the metric source.
*Required*: Yes
*Type*: String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
