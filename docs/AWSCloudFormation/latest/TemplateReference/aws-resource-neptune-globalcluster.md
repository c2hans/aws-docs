---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-neptune-globalcluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Neptune::GlobalCluster
<a name="aws-resource-neptune-globalcluster"></a>

The `AWS::Neptune::GlobalCluster` resource creates an Amazon Neptune global database spread across multiple AWS Regions. The global database contains a single primary cluster with read-write capability, and read-only secondary clusters that receive data from the primary cluster through high-speed replication performed by the Neptune storage subsystem.

**Note**
Currently, you can create this resource only in AWS Regions in which Amazon Neptune is supported.

When `DeletionPolicy` is set for the `AWS::Neptune::GlobalCluster` resource, it can not be deleted. The default behavior is to have no deletion protection. Before deletion, the primary and all secondary clusters must already be detached or deleted first. For more information about how CloudFormation deletes resources, see [DeletionPolicy Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

You can use `AWS::Neptune::GlobalCluster.DeletionProtection` to help guard against unintended deletion of your global database.

## Syntax
<a name="aws-resource-neptune-globalcluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-neptune-globalcluster-syntax.json"></a>

```
{
  "Type" : "AWS::Neptune::GlobalCluster",
  "Properties" : {
      "[DeletionProtection](#cfn-neptune-globalcluster-deletionprotection)" : {{Boolean}},
      "[Engine](#cfn-neptune-globalcluster-engine)" : {{String}},
      "[EngineVersion](#cfn-neptune-globalcluster-engineversion)" : {{String}},
      "[GlobalClusterIdentifier](#cfn-neptune-globalcluster-globalclusteridentifier)" : {{String}},
      "[SourceDBClusterIdentifier](#cfn-neptune-globalcluster-sourcedbclusteridentifier)" : {{String}},
      "[StorageEncrypted](#cfn-neptune-globalcluster-storageencrypted)" : {{Boolean}},
      "[Tags](#cfn-neptune-globalcluster-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-neptune-globalcluster-syntax.yaml"></a>

```
Type: AWS::Neptune::GlobalCluster
Properties:
  [DeletionProtection](#cfn-neptune-globalcluster-deletionprotection): {{Boolean}}
  [Engine](#cfn-neptune-globalcluster-engine): {{String}}
  [EngineVersion](#cfn-neptune-globalcluster-engineversion): {{String}}
  [GlobalClusterIdentifier](#cfn-neptune-globalcluster-globalclusteridentifier): {{String}}
  [SourceDBClusterIdentifier](#cfn-neptune-globalcluster-sourcedbclusteridentifier): {{String}}
  [StorageEncrypted](#cfn-neptune-globalcluster-storageencrypted): {{Boolean}}
  [Tags](#cfn-neptune-globalcluster-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-neptune-globalcluster-properties"></a>

`DeletionProtection`  <a name="cfn-neptune-globalcluster-deletionprotection"></a>
The deletion protection setting for the global database.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-neptune-globalcluster-engine"></a>
The Neptune database engine used by the global database.
*Required*: No
*Type*: String
*Allowed values*: `neptune`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EngineVersion`  <a name="cfn-neptune-globalcluster-engineversion"></a>
The Neptune engine version used by the global database. The minimum supported engine version is 1.2.0.0.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalClusterIdentifier`  <a name="cfn-neptune-globalcluster-globalclusteridentifier"></a>
Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database.
If it's not specified, then a random one will be automatically generated.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z][0-9A-Za-z-:._]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceDBClusterIdentifier`  <a name="cfn-neptune-globalcluster-sourcedbclusteridentifier"></a>
The Amazon Resource Name (ARN) of an existing Neptune DB cluster to use as the primary cluster of the new global database.
If you specify this property, the new global cluster inherits the engine version and storage-encryption settings of the source DB cluster, so the `Engine`, `EngineVersion`, and `StorageEncrypted` properties must not also be specified.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageEncrypted`  <a name="cfn-neptune-globalcluster-storageencrypted"></a>
The storage encryption setting for the global database.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-neptune-globalcluster-tags"></a>
The tags assigned to this global cluster.
*Required*: No
*Type*: Array of [Tag](aws-properties-neptune-globalcluster-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-neptune-globalcluster-return-values"></a>

### Ref
<a name="aws-resource-neptune-globalcluster-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
