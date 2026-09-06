---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-anomalydetector-anomalydetectorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::AnomalyDetector AnomalyDetectorConfiguration
<a name="aws-properties-aps-anomalydetector-anomalydetectorconfiguration"></a>

The configuration for the anomaly detection algorithm.

## Syntax
<a name="aws-properties-aps-anomalydetector-anomalydetectorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-anomalydetector-anomalydetectorconfiguration-syntax.json"></a>

```
{
  "[RandomCutForest](#cfn-aps-anomalydetector-anomalydetectorconfiguration-randomcutforest)" : {{RandomCutForestConfiguration}}
}
```

### YAML
<a name="aws-properties-aps-anomalydetector-anomalydetectorconfiguration-syntax.yaml"></a>

```
  [RandomCutForest](#cfn-aps-anomalydetector-anomalydetectorconfiguration-randomcutforest): {{
    RandomCutForestConfiguration}}
```

## Properties
<a name="aws-properties-aps-anomalydetector-anomalydetectorconfiguration-properties"></a>

`RandomCutForest`  <a name="cfn-aps-anomalydetector-anomalydetectorconfiguration-randomcutforest"></a>
The Random Cut Forest algorithm configuration for anomaly detection.
*Required*: Yes
*Type*: [RandomCutForestConfiguration](aws-properties-aps-anomalydetector-randomcutforestconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
