---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-custominstructions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic CustomInstructions
<a name="aws-properties-quicksight-topic-custominstructions"></a>

Instructions that provide additional guidance and context for response generation.

## Syntax
<a name="aws-properties-quicksight-topic-custominstructions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-custominstructions-syntax.json"></a>

```
{
  "[CustomInstructionsString](#cfn-quicksight-topic-custominstructions-custominstructionsstring)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-custominstructions-syntax.yaml"></a>

```
  [CustomInstructionsString](#cfn-quicksight-topic-custominstructions-custominstructionsstring): {{
    String}}
```

## Properties
<a name="aws-properties-quicksight-topic-custominstructions-properties"></a>

`CustomInstructionsString`  <a name="cfn-quicksight-topic-custominstructions-custominstructionsstring"></a>
A text field for providing additional guidance or context for response generation.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
