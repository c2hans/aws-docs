---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition Tag
<a name="aws-properties-customerprofiles-segmentdefinition-tag"></a>

The tag belonging to the segment definition.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-tag-syntax.json"></a>

```
{
  "[Key](#cfn-customerprofiles-segmentdefinition-tag-key)" : {{String}},
  "[Value](#cfn-customerprofiles-segmentdefinition-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-tag-syntax.yaml"></a>

```
  [Key](#cfn-customerprofiles-segmentdefinition-tag-key): {{String}}
  [Value](#cfn-customerprofiles-segmentdefinition-tag-value): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-tag-properties"></a>

`Key`  <a name="cfn-customerprofiles-segmentdefinition-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-customerprofiles-segmentdefinition-tag-value"></a>
One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
