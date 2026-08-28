---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-datasetgroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::DatasetGroup Tag
<a name="aws-properties-personalize-datasetgroup-tag"></a>

The optional metadata that you apply to resources to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information see [Tagging Amazon Personalize resources](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html).

## Syntax
<a name="aws-properties-personalize-datasetgroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-datasetgroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-personalize-datasetgroup-tag-key)" : {{String}},
  "[Value](#cfn-personalize-datasetgroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-personalize-datasetgroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-personalize-datasetgroup-tag-key): {{String}}
  [Value](#cfn-personalize-datasetgroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-personalize-datasetgroup-tag-properties"></a>

`Key`  <a name="cfn-personalize-datasetgroup-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-personalize-datasetgroup-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
