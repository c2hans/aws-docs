---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-layercustomactionoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard LayerCustomActionOperation
<a name="aws-properties-quicksight-dashboard-layercustomactionoperation"></a>

The operation that is defined by the custom action.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-dashboard-layercustomactionoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-layercustomactionoperation-syntax.json"></a>

```
{
  "[FilterOperation](#cfn-quicksight-dashboard-layercustomactionoperation-filteroperation)" : {{CustomActionFilterOperation}},
  "[NavigationOperation](#cfn-quicksight-dashboard-layercustomactionoperation-navigationoperation)" : {{CustomActionNavigationOperation}},
  "[SetParametersOperation](#cfn-quicksight-dashboard-layercustomactionoperation-setparametersoperation)" : {{CustomActionSetParametersOperation}},
  "[URLOperation](#cfn-quicksight-dashboard-layercustomactionoperation-urloperation)" : {{CustomActionURLOperation}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-layercustomactionoperation-syntax.yaml"></a>

```
  [FilterOperation](#cfn-quicksight-dashboard-layercustomactionoperation-filteroperation): {{
    CustomActionFilterOperation}}
  [NavigationOperation](#cfn-quicksight-dashboard-layercustomactionoperation-navigationoperation): {{
    CustomActionNavigationOperation}}
  [SetParametersOperation](#cfn-quicksight-dashboard-layercustomactionoperation-setparametersoperation): {{
    CustomActionSetParametersOperation}}
  [URLOperation](#cfn-quicksight-dashboard-layercustomactionoperation-urloperation): {{
    CustomActionURLOperation}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-layercustomactionoperation-properties"></a>

`FilterOperation`  <a name="cfn-quicksight-dashboard-layercustomactionoperation-filteroperation"></a>
Property description not available.
*Required*: No
*Type*: [CustomActionFilterOperation](aws-properties-quicksight-dashboard-customactionfilteroperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NavigationOperation`  <a name="cfn-quicksight-dashboard-layercustomactionoperation-navigationoperation"></a>
Property description not available.
*Required*: No
*Type*: [CustomActionNavigationOperation](aws-properties-quicksight-dashboard-customactionnavigationoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SetParametersOperation`  <a name="cfn-quicksight-dashboard-layercustomactionoperation-setparametersoperation"></a>
Property description not available.
*Required*: No
*Type*: [CustomActionSetParametersOperation](aws-properties-quicksight-dashboard-customactionsetparametersoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`URLOperation`  <a name="cfn-quicksight-dashboard-layercustomactionoperation-urloperation"></a>
Property description not available.
*Required*: No
*Type*: [CustomActionURLOperation](aws-properties-quicksight-dashboard-customactionurloperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
