---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-shield-protection-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Shield::Protection Tag
<a name="aws-properties-shield-protection-tag"></a>

A tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing or other management. Typically, the tag key represents a category, such as "environment", and the tag value represents a specific value within that category, such as "test," "development," or "production". Or you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.

## Syntax
<a name="aws-properties-shield-protection-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-shield-protection-tag-syntax.json"></a>

```
{
  "[Key](#cfn-shield-protection-tag-key)" : {{String}},
  "[Value](#cfn-shield-protection-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-shield-protection-tag-syntax.yaml"></a>

```
  [Key](#cfn-shield-protection-tag-key): {{String}}
  [Value](#cfn-shield-protection-tag-value): {{String}}
```

## Properties
<a name="aws-properties-shield-protection-tag-properties"></a>

`Key`  <a name="cfn-shield-protection-tag-key"></a>
Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-shield-protection-tag-value"></a>
Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
