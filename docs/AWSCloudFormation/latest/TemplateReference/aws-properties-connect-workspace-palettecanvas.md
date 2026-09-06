---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-workspace-palettecanvas.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace PaletteCanvas
<a name="aws-properties-connect-workspace-palettecanvas"></a>

Contains color configuration for canvas elements in a workspace theme.

## Syntax
<a name="aws-properties-connect-workspace-palettecanvas-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-workspace-palettecanvas-syntax.json"></a>

```
{
  "[ActiveBackground](#cfn-connect-workspace-palettecanvas-activebackground)" : {{String}},
  "[ContainerBackground](#cfn-connect-workspace-palettecanvas-containerbackground)" : {{String}},
  "[PageBackground](#cfn-connect-workspace-palettecanvas-pagebackground)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-workspace-palettecanvas-syntax.yaml"></a>

```
  [ActiveBackground](#cfn-connect-workspace-palettecanvas-activebackground): {{String}}
  [ContainerBackground](#cfn-connect-workspace-palettecanvas-containerbackground): {{String}}
  [PageBackground](#cfn-connect-workspace-palettecanvas-pagebackground): {{String}}
```

## Properties
<a name="aws-properties-connect-workspace-palettecanvas-properties"></a>

`ActiveBackground`  <a name="cfn-connect-workspace-palettecanvas-activebackground"></a>
The background color for active elements.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerBackground`  <a name="cfn-connect-workspace-palettecanvas-containerbackground"></a>
The background color for container elements.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PageBackground`  <a name="cfn-connect-workspace-palettecanvas-pagebackground"></a>
The background color for page elements.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
