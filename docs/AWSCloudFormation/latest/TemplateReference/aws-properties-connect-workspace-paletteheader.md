---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-workspace-paletteheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace PaletteHeader
<a name="aws-properties-connect-workspace-paletteheader"></a>

Contains color configuration for header elements in a workspace theme.

## Syntax
<a name="aws-properties-connect-workspace-paletteheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-workspace-paletteheader-syntax.json"></a>

```
{
  "[Background](#cfn-connect-workspace-paletteheader-background)" : {{String}},
  "[InvertActionsColors](#cfn-connect-workspace-paletteheader-invertactionscolors)" : {{Boolean}},
  "[Text](#cfn-connect-workspace-paletteheader-text)" : {{String}},
  "[TextHover](#cfn-connect-workspace-paletteheader-texthover)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-workspace-paletteheader-syntax.yaml"></a>

```
  [Background](#cfn-connect-workspace-paletteheader-background): {{String}}
  [InvertActionsColors](#cfn-connect-workspace-paletteheader-invertactionscolors): {{Boolean}}
  [Text](#cfn-connect-workspace-paletteheader-text): {{String}}
  [TextHover](#cfn-connect-workspace-paletteheader-texthover): {{String}}
```

## Properties
<a name="aws-properties-connect-workspace-paletteheader-properties"></a>

`Background`  <a name="cfn-connect-workspace-paletteheader-background"></a>
The background color of the header.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvertActionsColors`  <a name="cfn-connect-workspace-paletteheader-invertactionscolors"></a>
Whether to invert the colors of action buttons in the header.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-connect-workspace-paletteheader-text"></a>
The text color in the header.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextHover`  <a name="cfn-connect-workspace-paletteheader-texthover"></a>
The text color when hovering over header elements.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
