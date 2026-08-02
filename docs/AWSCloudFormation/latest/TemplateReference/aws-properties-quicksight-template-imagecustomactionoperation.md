---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-imagecustomactionoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ImageCustomActionOperation
<a name="aws-properties-quicksight-template-imagecustomactionoperation"></a>

The operation that is defined by the custom action.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-template-imagecustomactionoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-imagecustomactionoperation-syntax.json"></a>

```
{
  "[NavigationOperation](#cfn-quicksight-template-imagecustomactionoperation-navigationoperation)" : {{CustomActionNavigationOperation}},
  "[SetParametersOperation](#cfn-quicksight-template-imagecustomactionoperation-setparametersoperation)" : {{CustomActionSetParametersOperation}},
  "[URLOperation](#cfn-quicksight-template-imagecustomactionoperation-urloperation)" : {{CustomActionURLOperation}}
}
```

### YAML
<a name="aws-properties-quicksight-template-imagecustomactionoperation-syntax.yaml"></a>

```
  [NavigationOperation](#cfn-quicksight-template-imagecustomactionoperation-navigationoperation): {{
    CustomActionNavigationOperation}}
  [SetParametersOperation](#cfn-quicksight-template-imagecustomactionoperation-setparametersoperation): {{
    CustomActionSetParametersOperation}}
  [URLOperation](#cfn-quicksight-template-imagecustomactionoperation-urloperation): {{
    CustomActionURLOperation}}
```

## Properties
<a name="aws-properties-quicksight-template-imagecustomactionoperation-properties"></a>

`NavigationOperation`  <a name="cfn-quicksight-template-imagecustomactionoperation-navigationoperation"></a>
Property description not available.
*Required*: No
*Type*: [CustomActionNavigationOperation](aws-properties-quicksight-template-customactionnavigationoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SetParametersOperation`  <a name="cfn-quicksight-template-imagecustomactionoperation-setparametersoperation"></a>
Property description not available.
*Required*: No
*Type*: [CustomActionSetParametersOperation](aws-properties-quicksight-template-customactionsetparametersoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`URLOperation`  <a name="cfn-quicksight-template-imagecustomactionoperation-urloperation"></a>
Property description not available.
*Required*: No
*Type*: [CustomActionURLOperation](aws-properties-quicksight-template-customactionurloperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
