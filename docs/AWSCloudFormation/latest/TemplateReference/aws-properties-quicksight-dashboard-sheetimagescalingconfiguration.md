---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sheetimagescalingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SheetImageScalingConfiguration
<a name="aws-properties-quicksight-dashboard-sheetimagescalingconfiguration"></a>

Determines how the image is scaled

## Syntax
<a name="aws-properties-quicksight-dashboard-sheetimagescalingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sheetimagescalingconfiguration-syntax.json"></a>

```
{
  "[ScalingType](#cfn-quicksight-dashboard-sheetimagescalingconfiguration-scalingtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sheetimagescalingconfiguration-syntax.yaml"></a>

```
  [ScalingType](#cfn-quicksight-dashboard-sheetimagescalingconfiguration-scalingtype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sheetimagescalingconfiguration-properties"></a>

`ScalingType`  <a name="cfn-quicksight-dashboard-sheetimagescalingconfiguration-scalingtype"></a>
The scaling option to use when fitting the image inside the container.
Valid values are defined as follows:
+ `SCALE_TO_WIDTH`: The image takes up the entire width of the container. The image aspect ratio is preserved.
+ `SCALE_TO_HEIGHT`: The image takes up the entire height of the container. The image aspect ratio is preserved.
+ `SCALE_TO_CONTAINER`: The image takes up the entire width and height of the container. The image aspect ratio is not preserved.
+ `SCALE_NONE`: The image is displayed in its original size and is not scaled to the container.
*Required*: No
*Type*: String
*Allowed values*: `SCALE_TO_WIDTH | SCALE_TO_HEIGHT | SCALE_TO_CONTAINER | SCALE_NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
