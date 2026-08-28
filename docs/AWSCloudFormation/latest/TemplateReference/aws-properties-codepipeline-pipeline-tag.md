---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline Tag
<a name="aws-properties-codepipeline-pipeline-tag"></a>

A tag is a key-value pair that is used to manage the resource.

## Syntax
<a name="aws-properties-codepipeline-pipeline-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-tag-syntax.json"></a>

```
{
  "[Key](#cfn-codepipeline-pipeline-tag-key)" : {{String}},
  "[Value](#cfn-codepipeline-pipeline-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-tag-syntax.yaml"></a>

```
  [Key](#cfn-codepipeline-pipeline-tag-key): {{String}}
  [Value](#cfn-codepipeline-pipeline-tag-value): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-tag-properties"></a>

`Key`  <a name="cfn-codepipeline-pipeline-tag-key"></a>
The tag's key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-codepipeline-pipeline-tag-value"></a>
The tag's value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
