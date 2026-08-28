---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-workspace-palettenavigation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace PaletteNavigation
<a name="aws-properties-connect-workspace-palettenavigation"></a>

Contains color configuration for navigation elements in a workspace theme.

## Syntax
<a name="aws-properties-connect-workspace-palettenavigation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-workspace-palettenavigation-syntax.json"></a>

```
{
  "[Background](#cfn-connect-workspace-palettenavigation-background)" : {{String}},
  "[InvertActionsColors](#cfn-connect-workspace-palettenavigation-invertactionscolors)" : {{Boolean}},
  "[Text](#cfn-connect-workspace-palettenavigation-text)" : {{String}},
  "[TextActive](#cfn-connect-workspace-palettenavigation-textactive)" : {{String}},
  "[TextBackgroundActive](#cfn-connect-workspace-palettenavigation-textbackgroundactive)" : {{String}},
  "[TextBackgroundHover](#cfn-connect-workspace-palettenavigation-textbackgroundhover)" : {{String}},
  "[TextHover](#cfn-connect-workspace-palettenavigation-texthover)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-workspace-palettenavigation-syntax.yaml"></a>

```
  [Background](#cfn-connect-workspace-palettenavigation-background): {{String}}
  [InvertActionsColors](#cfn-connect-workspace-palettenavigation-invertactionscolors): {{Boolean}}
  [Text](#cfn-connect-workspace-palettenavigation-text): {{String}}
  [TextActive](#cfn-connect-workspace-palettenavigation-textactive): {{String}}
  [TextBackgroundActive](#cfn-connect-workspace-palettenavigation-textbackgroundactive): {{String}}
  [TextBackgroundHover](#cfn-connect-workspace-palettenavigation-textbackgroundhover): {{String}}
  [TextHover](#cfn-connect-workspace-palettenavigation-texthover): {{String}}
```

## Properties
<a name="aws-properties-connect-workspace-palettenavigation-properties"></a>

`Background`  <a name="cfn-connect-workspace-palettenavigation-background"></a>
The background color of the navigation area.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvertActionsColors`  <a name="cfn-connect-workspace-palettenavigation-invertactionscolors"></a>
Whether to invert the colors of action buttons in the navigation area.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-connect-workspace-palettenavigation-text"></a>
The text color in the navigation area.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextActive`  <a name="cfn-connect-workspace-palettenavigation-textactive"></a>
The text color for active navigation items.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextBackgroundActive`  <a name="cfn-connect-workspace-palettenavigation-textbackgroundactive"></a>
The background color for active navigation items.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextBackgroundHover`  <a name="cfn-connect-workspace-palettenavigation-textbackgroundhover"></a>
The background color when hovering over navigation text.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextHover`  <a name="cfn-connect-workspace-palettenavigation-texthover"></a>
The text color when hovering over navigation items.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
