---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-efs-filesystem-replicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EFS::FileSystem ReplicationConfiguration
<a name="aws-properties-efs-filesystem-replicationconfiguration"></a>

Describes the replication configuration for a specific file system.

## Syntax
<a name="aws-properties-efs-filesystem-replicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-efs-filesystem-replicationconfiguration-syntax.json"></a>

```
{
  "[Destinations](#cfn-efs-filesystem-replicationconfiguration-destinations)" : {{[ ReplicationDestination, ... ]}}
}
```

### YAML
<a name="aws-properties-efs-filesystem-replicationconfiguration-syntax.yaml"></a>

```
  [Destinations](#cfn-efs-filesystem-replicationconfiguration-destinations): {{
    - ReplicationDestination}}
```

## Properties
<a name="aws-properties-efs-filesystem-replicationconfiguration-properties"></a>

`Destinations`  <a name="cfn-efs-filesystem-replicationconfiguration-destinations"></a>
An array of destination objects. Only one destination object is supported.
*Required*: No
*Type*: Array of [ReplicationDestination](aws-properties-efs-filesystem-replicationdestination.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
