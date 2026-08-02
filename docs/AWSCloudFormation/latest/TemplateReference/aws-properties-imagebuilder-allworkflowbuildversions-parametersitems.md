---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-allworkflowbuildversions-parametersitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::AllWorkflowBuildVersions ParametersItems
<a name="aws-properties-imagebuilder-allworkflowbuildversions-parametersitems"></a>

<a name="aws-properties-imagebuilder-allworkflowbuildversions-parametersitems-description"></a>The `ParametersItems` property type specifies Property description not available. for an [AWS::ImageBuilder::AllWorkflowBuildVersions](aws-resource-imagebuilder-allworkflowbuildversions.md).

## Syntax
<a name="aws-properties-imagebuilder-allworkflowbuildversions-parametersitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-allworkflowbuildversions-parametersitems-syntax.json"></a>

```
{
  "[DefaultValue](#cfn-imagebuilder-allworkflowbuildversions-parametersitems-defaultvalue)" : {{[ String, ... ]}},
  "[Description](#cfn-imagebuilder-allworkflowbuildversions-parametersitems-description)" : {{String}},
  "[Name](#cfn-imagebuilder-allworkflowbuildversions-parametersitems-name)" : {{String}},
  "[Type](#cfn-imagebuilder-allworkflowbuildversions-parametersitems-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-allworkflowbuildversions-parametersitems-syntax.yaml"></a>

```
  [DefaultValue](#cfn-imagebuilder-allworkflowbuildversions-parametersitems-defaultvalue): {{
    - String}}
  [Description](#cfn-imagebuilder-allworkflowbuildversions-parametersitems-description): {{String}}
  [Name](#cfn-imagebuilder-allworkflowbuildversions-parametersitems-name): {{String}}
  [Type](#cfn-imagebuilder-allworkflowbuildversions-parametersitems-type): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-allworkflowbuildversions-parametersitems-properties"></a>

`DefaultValue`  <a name="cfn-imagebuilder-allworkflowbuildversions-parametersitems-defaultvalue"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-imagebuilder-allworkflowbuildversions-parametersitems-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-imagebuilder-allworkflowbuildversions-parametersitems-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-imagebuilder-allworkflowbuildversions-parametersitems-type"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
