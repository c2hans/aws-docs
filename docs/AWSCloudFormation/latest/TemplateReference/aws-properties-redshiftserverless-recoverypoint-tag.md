---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshiftserverless-recoverypoint-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::RecoveryPoint Tag
<a name="aws-properties-redshiftserverless-recoverypoint-tag"></a>

A map of key-value pairs.

## Syntax
<a name="aws-properties-redshiftserverless-recoverypoint-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshiftserverless-recoverypoint-tag-syntax.json"></a>

```
{
  "[Key](#cfn-redshiftserverless-recoverypoint-tag-key)" : {{String}},
  "[Value](#cfn-redshiftserverless-recoverypoint-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshiftserverless-recoverypoint-tag-syntax.yaml"></a>

```
  [Key](#cfn-redshiftserverless-recoverypoint-tag-key): {{String}}
  [Value](#cfn-redshiftserverless-recoverypoint-tag-value): {{String}}
```

## Properties
<a name="aws-properties-redshiftserverless-recoverypoint-tag-properties"></a>

`Key`  <a name="cfn-redshiftserverless-recoverypoint-tag-key"></a>
The key to use in the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-redshiftserverless-recoverypoint-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
