---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-anomalydetector-label.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::AnomalyDetector Label
<a name="aws-properties-aps-anomalydetector-label"></a>

The Amazon Managed Service for Prometheus metric labels associated with the anomaly detector.

## Syntax
<a name="aws-properties-aps-anomalydetector-label-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-anomalydetector-label-syntax.json"></a>

```
{
  "[Key](#cfn-aps-anomalydetector-label-key)" : {{String}},
  "[Value](#cfn-aps-anomalydetector-label-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-aps-anomalydetector-label-syntax.yaml"></a>

```
  [Key](#cfn-aps-anomalydetector-label-key): {{String}}
  [Value](#cfn-aps-anomalydetector-label-value): {{String}}
```

## Properties
<a name="aws-properties-aps-anomalydetector-label-properties"></a>

`Key`  <a name="cfn-aps-anomalydetector-label-key"></a>
The key of the label.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-aps-anomalydetector-label-value"></a>
The value for this label.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
