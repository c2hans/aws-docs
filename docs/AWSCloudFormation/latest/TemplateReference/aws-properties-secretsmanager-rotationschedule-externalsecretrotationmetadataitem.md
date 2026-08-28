---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-secretsmanager-rotationschedule-externalsecretrotationmetadataitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecretsManager::RotationSchedule ExternalSecretRotationMetadataItem
<a name="aws-properties-secretsmanager-rotationschedule-externalsecretrotationmetadataitem"></a>

The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information, see [Managed external secret partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).

## Syntax
<a name="aws-properties-secretsmanager-rotationschedule-externalsecretrotationmetadataitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-secretsmanager-rotationschedule-externalsecretrotationmetadataitem-syntax.json"></a>

```
{
  "[Key](#cfn-secretsmanager-rotationschedule-externalsecretrotationmetadataitem-key)" : {{String}},
  "[Value](#cfn-secretsmanager-rotationschedule-externalsecretrotationmetadataitem-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-secretsmanager-rotationschedule-externalsecretrotationmetadataitem-syntax.yaml"></a>

```
  [Key](#cfn-secretsmanager-rotationschedule-externalsecretrotationmetadataitem-key): {{String}}
  [Value](#cfn-secretsmanager-rotationschedule-externalsecretrotationmetadataitem-value): {{String}}
```

## Properties
<a name="aws-properties-secretsmanager-rotationschedule-externalsecretrotationmetadataitem-properties"></a>

`Key`  <a name="cfn-secretsmanager-rotationschedule-externalsecretrotationmetadataitem-key"></a>
The key that identifies the item.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-secretsmanager-rotationschedule-externalsecretrotationmetadataitem-value"></a>
The value of the specified item.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
