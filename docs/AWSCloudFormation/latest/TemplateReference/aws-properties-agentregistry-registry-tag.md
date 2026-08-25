---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry Tag
<a name="aws-properties-agentregistry-registry-tag"></a>

Metadata that you can assign to a registry, consisting of a key-value pair.

## Syntax
<a name="aws-properties-agentregistry-registry-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-tag-syntax.json"></a>

```
{
  "[Key](#cfn-agentregistry-registry-tag-key)" : {{String}},
  "[Value](#cfn-agentregistry-registry-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-tag-syntax.yaml"></a>

```
  [Key](#cfn-agentregistry-registry-tag-key): {{String}}
  [Value](#cfn-agentregistry-registry-tag-value): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registry-tag-properties"></a>

`Key`  <a name="cfn-agentregistry-registry-tag-key"></a>
A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-agentregistry-registry-tag-value"></a>
The value for the specified tag key.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
