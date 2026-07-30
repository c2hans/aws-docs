---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualservice-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualService Tag
<a name="aws-properties-appmesh-virtualservice-tag"></a>

Optional metadata that you can apply to the virtual service to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

## Syntax
<a name="aws-properties-appmesh-virtualservice-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualservice-tag-syntax.json"></a>

```
{
  "[Key](#cfn-appmesh-virtualservice-tag-key)" : {{String}},
  "[Value](#cfn-appmesh-virtualservice-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualservice-tag-syntax.yaml"></a>

```
  [Key](#cfn-appmesh-virtualservice-tag-key): {{String}}
  [Value](#cfn-appmesh-virtualservice-tag-value): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualservice-tag-properties"></a>

`Key`  <a name="cfn-appmesh-virtualservice-tag-key"></a>
One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appmesh-virtualservice-tag-value"></a>
The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
