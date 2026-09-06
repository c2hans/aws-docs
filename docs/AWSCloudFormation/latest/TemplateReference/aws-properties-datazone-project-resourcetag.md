---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-project-resourcetag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Project ResourceTag
<a name="aws-properties-datazone-project-resourcetag"></a>

The resource tag of the project.

## Syntax
<a name="aws-properties-datazone-project-resourcetag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-project-resourcetag-syntax.json"></a>

```
{
  "[Key](#cfn-datazone-project-resourcetag-key)" : {{String}},
  "[Value](#cfn-datazone-project-resourcetag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-project-resourcetag-syntax.yaml"></a>

```
  [Key](#cfn-datazone-project-resourcetag-key): {{String}}
  [Value](#cfn-datazone-project-resourcetag-value): {{String}}
```

## Properties
<a name="aws-properties-datazone-project-resourcetag-properties"></a>

`Key`  <a name="cfn-datazone-project-resourcetag-key"></a>
The key of the resource tag of the project.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w \.:/=+@-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datazone-project-resourcetag-value"></a>
The value of the resource tag parameter key of the project profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w \.:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
