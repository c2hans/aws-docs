---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-profile-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Profile Tag
<a name="aws-properties-b2bi-profile-tag"></a>

Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.

## Syntax
<a name="aws-properties-b2bi-profile-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-profile-tag-syntax.json"></a>

```
{
  "[Key](#cfn-b2bi-profile-tag-key)" : {{String}},
  "[Value](#cfn-b2bi-profile-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-profile-tag-syntax.yaml"></a>

```
  [Key](#cfn-b2bi-profile-tag-key): {{String}}
  [Value](#cfn-b2bi-profile-tag-value): {{String}}
```

## Properties
<a name="aws-properties-b2bi-profile-tag-properties"></a>

`Key`  <a name="cfn-b2bi-profile-tag-key"></a>
Specifies the name assigned to the tag that you create.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-b2bi-profile-tag-value"></a>
Contains one or more values that you assigned to the key name that you create.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
