---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-classification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::WorkGroup Classification
<a name="aws-properties-athena-workgroup-classification"></a>

A classification refers to a set of specific configurations.

## Syntax
<a name="aws-properties-athena-workgroup-classification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-workgroup-classification-syntax.json"></a>

```
{
  "[Name](#cfn-athena-workgroup-classification-name)" : {{String}},
  "[Properties](#cfn-athena-workgroup-classification-properties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-athena-workgroup-classification-syntax.yaml"></a>

```
  [Name](#cfn-athena-workgroup-classification-name): {{String}}
  [Properties](#cfn-athena-workgroup-classification-properties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-athena-workgroup-classification-properties"></a>

`Name`  <a name="cfn-athena-workgroup-classification-name"></a>
The name of the configuration classification.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-athena-workgroup-classification-properties"></a>
A set of properties specified within a configuration classification.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
