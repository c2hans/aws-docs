---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-inboundexternallink-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::InboundExternalLink Tag
<a name="aws-properties-rtbfabric-inboundexternallink-tag"></a>

<a name="aws-properties-rtbfabric-inboundexternallink-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::RTBFabric::InboundExternalLink](aws-resource-rtbfabric-inboundexternallink.md).

## Syntax
<a name="aws-properties-rtbfabric-inboundexternallink-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-inboundexternallink-tag-syntax.json"></a>

```
{
  "[Key](#cfn-rtbfabric-inboundexternallink-tag-key)" : {{String}},
  "[Value](#cfn-rtbfabric-inboundexternallink-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-rtbfabric-inboundexternallink-tag-syntax.yaml"></a>

```
  [Key](#cfn-rtbfabric-inboundexternallink-tag-key): {{String}}
  [Value](#cfn-rtbfabric-inboundexternallink-tag-value): {{String}}
```

## Properties
<a name="aws-properties-rtbfabric-inboundexternallink-tag-properties"></a>

`Key`  <a name="cfn-rtbfabric-inboundexternallink-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(resourceArn|internalId|[a-zA-Z0-9+\-=._:/@]+)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-rtbfabric-inboundexternallink-tag-value"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
