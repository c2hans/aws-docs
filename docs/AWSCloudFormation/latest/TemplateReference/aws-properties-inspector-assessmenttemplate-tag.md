---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspector-assessmenttemplate-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Inspector::AssessmentTemplate Tag
<a name="aws-properties-inspector-assessmenttemplate-tag"></a>

A key and value pair. This data type is used as a request parameter in the [SetTagsForResource](https://docs.aws.amazon.com/inspector/v1/APIReference/API_SetTagsForResource.html) action and a response element in the [ListTagsForResource](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListTagsForResource.html) action.

## Syntax
<a name="aws-properties-inspector-assessmenttemplate-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspector-assessmenttemplate-tag-syntax.json"></a>

```
{
  "[Key](#cfn-inspector-assessmenttemplate-tag-key)" : {{String}},
  "[Value](#cfn-inspector-assessmenttemplate-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspector-assessmenttemplate-tag-syntax.yaml"></a>

```
  [Key](#cfn-inspector-assessmenttemplate-tag-key): {{String}}
  [Value](#cfn-inspector-assessmenttemplate-tag-value): {{String}}
```

## Properties
<a name="aws-properties-inspector-assessmenttemplate-tag-properties"></a>

`Key`  <a name="cfn-inspector-assessmenttemplate-tag-key"></a>
A tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-inspector-assessmenttemplate-tag-value"></a>
A value assigned to a tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
