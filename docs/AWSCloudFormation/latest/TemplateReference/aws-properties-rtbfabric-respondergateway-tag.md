---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-respondergateway-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::ResponderGateway Tag
<a name="aws-properties-rtbfabric-respondergateway-tag"></a>

<a name="aws-properties-rtbfabric-respondergateway-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::RTBFabric::ResponderGateway](aws-resource-rtbfabric-respondergateway.md).

## Syntax
<a name="aws-properties-rtbfabric-respondergateway-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-respondergateway-tag-syntax.json"></a>

```
{
  "[Key](#cfn-rtbfabric-respondergateway-tag-key)" : {{String}},
  "[Value](#cfn-rtbfabric-respondergateway-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-rtbfabric-respondergateway-tag-syntax.yaml"></a>

```
  [Key](#cfn-rtbfabric-respondergateway-tag-key): {{String}}
  [Value](#cfn-rtbfabric-respondergateway-tag-value): {{String}}
```

## Properties
<a name="aws-properties-rtbfabric-respondergateway-tag-properties"></a>

`Key`  <a name="cfn-rtbfabric-respondergateway-tag-key"></a>
The key name of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^(resourceArn|internalId|[a-zA-Z0-9+\-=._:/@]+)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-rtbfabric-respondergateway-tag-value"></a>
The value for the tag.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
