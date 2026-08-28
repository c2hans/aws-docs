---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-fuotatask-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::FuotaTask Tag
<a name="aws-properties-iotwireless-fuotatask-tag"></a>

The tags to attach to the FUOTA task. Tags are metadata that you can use to manage a resource.

## Syntax
<a name="aws-properties-iotwireless-fuotatask-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-fuotatask-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iotwireless-fuotatask-tag-key)" : {{String}},
  "[Value](#cfn-iotwireless-fuotatask-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-fuotatask-tag-syntax.yaml"></a>

```
  [Key](#cfn-iotwireless-fuotatask-tag-key): {{String}}
  [Value](#cfn-iotwireless-fuotatask-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-fuotatask-tag-properties"></a>

`Key`  <a name="cfn-iotwireless-fuotatask-tag-key"></a>
The tag's key value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotwireless-fuotatask-tag-value"></a>
The tag's value.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
