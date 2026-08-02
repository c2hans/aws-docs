---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-contextmenuoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ContextMenuOption
<a name="aws-properties-quicksight-analysis-contextmenuoption"></a>

The context menu options for a visual's interactions.

## Syntax
<a name="aws-properties-quicksight-analysis-contextmenuoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-contextmenuoption-syntax.json"></a>

```
{
  "[AvailabilityStatus](#cfn-quicksight-analysis-contextmenuoption-availabilitystatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-contextmenuoption-syntax.yaml"></a>

```
  [AvailabilityStatus](#cfn-quicksight-analysis-contextmenuoption-availabilitystatus): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-contextmenuoption-properties"></a>

`AvailabilityStatus`  <a name="cfn-quicksight-analysis-contextmenuoption-availabilitystatus"></a>
The availability status of the context menu options. If the value of this property is set to `ENABLED`, dashboard readers can interact with the context menu.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
