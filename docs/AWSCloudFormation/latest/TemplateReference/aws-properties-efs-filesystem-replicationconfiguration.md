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
