---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-replicationconfiguration-replicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::ReplicationConfiguration ReplicationConfiguration
<a name="aws-properties-ecr-replicationconfiguration-replicationconfiguration"></a>

The replication configuration for a registry.

## Syntax
<a name="aws-properties-ecr-replicationconfiguration-replicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-replicationconfiguration-replicationconfiguration-syntax.json"></a>

```
{
  "[Rules](#cfn-ecr-replicationconfiguration-replicationconfiguration-rules)" : {{[ ReplicationRule, ... ]}}
}
```

### YAML
<a name="aws-properties-ecr-replicationconfiguration-replicationconfiguration-syntax.yaml"></a>

```
  [Rules](#cfn-ecr-replicationconfiguration-replicationconfiguration-rules): {{
    - ReplicationRule}}
```

## Properties
<a name="aws-properties-ecr-replicationconfiguration-replicationconfiguration-properties"></a>

`Rules`  <a name="cfn-ecr-replicationconfiguration-replicationconfiguration-rules"></a>
An array of objects representing the replication destinations and repository filters for a replication configuration.
*Required*: Yes
*Type*: Array of [ReplicationRule](aws-properties-ecr-replicationconfiguration-replicationrule.md)
*Minimum*: `0`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
