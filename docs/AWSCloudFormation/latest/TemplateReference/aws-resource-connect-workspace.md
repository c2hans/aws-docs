---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-workspace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace
<a name="aws-resource-connect-workspace"></a>

Contains information about a workspace, which defines the user experience by mapping views to pages.

## Syntax
<a name="aws-resource-connect-workspace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-workspace-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::Workspace",
  "Properties" : {
      "[Associations](#cfn-connect-workspace-associations)" : {{[ String, ... ]}},
      "[Description](#cfn-connect-workspace-description)" : {{String}},
      "[InstanceArn](#cfn-connect-workspace-instancearn)" : {{String}},
      "[Media](#cfn-connect-workspace-media)" : {{[ MediaItem, ... ]}},
      "[Name](#cfn-connect-workspace-name)" : {{String}},
      "[Pages](#cfn-connect-workspace-pages)" : {{[ WorkspacePage, ... ]}},
      "[Tags](#cfn-connect-workspace-tags)" : {{[ Tag, ... ]}},
      "[Theme](#cfn-connect-workspace-theme)" : {{WorkspaceTheme}},
      "[Title](#cfn-connect-workspace-title)" : {{String}},
      "[Visibility](#cfn-connect-workspace-visibility)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-workspace-syntax.yaml"></a>

```
Type: AWS::Connect::Workspace
Properties:
  [Associations](#cfn-connect-workspace-associations): {{
    - String}}
  [Description](#cfn-connect-workspace-description): {{String}}
  [InstanceArn](#cfn-connect-workspace-instancearn): {{String}}
  [Media](#cfn-connect-workspace-media): {{
    - MediaItem}}
  [Name](#cfn-connect-workspace-name): {{String}}
  [Pages](#cfn-connect-workspace-pages): {{
    - WorkspacePage}}
  [Tags](#cfn-connect-workspace-tags): {{
    - Tag}}
  [Theme](#cfn-connect-workspace-theme): {{
    WorkspaceTheme}}
  [Title](#cfn-connect-workspace-title): {{String}}
  [Visibility](#cfn-connect-workspace-visibility): {{String}}
```

## Properties
<a name="aws-resource-connect-workspace-properties"></a>

`Associations`  <a name="cfn-connect-workspace-associations"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-connect-workspace-description"></a>
The description of the workspace.
*Required*: No
*Type*: String
*Pattern*: `^[\P{C} ]*$`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-workspace-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Media`  <a name="cfn-connect-workspace-media"></a>
Property description not available.
*Required*: No
*Type*: Array of [MediaItem](aws-properties-connect-workspace-mediaitem.md)
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-workspace-name"></a>
The name of the workspace.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pages`  <a name="cfn-connect-workspace-pages"></a>
Property description not available.
*Required*: No
*Type*: Array of [WorkspacePage](aws-properties-connect-workspace-workspacepage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-workspace-tags"></a>
The tags used to organize, track, or control access for the workspace.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-workspace-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Theme`  <a name="cfn-connect-workspace-theme"></a>
The theme configuration for the workspace, including colors and styling.
*Required*: No
*Type*: [WorkspaceTheme](aws-properties-connect-workspace-workspacetheme.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-connect-workspace-title"></a>
The title displayed for the workspace.
*Required*: No
*Type*: String
*Pattern*: `^[\P{C}]*$`
*Minimum*: `0`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-connect-workspace-visibility"></a>
Controls who can access the workspace. Valid values are: `ALL` (all users), `ASSIGNED` (only assigned users and routing profiles), and `NONE` (not visible).
*Required*: No
*Type*: String
*Allowed values*: `ALL | ASSIGNED | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-workspace-return-values"></a>

### Ref
<a name="aws-resource-connect-workspace-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-workspace-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-workspace-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
