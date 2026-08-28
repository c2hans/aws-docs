---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-globalaccelerator-crossaccountattachment-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GlobalAccelerator::CrossAccountAttachment Tag
<a name="aws-properties-globalaccelerator-crossaccountattachment-tag"></a>

A complex type that contains a `Tag` key and `Tag` value.

## Syntax
<a name="aws-properties-globalaccelerator-crossaccountattachment-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-globalaccelerator-crossaccountattachment-tag-syntax.json"></a>

```
{
  "[Key](#cfn-globalaccelerator-crossaccountattachment-tag-key)" : {{String}},
  "[Value](#cfn-globalaccelerator-crossaccountattachment-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-globalaccelerator-crossaccountattachment-tag-syntax.yaml"></a>

```
  [Key](#cfn-globalaccelerator-crossaccountattachment-tag-key): {{String}}
  [Value](#cfn-globalaccelerator-crossaccountattachment-tag-value): {{String}}
```

## Properties
<a name="aws-properties-globalaccelerator-crossaccountattachment-tag-properties"></a>

`Key`  <a name="cfn-globalaccelerator-crossaccountattachment-tag-key"></a>
A string that contains a `Tag` key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-globalaccelerator-crossaccountattachment-tag-value"></a>
A string that contains a `Tag` value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
