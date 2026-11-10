---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-visualmessages.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis VisualMessages
<a name="aws-properties-quicksight-analysis-visualmessages"></a>

The messages that are displayed on a visual under specific conditions, such as when the visual returns no data.

## Syntax
<a name="aws-properties-quicksight-analysis-visualmessages-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-visualmessages-syntax.json"></a>

```
{
  "[NoDataMessage](#cfn-quicksight-analysis-visualmessages-nodatamessage)" : {{VisualMessageConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-visualmessages-syntax.yaml"></a>

```
  [NoDataMessage](#cfn-quicksight-analysis-visualmessages-nodatamessage): {{
    VisualMessageConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-visualmessages-properties"></a>

`NoDataMessage`  <a name="cfn-quicksight-analysis-visualmessages-nodatamessage"></a>
The message that is displayed on a visual when there is no data to display.
*Required*: No
*Type*: [VisualMessageConfiguration](aws-properties-quicksight-analysis-visualmessageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
