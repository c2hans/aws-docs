---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codestarconnections-connection-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeStarConnections::Connection Tag
<a name="aws-properties-codestarconnections-connection-tag"></a>

A tag is a key-value pair that is used to manage the resource.

This tag is available for use by AWS services that support tags.

## Syntax
<a name="aws-properties-codestarconnections-connection-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codestarconnections-connection-tag-syntax.json"></a>

```
{
  "[Key](#cfn-codestarconnections-connection-tag-key)" : {{String}},
  "[Value](#cfn-codestarconnections-connection-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-codestarconnections-connection-tag-syntax.yaml"></a>

```
  [Key](#cfn-codestarconnections-connection-tag-key): {{String}}
  [Value](#cfn-codestarconnections-connection-tag-value): {{String}}
```

## Properties
<a name="aws-properties-codestarconnections-connection-tag-properties"></a>

`Key`  <a name="cfn-codestarconnections-connection-tag-key"></a>
The tag's key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-codestarconnections-connection-tag-value"></a>
The tag's value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
