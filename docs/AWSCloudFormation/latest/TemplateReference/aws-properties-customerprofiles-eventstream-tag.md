---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventstream-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventStream Tag
<a name="aws-properties-customerprofiles-eventstream-tag"></a>

<a name="aws-properties-customerprofiles-eventstream-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::CustomerProfiles::EventStream](aws-resource-customerprofiles-eventstream.md).

## Syntax
<a name="aws-properties-customerprofiles-eventstream-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventstream-tag-syntax.json"></a>

```
{
  "[Key](#cfn-customerprofiles-eventstream-tag-key)" : {{String}},
  "[Value](#cfn-customerprofiles-eventstream-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventstream-tag-syntax.yaml"></a>

```
  [Key](#cfn-customerprofiles-eventstream-tag-key): {{String}}
  [Value](#cfn-customerprofiles-eventstream-tag-value): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-eventstream-tag-properties"></a>

`Key`  <a name="cfn-customerprofiles-eventstream-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-customerprofiles-eventstream-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
