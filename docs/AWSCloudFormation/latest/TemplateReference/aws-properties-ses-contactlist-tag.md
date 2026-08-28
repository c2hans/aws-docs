---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-contactlist-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ContactList Tag
<a name="aws-properties-ses-contactlist-tag"></a>

A tag is a label that you optionally define and associate with a resource, such as a contact list. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.

## Syntax
<a name="aws-properties-ses-contactlist-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-contactlist-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ses-contactlist-tag-key)" : {{String}},
  "[Value](#cfn-ses-contactlist-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-contactlist-tag-syntax.yaml"></a>

```
  [Key](#cfn-ses-contactlist-tag-key): {{String}}
  [Value](#cfn-ses-contactlist-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ses-contactlist-tag-properties"></a>

`Key`  <a name="cfn-ses-contactlist-tag-key"></a>
One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ses-contactlist-tag-value"></a>
The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don't want a resource to have a specific tag value, don't specify a value for this parameter. If you don't specify a value, Amazon SES sets the value to an empty string.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
