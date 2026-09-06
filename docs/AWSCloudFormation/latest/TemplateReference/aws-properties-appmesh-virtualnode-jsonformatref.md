---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-jsonformatref.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode JsonFormatRef
<a name="aws-properties-appmesh-virtualnode-jsonformatref"></a>

An object that represents the key value pairs for the JSON.

## Syntax
<a name="aws-properties-appmesh-virtualnode-jsonformatref-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-jsonformatref-syntax.json"></a>

```
{
  "[Key](#cfn-appmesh-virtualnode-jsonformatref-key)" : {{String}},
  "[Value](#cfn-appmesh-virtualnode-jsonformatref-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-jsonformatref-syntax.yaml"></a>

```
  [Key](#cfn-appmesh-virtualnode-jsonformatref-key): {{String}}
  [Value](#cfn-appmesh-virtualnode-jsonformatref-value): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-jsonformatref-properties"></a>

`Key`  <a name="cfn-appmesh-virtualnode-jsonformatref-key"></a>
The specified key for the JSON.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appmesh-virtualnode-jsonformatref-value"></a>
The specified value for the JSON.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
