---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-docdb-globalcluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DocDB::GlobalCluster
<a name="aws-resource-docdb-globalcluster"></a>

A data type representing an Amazon DocumentDB global cluster.

## Syntax
<a name="aws-resource-docdb-globalcluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-docdb-globalcluster-syntax.json"></a>

```
{
  "Type" : "AWS::DocDB::GlobalCluster",
  "Properties" : {
      "[DeletionProtection](#cfn-docdb-globalcluster-deletionprotection)" : {{Boolean}},
      "[Engine](#cfn-docdb-globalcluster-engine)" : {{String}},
      "[EngineVersion](#cfn-docdb-globalcluster-engineversion)" : {{String}},
      "[GlobalClusterIdentifier](#cfn-docdb-globalcluster-globalclusteridentifier)" : {{String}},
      "[SourceDBClusterIdentifier](#cfn-docdb-globalcluster-sourcedbclusteridentifier)" : {{String}},
      "[StorageEncrypted](#cfn-docdb-globalcluster-storageencrypted)" : {{Boolean}},
      "[Tags](#cfn-docdb-globalcluster-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-docdb-globalcluster-syntax.yaml"></a>

```
Type: AWS::DocDB::GlobalCluster
Properties:
  [DeletionProtection](#cfn-docdb-globalcluster-deletionprotection): {{Boolean}}
  [Engine](#cfn-docdb-globalcluster-engine): {{String}}
  [EngineVersion](#cfn-docdb-globalcluster-engineversion): {{String}}
  [GlobalClusterIdentifier](#cfn-docdb-globalcluster-globalclusteridentifier): {{String}}
  [SourceDBClusterIdentifier](#cfn-docdb-globalcluster-sourcedbclusteridentifier): {{String}}
  [StorageEncrypted](#cfn-docdb-globalcluster-storageencrypted): {{Boolean}}
  [Tags](#cfn-docdb-globalcluster-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-docdb-globalcluster-properties"></a>

`DeletionProtection`  <a name="cfn-docdb-globalcluster-deletionprotection"></a>
The deletion protection setting for the new global cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-docdb-globalcluster-engine"></a>
The Amazon DocumentDB database engine used by the global cluster.
*Required*: No
*Type*: String
*Allowed values*: `docdb`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EngineVersion`  <a name="cfn-docdb-globalcluster-engineversion"></a>
Indicates the database engine version.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GlobalClusterIdentifier`  <a name="cfn-docdb-globalcluster-globalclusteridentifier"></a>
Contains a user-supplied global cluster identifier. This identifier is the unique key that identifies a global cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceDBClusterIdentifier`  <a name="cfn-docdb-globalcluster-sourcedbclusteridentifier"></a>
The Amazon Resource Name (ARN) to use as the primary cluster of the global cluster. This parameter is optional.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageEncrypted`  <a name="cfn-docdb-globalcluster-storageencrypted"></a>
The storage encryption setting for the global cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-docdb-globalcluster-tags"></a>
The tags to be assigned to the Amazon DocumentDB resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-docdb-globalcluster-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-docdb-globalcluster-return-values"></a>

### Ref
<a name="aws-resource-docdb-globalcluster-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-docdb-globalcluster-return-values-fn--getatt"></a>

####
<a name="aws-resource-docdb-globalcluster-return-values-fn--getatt-fn--getatt"></a>

`GlobalClusterArn`  <a name="GlobalClusterArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the global cluster.

`GlobalClusterResourceId`  <a name="GlobalClusterResourceId-fn::getatt"></a>
The AWS Region-unique, immutable identifier for the global database cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS customer master key (CMK) for the cluster is accessed.
