---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backupgateway-hypervisor-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BackupGateway::Hypervisor Tag
<a name="aws-properties-backupgateway-hypervisor-tag"></a>

A key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, and the following characters: \+ - = . \_ : /. Spaces are not allowed in tag values.

## Syntax
<a name="aws-properties-backupgateway-hypervisor-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backupgateway-hypervisor-tag-syntax.json"></a>

```
{
  "[Key](#cfn-backupgateway-hypervisor-tag-key)" : {{String}},
  "[Value](#cfn-backupgateway-hypervisor-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-backupgateway-hypervisor-tag-syntax.yaml"></a>

```
  [Key](#cfn-backupgateway-hypervisor-tag-key): {{String}}
  [Value](#cfn-backupgateway-hypervisor-tag-value): {{String}}
```

## Properties
<a name="aws-properties-backupgateway-hypervisor-tag-properties"></a>

`Key`  <a name="cfn-backupgateway-hypervisor-tag-key"></a>
The key part of a tag's key-value pair. The key can't start with `aws:`.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-backupgateway-hypervisor-tag-value"></a>
The value part of a tag's key-value pair.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\x00]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
