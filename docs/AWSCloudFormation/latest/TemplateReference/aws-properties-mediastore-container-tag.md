---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediastore-container-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaStore::Container Tag
<a name="aws-properties-mediastore-container-tag"></a>

A collection of tags associated with a container. Each tag consists of a key:value pair, which can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see [Tagging Resources in MediaStore](https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html).

## Syntax
<a name="aws-properties-mediastore-container-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediastore-container-tag-syntax.json"></a>

```
{
  "[Key](#cfn-mediastore-container-tag-key)" : {{String}},
  "[Value](#cfn-mediastore-container-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediastore-container-tag-syntax.yaml"></a>

```
  [Key](#cfn-mediastore-container-tag-key): {{String}}
  [Value](#cfn-mediastore-container-tag-value): {{String}}
```

## Properties
<a name="aws-properties-mediastore-container-tag-properties"></a>

`Key`  <a name="cfn-mediastore-container-tag-key"></a>
Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-mediastore-container-tag-value"></a>
Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
