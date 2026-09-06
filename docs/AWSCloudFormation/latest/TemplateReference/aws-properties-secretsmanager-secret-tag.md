---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-secretsmanager-secret-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecretsManager::Secret Tag
<a name="aws-properties-secretsmanager-secret-tag"></a>

A structure that contains information about a tag.

## Syntax
<a name="aws-properties-secretsmanager-secret-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-secretsmanager-secret-tag-syntax.json"></a>

```
{
  "[Key](#cfn-secretsmanager-secret-tag-key)" : {{String}},
  "[Value](#cfn-secretsmanager-secret-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-secretsmanager-secret-tag-syntax.yaml"></a>

```
  [Key](#cfn-secretsmanager-secret-tag-key): {{String}}
  [Value](#cfn-secretsmanager-secret-tag-value): {{String}}
```

## Properties
<a name="aws-properties-secretsmanager-secret-tag-properties"></a>

`Key`  <a name="cfn-secretsmanager-secret-tag-key"></a>
The key identifier, or name, of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-secretsmanager-secret-tag-value"></a>
The string value associated with the key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
