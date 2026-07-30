---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-workspace-workspacepage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace WorkspacePage
<a name="aws-properties-connect-workspace-workspacepage"></a>

Contains information about a page configuration in a workspace, including the view assigned to the page.

## Syntax
<a name="aws-properties-connect-workspace-workspacepage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-workspace-workspacepage-syntax.json"></a>

```
{
  "[InputData](#cfn-connect-workspace-workspacepage-inputdata)" : {{String}},
  "[Page](#cfn-connect-workspace-workspacepage-page)" : {{String}},
  "[ResourceArn](#cfn-connect-workspace-workspacepage-resourcearn)" : {{String}},
  "[Slug](#cfn-connect-workspace-workspacepage-slug)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-workspace-workspacepage-syntax.yaml"></a>

```
  [InputData](#cfn-connect-workspace-workspacepage-inputdata): {{String}}
  [Page](#cfn-connect-workspace-workspacepage-page): {{String}}
  [ResourceArn](#cfn-connect-workspace-workspacepage-resourcearn): {{String}}
  [Slug](#cfn-connect-workspace-workspacepage-slug): {{String}}
```

## Properties
<a name="aws-properties-connect-workspace-workspacepage-properties"></a>

`InputData`  <a name="cfn-connect-workspace-workspacepage-inputdata"></a>
A JSON string containing input parameters passed to the view when the page is rendered.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Page`  <a name="cfn-connect-workspace-workspacepage-page"></a>
The page identifier. System pages include `HOME` and `AGENT_EXPERIENCE`.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\.$)(?!\.\.$)[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-connect-workspace-workspacepage-resourcearn"></a>
The Amazon Resource Name (ARN) of the view associated with this page.
*Required*: Yes
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Slug`  <a name="cfn-connect-workspace-workspacepage-slug"></a>
The URL-friendly identifier for the page.
*Required*: No
*Type*: String
*Pattern*: `^$|^[\p{L}\p{Z}\p{N}\-_.:=@'|]{3,}$`
*Minimum*: `0`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
