---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-runcommandtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule RunCommandTarget
<a name="aws-properties-events-rule-runcommandtarget"></a>

Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each `RunCommandTarget` block can include only one key, but this key may specify multiple values.

## Syntax
<a name="aws-properties-events-rule-runcommandtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-runcommandtarget-syntax.json"></a>

```
{
  "[Key](#cfn-events-rule-runcommandtarget-key)" : {{String}},
  "[Values](#cfn-events-rule-runcommandtarget-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-events-rule-runcommandtarget-syntax.yaml"></a>

```
  [Key](#cfn-events-rule-runcommandtarget-key): {{String}}
  [Values](#cfn-events-rule-runcommandtarget-values): {{
    - String}}
```

## Properties
<a name="aws-properties-events-rule-runcommandtarget-properties"></a>

`Key`  <a name="cfn-events-rule-runcommandtarget-key"></a>
Can be either `tag:`*tag-key* or `InstanceIds`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-events-rule-runcommandtarget-values"></a>
If `Key` is `tag:`*tag-key*, `Values` is a list of tag values. If `Key` is `InstanceIds`, `Values` is a list of Amazon EC2 instance IDs.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
