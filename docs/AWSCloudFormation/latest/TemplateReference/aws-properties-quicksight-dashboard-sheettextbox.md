---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sheettextbox.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SheetTextBox
<a name="aws-properties-quicksight-dashboard-sheettextbox"></a>

A text box.

## Syntax
<a name="aws-properties-quicksight-dashboard-sheettextbox-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sheettextbox-syntax.json"></a>

```
{
  "[Content](#cfn-quicksight-dashboard-sheettextbox-content)" : {{String}},
  "[SheetTextBoxId](#cfn-quicksight-dashboard-sheettextbox-sheettextboxid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sheettextbox-syntax.yaml"></a>

```
  [Content](#cfn-quicksight-dashboard-sheettextbox-content): {{String}}
  [SheetTextBoxId](#cfn-quicksight-dashboard-sheettextbox-sheettextboxid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sheettextbox-properties"></a>

`Content`  <a name="cfn-quicksight-dashboard-sheettextbox-content"></a>
The content that is displayed in the text box.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `150000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetTextBoxId`  <a name="cfn-quicksight-dashboard-sheettextbox-sheettextboxid"></a>
The unique identifier for a text box. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have text boxes that share identifiers.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
