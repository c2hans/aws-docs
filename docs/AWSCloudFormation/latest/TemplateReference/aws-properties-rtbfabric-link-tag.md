---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link Tag
<a name="aws-properties-rtbfabric-link-tag"></a>

<a name="aws-properties-rtbfabric-link-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::RTBFabric::Link](aws-resource-rtbfabric-link.md).

## Syntax
<a name="aws-properties-rtbfabric-link-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-tag-syntax.json"></a>

```
{
  "[Key](#cfn-rtbfabric-link-tag-key)" : {{String}},
  "[Value](#cfn-rtbfabric-link-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-tag-syntax.yaml"></a>

```
  [Key](#cfn-rtbfabric-link-tag-key): {{String}}
  [Value](#cfn-rtbfabric-link-tag-value): {{String}}
```

## Properties
<a name="aws-properties-rtbfabric-link-tag-properties"></a>

`Key`  <a name="cfn-rtbfabric-link-tag-key"></a>
The key name of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^(resourceArn|internalId|[a-zA-Z0-9+\-=._:/@]+)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-rtbfabric-link-tag-value"></a>
The value for the tag.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
