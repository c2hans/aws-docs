---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-imagecustomactionoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ImageCustomActionOperation
<a name="aws-properties-quicksight-dashboard-imagecustomactionoperation"></a>

The operation that is defined by the custom action.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-dashboard-imagecustomactionoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-imagecustomactionoperation-syntax.json"></a>

```
{
  "[NavigationOperation](#cfn-quicksight-dashboard-imagecustomactionoperation-navigationoperation)" : {{CustomActionNavigationOperation}},
  "[SetParametersOperation](#cfn-quicksight-dashboard-imagecustomactionoperation-setparametersoperation)" : {{CustomActionSetParametersOperation}},
  "[URLOperation](#cfn-quicksight-dashboard-imagecustomactionoperation-urloperation)" : {{CustomActionURLOperation}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-imagecustomactionoperation-syntax.yaml"></a>

```
  [NavigationOperation](#cfn-quicksight-dashboard-imagecustomactionoperation-navigationoperation): {{
    CustomActionNavigationOperation}}
  [SetParametersOperation](#cfn-quicksight-dashboard-imagecustomactionoperation-setparametersoperation): {{
    CustomActionSetParametersOperation}}
  [URLOperation](#cfn-quicksight-dashboard-imagecustomactionoperation-urloperation): {{
    CustomActionURLOperation}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-imagecustomactionoperation-properties"></a>

`NavigationOperation`  <a name="cfn-quicksight-dashboard-imagecustomactionoperation-navigationoperation"></a>
Property description not available.
*Required*: No
*Type*: [CustomActionNavigationOperation](aws-properties-quicksight-dashboard-customactionnavigationoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SetParametersOperation`  <a name="cfn-quicksight-dashboard-imagecustomactionoperation-setparametersoperation"></a>
Property description not available.
*Required*: No
*Type*: [CustomActionSetParametersOperation](aws-properties-quicksight-dashboard-customactionsetparametersoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`URLOperation`  <a name="cfn-quicksight-dashboard-imagecustomactionoperation-urloperation"></a>
Property description not available.
*Required*: No
*Type*: [CustomActionURLOperation](aws-properties-quicksight-dashboard-customactionurloperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
