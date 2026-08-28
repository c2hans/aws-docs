---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-customactionsetparametersoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard CustomActionSetParametersOperation
<a name="aws-properties-quicksight-dashboard-customactionsetparametersoperation"></a>

The set parameter operation that sets parameters in custom action.

## Syntax
<a name="aws-properties-quicksight-dashboard-customactionsetparametersoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-customactionsetparametersoperation-syntax.json"></a>

```
{
  "[ParameterValueConfigurations](#cfn-quicksight-dashboard-customactionsetparametersoperation-parametervalueconfigurations)" : {{[ SetParameterValueConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-customactionsetparametersoperation-syntax.yaml"></a>

```
  [ParameterValueConfigurations](#cfn-quicksight-dashboard-customactionsetparametersoperation-parametervalueconfigurations): {{
    - SetParameterValueConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-customactionsetparametersoperation-properties"></a>

`ParameterValueConfigurations`  <a name="cfn-quicksight-dashboard-customactionsetparametersoperation-parametervalueconfigurations"></a>
The parameter that determines the value configuration.
*Required*: Yes
*Type*: Array of [SetParameterValueConfiguration](aws-properties-quicksight-dashboard-setparametervalueconfiguration.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
