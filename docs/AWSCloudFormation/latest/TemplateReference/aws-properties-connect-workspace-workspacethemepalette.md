---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-workspace-workspacethemepalette.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace WorkspaceThemePalette
<a name="aws-properties-connect-workspace-workspacethemepalette"></a>

Contains color palette configuration for different areas of a workspace.

## Syntax
<a name="aws-properties-connect-workspace-workspacethemepalette-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-workspace-workspacethemepalette-syntax.json"></a>

```
{
  "[Canvas](#cfn-connect-workspace-workspacethemepalette-canvas)" : {{PaletteCanvas}},
  "[Header](#cfn-connect-workspace-workspacethemepalette-header)" : {{PaletteHeader}},
  "[Navigation](#cfn-connect-workspace-workspacethemepalette-navigation)" : {{PaletteNavigation}},
  "[Primary](#cfn-connect-workspace-workspacethemepalette-primary)" : {{PalettePrimary}}
}
```

### YAML
<a name="aws-properties-connect-workspace-workspacethemepalette-syntax.yaml"></a>

```
  [Canvas](#cfn-connect-workspace-workspacethemepalette-canvas): {{
    PaletteCanvas}}
  [Header](#cfn-connect-workspace-workspacethemepalette-header): {{
    PaletteHeader}}
  [Navigation](#cfn-connect-workspace-workspacethemepalette-navigation): {{
    PaletteNavigation}}
  [Primary](#cfn-connect-workspace-workspacethemepalette-primary): {{
    PalettePrimary}}
```

## Properties
<a name="aws-properties-connect-workspace-workspacethemepalette-properties"></a>

`Canvas`  <a name="cfn-connect-workspace-workspacethemepalette-canvas"></a>
The color configuration for the canvas area.
*Required*: No
*Type*: [PaletteCanvas](aws-properties-connect-workspace-palettecanvas.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Header`  <a name="cfn-connect-workspace-workspacethemepalette-header"></a>
The color configuration for the header area.
*Required*: No
*Type*: [PaletteHeader](aws-properties-connect-workspace-paletteheader.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Navigation`  <a name="cfn-connect-workspace-workspacethemepalette-navigation"></a>
The color configuration for the navigation area.
*Required*: No
*Type*: [PaletteNavigation](aws-properties-connect-workspace-palettenavigation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Primary`  <a name="cfn-connect-workspace-workspacethemepalette-primary"></a>
The primary color configuration used throughout the workspace.
*Required*: No
*Type*: [PalettePrimary](aws-properties-connect-workspace-paletteprimary.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
