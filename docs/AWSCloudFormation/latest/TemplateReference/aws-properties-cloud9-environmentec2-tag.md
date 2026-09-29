---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloud9-environmentec2-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cloud9::EnvironmentEC2 Tag
<a name="aws-properties-cloud9-environmentec2-tag"></a>

Metadata that is associated with AWS resources. In particular, a name-value pair that can be associated with an AWS Cloud9 development environment. There are two types of tags: *user tags* and *system tags*. A user tag is created by the user. A system tag is automatically created by AWS services. A system tag is prefixed with `"aws:"` and cannot be modified by the user.

## Syntax
<a name="aws-properties-cloud9-environmentec2-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloud9-environmentec2-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cloud9-environmentec2-tag-key)" : {{String}},
  "[Value](#cfn-cloud9-environmentec2-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloud9-environmentec2-tag-syntax.yaml"></a>

```
  [Key](#cfn-cloud9-environmentec2-tag-key): {{String}}
  [Value](#cfn-cloud9-environmentec2-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cloud9-environmentec2-tag-properties"></a>

`Key`  <a name="cfn-cloud9-environmentec2-tag-key"></a>
The **name** part of a tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloud9-environmentec2-tag-value"></a>
The **value** part of a tag.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
