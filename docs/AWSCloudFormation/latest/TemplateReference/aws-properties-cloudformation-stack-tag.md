---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-stack-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::Stack Tag
<a name="aws-properties-cloudformation-stack-tag"></a>

The Tag type enables you to specify a key-value pair that can be used to store information about an CloudFormation stack.

## Syntax
<a name="aws-properties-cloudformation-stack-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-stack-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cloudformation-stack-tag-key)" : {{String}},
  "[Value](#cfn-cloudformation-stack-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudformation-stack-tag-syntax.yaml"></a>

```
  [Key](#cfn-cloudformation-stack-tag-key): {{String}}
  [Value](#cfn-cloudformation-stack-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cloudformation-stack-tag-properties"></a>

`Key`  <a name="cfn-cloudformation-stack-tag-key"></a>
A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by AWS have the reserved prefix: `aws:`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudformation-stack-tag-value"></a>
A string that contains the value for this tag. You can specify a maximum of 256 characters for a tag value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
