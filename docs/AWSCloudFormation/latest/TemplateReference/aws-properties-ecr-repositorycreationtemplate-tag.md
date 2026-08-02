---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-repositorycreationtemplate-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::RepositoryCreationTemplate Tag
<a name="aws-properties-ecr-repositorycreationtemplate-tag"></a>

The metadata to apply to a resource to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

## Syntax
<a name="aws-properties-ecr-repositorycreationtemplate-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-repositorycreationtemplate-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ecr-repositorycreationtemplate-tag-key)" : {{String}},
  "[Value](#cfn-ecr-repositorycreationtemplate-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecr-repositorycreationtemplate-tag-syntax.yaml"></a>

```
  [Key](#cfn-ecr-repositorycreationtemplate-tag-key): {{String}}
  [Value](#cfn-ecr-repositorycreationtemplate-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ecr-repositorycreationtemplate-tag-properties"></a>

`Key`  <a name="cfn-ecr-repositorycreationtemplate-tag-key"></a>
One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ecr-repositorycreationtemplate-tag-value"></a>
A `value` acts as a descriptor within a tag category (key).
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
