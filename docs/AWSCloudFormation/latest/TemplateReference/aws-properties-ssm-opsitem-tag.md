---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-opsitem-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::OpsItem Tag
<a name="aws-properties-ssm-opsitem-tag"></a>

Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In AWS Systems Manager, you can apply tags to Systems Manager documents (SSM documents), managed nodes, maintenance windows, parameters, patch baselines, OpsItems, and OpsMetadata.

## Syntax
<a name="aws-properties-ssm-opsitem-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-opsitem-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ssm-opsitem-tag-key)" : {{String}},
  "[Value](#cfn-ssm-opsitem-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssm-opsitem-tag-syntax.yaml"></a>

```
  [Key](#cfn-ssm-opsitem-tag-key): {{String}}
  [Value](#cfn-ssm-opsitem-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ssm-opsitem-tag-properties"></a>

`Key`  <a name="cfn-ssm-opsitem-tag-key"></a>
The name of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ssm-opsitem-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
