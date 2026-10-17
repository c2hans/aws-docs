---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wellarchitected-agentprofile-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::AgentProfile Tag
<a name="aws-properties-wellarchitected-agentprofile-tag"></a>

A key-value pair to associate with the profile.

## Syntax
<a name="aws-properties-wellarchitected-agentprofile-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wellarchitected-agentprofile-tag-syntax.json"></a>

```
{
  "[Key](#cfn-wellarchitected-agentprofile-tag-key)" : {{String}},
  "[Value](#cfn-wellarchitected-agentprofile-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-wellarchitected-agentprofile-tag-syntax.yaml"></a>

```
  [Key](#cfn-wellarchitected-agentprofile-tag-key): {{String}}
  [Value](#cfn-wellarchitected-agentprofile-tag-value): {{String}}
```

## Properties
<a name="aws-properties-wellarchitected-agentprofile-tag-properties"></a>

`Key`  <a name="cfn-wellarchitected-agentprofile-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-wellarchitected-agentprofile-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
