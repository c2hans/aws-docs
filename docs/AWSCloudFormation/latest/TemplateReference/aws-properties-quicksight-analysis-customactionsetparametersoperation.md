---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-customactionsetparametersoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis CustomActionSetParametersOperation
<a name="aws-properties-quicksight-analysis-customactionsetparametersoperation"></a>

The set parameter operation that sets parameters in custom action.

## Syntax
<a name="aws-properties-quicksight-analysis-customactionsetparametersoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-customactionsetparametersoperation-syntax.json"></a>

```
{
  "[ParameterValueConfigurations](#cfn-quicksight-analysis-customactionsetparametersoperation-parametervalueconfigurations)" : {{[ SetParameterValueConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-customactionsetparametersoperation-syntax.yaml"></a>

```
  [ParameterValueConfigurations](#cfn-quicksight-analysis-customactionsetparametersoperation-parametervalueconfigurations): {{
    - SetParameterValueConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-customactionsetparametersoperation-properties"></a>

`ParameterValueConfigurations`  <a name="cfn-quicksight-analysis-customactionsetparametersoperation-parametervalueconfigurations"></a>
The parameter that determines the value configuration.
*Required*: Yes
*Type*: Array of [SetParameterValueConfiguration](aws-properties-quicksight-analysis-setparametervalueconfiguration.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
