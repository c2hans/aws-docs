---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-volume-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::Volume Tag
<a name="aws-properties-fsx-volume-tag"></a>

Specifies a key-value pair for a resource tag.

## Syntax
<a name="aws-properties-fsx-volume-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-volume-tag-syntax.json"></a>

```
{
  "[Key](#cfn-fsx-volume-tag-key)" : {{String}},
  "[Value](#cfn-fsx-volume-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-volume-tag-syntax.yaml"></a>

```
  [Key](#cfn-fsx-volume-tag-key): {{String}}
  [Value](#cfn-fsx-volume-tag-value): {{String}}
```

## Properties
<a name="aws-properties-fsx-volume-tag-properties"></a>

`Key`  <a name="cfn-fsx-volume-tag-key"></a>
A value that specifies the `TagKey`, the name of the tag. Tag keys must be unique for the resource to which they are attached.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-fsx-volume-tag-value"></a>
A value that specifies the `TagValue`, the value assigned to the corresponding tag key. Tag values can be null and don't have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
