---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-tablebucket-replicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucket ReplicationConfiguration
<a name="aws-properties-s3tables-tablebucket-replicationconfiguration"></a>

<a name="aws-properties-s3tables-tablebucket-replicationconfiguration-description"></a>The `ReplicationConfiguration` property type specifies Property description not available. for an [AWS::S3Tables::TableBucket](aws-resource-s3tables-tablebucket.md).

## Syntax
<a name="aws-properties-s3tables-tablebucket-replicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-tablebucket-replicationconfiguration-syntax.json"></a>

```
{
  "[Role](#cfn-s3tables-tablebucket-replicationconfiguration-role)" : {{String}},
  "[Rules](#cfn-s3tables-tablebucket-replicationconfiguration-rules)" : {{[ ReplicationRule, ... ]}}
}
```

### YAML
<a name="aws-properties-s3tables-tablebucket-replicationconfiguration-syntax.yaml"></a>

```
  [Role](#cfn-s3tables-tablebucket-replicationconfiguration-role): {{String}}
  [Rules](#cfn-s3tables-tablebucket-replicationconfiguration-rules): {{
    - ReplicationRule}}
```

## Properties
<a name="aws-properties-s3tables-tablebucket-replicationconfiguration-properties"></a>

`Role`  <a name="cfn-s3tables-tablebucket-replicationconfiguration-role"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-s3tables-tablebucket-replicationconfiguration-rules"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [ReplicationRule](aws-properties-s3tables-tablebucket-replicationrule.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
