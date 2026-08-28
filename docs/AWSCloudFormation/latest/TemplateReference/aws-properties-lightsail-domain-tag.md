---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-domain-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Domain Tag
<a name="aws-properties-lightsail-domain-tag"></a>

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).

## Syntax
<a name="aws-properties-lightsail-domain-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-domain-tag-syntax.json"></a>

```
{
  "[Key](#cfn-lightsail-domain-tag-key)" : {{String}},
  "[Value](#cfn-lightsail-domain-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-domain-tag-syntax.yaml"></a>

```
  [Key](#cfn-lightsail-domain-tag-key): {{String}}
  [Value](#cfn-lightsail-domain-tag-value): {{String}}
```

## Properties
<a name="aws-properties-lightsail-domain-tag-properties"></a>

`Key`  <a name="cfn-lightsail-domain-tag-key"></a>
The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: \+ - = . \_ : / @
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-lightsail-domain-tag-value"></a>
The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: \+ - = . \_ : / @
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
