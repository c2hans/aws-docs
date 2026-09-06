---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-setparametervalueconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SetParameterValueConfiguration
<a name="aws-properties-quicksight-dashboard-setparametervalueconfiguration"></a>

The configuration of adding parameters in action.

## Syntax
<a name="aws-properties-quicksight-dashboard-setparametervalueconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-setparametervalueconfiguration-syntax.json"></a>

```
{
  "[DestinationParameterName](#cfn-quicksight-dashboard-setparametervalueconfiguration-destinationparametername)" : {{String}},
  "[Value](#cfn-quicksight-dashboard-setparametervalueconfiguration-value)" : {{DestinationParameterValueConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-setparametervalueconfiguration-syntax.yaml"></a>

```
  [DestinationParameterName](#cfn-quicksight-dashboard-setparametervalueconfiguration-destinationparametername): {{String}}
  [Value](#cfn-quicksight-dashboard-setparametervalueconfiguration-value): {{
    DestinationParameterValueConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-setparametervalueconfiguration-properties"></a>

`DestinationParameterName`  <a name="cfn-quicksight-dashboard-setparametervalueconfiguration-destinationparametername"></a>
The destination parameter name of the `SetParameterValueConfiguration`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-dashboard-setparametervalueconfiguration-value"></a>
Property description not available.
*Required*: Yes
*Type*: [DestinationParameterValueConfiguration](aws-properties-quicksight-dashboard-destinationparametervalueconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
