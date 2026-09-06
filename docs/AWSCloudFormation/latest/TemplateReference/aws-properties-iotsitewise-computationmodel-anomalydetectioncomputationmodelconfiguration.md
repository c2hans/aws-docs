---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::ComputationModel AnomalyDetectionComputationModelConfiguration
<a name="aws-properties-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration"></a>

Contains the configuration for anomaly detection computation models.

## Syntax
<a name="aws-properties-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-syntax.json"></a>

```
{
  "[InputProperties](#cfn-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-inputproperties)" : {{String}},
  "[ResultProperty](#cfn-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-resultproperty)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-syntax.yaml"></a>

```
  [InputProperties](#cfn-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-inputproperties): {{String}}
  [ResultProperty](#cfn-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-resultproperty): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-properties"></a>

`InputProperties`  <a name="cfn-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-inputproperties"></a>
The list of input properties for the anomaly detection model.
*Required*: Yes
*Type*: String
*Pattern*: `^\$\{[a-z][a-z0-9_]*\}$`
*Minimum*: `4`
*Maximum*: `67`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResultProperty`  <a name="cfn-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-resultproperty"></a>
The property where the anomaly detection results will be stored.
*Required*: Yes
*Type*: String
*Pattern*: `^\$\{[a-z][a-z0-9_]*\}$`
*Minimum*: `4`
*Maximum*: `67`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
