---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy Tag
<a name="aws-properties-dlm-lifecyclepolicy-tag"></a>

Specifies a tag for a resource.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-tag-syntax.json"></a>

```
{
  "[Key](#cfn-dlm-lifecyclepolicy-tag-key)" : {{String}},
  "[Value](#cfn-dlm-lifecyclepolicy-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-tag-syntax.yaml"></a>

```
  [Key](#cfn-dlm-lifecyclepolicy-tag-key): {{String}}
  [Value](#cfn-dlm-lifecyclepolicy-tag-value): {{String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-tag-properties"></a>

`Key`  <a name="cfn-dlm-lifecyclepolicy-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{all}]*`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-dlm-lifecyclepolicy-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{all}]*`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
