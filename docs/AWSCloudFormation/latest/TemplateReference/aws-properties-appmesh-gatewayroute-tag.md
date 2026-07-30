---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute Tag
<a name="aws-properties-appmesh-gatewayroute-tag"></a>

Optional metadata that you can apply to the gateway route to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-tag-syntax.json"></a>

```
{
  "[Key](#cfn-appmesh-gatewayroute-tag-key)" : {{String}},
  "[Value](#cfn-appmesh-gatewayroute-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-tag-syntax.yaml"></a>

```
  [Key](#cfn-appmesh-gatewayroute-tag-key): {{String}}
  [Value](#cfn-appmesh-gatewayroute-tag-value): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-tag-properties"></a>

`Key`  <a name="cfn-appmesh-gatewayroute-tag-key"></a>
One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appmesh-gatewayroute-tag-value"></a>
The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
