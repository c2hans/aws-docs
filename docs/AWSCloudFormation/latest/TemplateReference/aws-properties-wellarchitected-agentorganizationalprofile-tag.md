---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wellarchitected-agentorganizationalprofile-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::AgentOrganizationalProfile Tag
<a name="aws-properties-wellarchitected-agentorganizationalprofile-tag"></a>

A key-value pair associated with a resource for cost allocation and access control.

## Syntax
<a name="aws-properties-wellarchitected-agentorganizationalprofile-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wellarchitected-agentorganizationalprofile-tag-syntax.json"></a>

```
{
  "[Key](#cfn-wellarchitected-agentorganizationalprofile-tag-key)" : {{String}},
  "[Value](#cfn-wellarchitected-agentorganizationalprofile-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-wellarchitected-agentorganizationalprofile-tag-syntax.yaml"></a>

```
  [Key](#cfn-wellarchitected-agentorganizationalprofile-tag-key): {{String}}
  [Value](#cfn-wellarchitected-agentorganizationalprofile-tag-value): {{String}}
```

## Properties
<a name="aws-properties-wellarchitected-agentorganizationalprofile-tag-properties"></a>

`Key`  <a name="cfn-wellarchitected-agentorganizationalprofile-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-wellarchitected-agentorganizationalprofile-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
