---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationobjectstorage-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationObjectStorage Tag
<a name="aws-properties-datasync-locationobjectstorage-tag"></a>

Specifies the key-value pair that represents a tag that you want to add to the resource. Tags can help you manage, filter, and search for your resources. We recommend creating a name tag for your location.

## Syntax
<a name="aws-properties-datasync-locationobjectstorage-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationobjectstorage-tag-syntax.json"></a>

```
{
  "[Key](#cfn-datasync-locationobjectstorage-tag-key)" : {{String}},
  "[Value](#cfn-datasync-locationobjectstorage-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationobjectstorage-tag-syntax.yaml"></a>

```
  [Key](#cfn-datasync-locationobjectstorage-tag-key): {{String}}
  [Value](#cfn-datasync-locationobjectstorage-tag-value): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationobjectstorage-tag-properties"></a>

`Key`  <a name="cfn-datasync-locationobjectstorage-tag-key"></a>
The key for an AWS resource tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datasync-locationobjectstorage-tag-value"></a>
The value for an AWS resource tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:@/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
