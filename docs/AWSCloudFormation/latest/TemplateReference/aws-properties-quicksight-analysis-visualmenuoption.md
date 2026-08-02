---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-visualmenuoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis VisualMenuOption
<a name="aws-properties-quicksight-analysis-visualmenuoption"></a>

The menu options for a visual.

## Syntax
<a name="aws-properties-quicksight-analysis-visualmenuoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-visualmenuoption-syntax.json"></a>

```
{
  "[AvailabilityStatus](#cfn-quicksight-analysis-visualmenuoption-availabilitystatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-visualmenuoption-syntax.yaml"></a>

```
  [AvailabilityStatus](#cfn-quicksight-analysis-visualmenuoption-availabilitystatus): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-visualmenuoption-properties"></a>

`AvailabilityStatus`  <a name="cfn-quicksight-analysis-visualmenuoption-availabilitystatus"></a>
The availaiblity status of a visual's menu options.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
