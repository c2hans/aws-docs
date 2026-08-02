---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-computationmodel-computationmodelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::ComputationModel ComputationModelConfiguration
<a name="aws-properties-iotsitewise-computationmodel-computationmodelconfiguration"></a>

The configuration for the computation model.

## Syntax
<a name="aws-properties-iotsitewise-computationmodel-computationmodelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-computationmodel-computationmodelconfiguration-syntax.json"></a>

```
{
  "[AnomalyDetection](#cfn-iotsitewise-computationmodel-computationmodelconfiguration-anomalydetection)" : {{AnomalyDetectionComputationModelConfiguration}}
}
```

### YAML
<a name="aws-properties-iotsitewise-computationmodel-computationmodelconfiguration-syntax.yaml"></a>

```
  [AnomalyDetection](#cfn-iotsitewise-computationmodel-computationmodelconfiguration-anomalydetection): {{
    AnomalyDetectionComputationModelConfiguration}}
```

## Properties
<a name="aws-properties-iotsitewise-computationmodel-computationmodelconfiguration-properties"></a>

`AnomalyDetection`  <a name="cfn-iotsitewise-computationmodel-computationmodelconfiguration-anomalydetection"></a>
The configuration for the anomaly detection type of computation model.
*Required*: No
*Type*: [AnomalyDetectionComputationModelConfiguration](aws-properties-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
