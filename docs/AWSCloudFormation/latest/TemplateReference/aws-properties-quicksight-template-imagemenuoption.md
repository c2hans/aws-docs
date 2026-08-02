---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-imagemenuoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ImageMenuOption
<a name="aws-properties-quicksight-template-imagemenuoption"></a>

The menu options for the interactions of an image.

## Syntax
<a name="aws-properties-quicksight-template-imagemenuoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-imagemenuoption-syntax.json"></a>

```
{
  "[AvailabilityStatus](#cfn-quicksight-template-imagemenuoption-availabilitystatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-imagemenuoption-syntax.yaml"></a>

```
  [AvailabilityStatus](#cfn-quicksight-template-imagemenuoption-availabilitystatus): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-imagemenuoption-properties"></a>

`AvailabilityStatus`  <a name="cfn-quicksight-template-imagemenuoption-availabilitystatus"></a>
The availability status of the image menu. If the value of this property is set to `ENABLED`, dashboard readers can interact with the image menu.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
