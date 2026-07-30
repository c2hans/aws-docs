---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aiops-investigationgroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AIOps::InvestigationGroup Tag
<a name="aws-properties-aiops-investigationgroup-tag"></a>

A list of key-value pairs to associate with the investigation group. You can associate as many as 50 tags with an investigation group. To be able to associate tags when you create the investigation group, you must have the `cloudwatch:TagResource` permission.

Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

## Syntax
<a name="aws-properties-aiops-investigationgroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aiops-investigationgroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-aiops-investigationgroup-tag-key)" : {{String}},
  "[Value](#cfn-aiops-investigationgroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-aiops-investigationgroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-aiops-investigationgroup-tag-key): {{String}}
  [Value](#cfn-aiops-investigationgroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-aiops-investigationgroup-tag-properties"></a>

`Key`  <a name="cfn-aiops-investigationgroup-tag-key"></a>
Assigns one or more tags (key-value pairs) to the specified resource.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.
You can associate as many as 50 tags with a resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-aiops-investigationgroup-tag-value"></a>
A list of key-value pairs to associate with the investigation group. You can associate as many as 50 tags with an investigation group. To be able to associate tags when you create the investigation group, you must have the `cloudwatch:TagResource` permission.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
