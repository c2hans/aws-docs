---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-anomalydetector-missingdataaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::AnomalyDetector MissingDataAction
<a name="aws-properties-aps-anomalydetector-missingdataaction"></a>

Specifies the action to take when data is missing during anomaly detection evaluation.

## Syntax
<a name="aws-properties-aps-anomalydetector-missingdataaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-anomalydetector-missingdataaction-syntax.json"></a>

```
{
  "[MarkAsAnomaly](#cfn-aps-anomalydetector-missingdataaction-markasanomaly)" : {{Boolean}},
  "[Skip](#cfn-aps-anomalydetector-missingdataaction-skip)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-aps-anomalydetector-missingdataaction-syntax.yaml"></a>

```
  [MarkAsAnomaly](#cfn-aps-anomalydetector-missingdataaction-markasanomaly): {{Boolean}}
  [Skip](#cfn-aps-anomalydetector-missingdataaction-skip): {{Boolean}}
```

## Properties
<a name="aws-properties-aps-anomalydetector-missingdataaction-properties"></a>

`MarkAsAnomaly`  <a name="cfn-aps-anomalydetector-missingdataaction-markasanomaly"></a>
Marks missing data points as anomalies.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Skip`  <a name="cfn-aps-anomalydetector-missingdataaction-skip"></a>
Skips evaluation when data is missing.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
