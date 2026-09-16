---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-snapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::Snapshot
<a name="aws-resource-redshift-snapshot"></a>

Describes a snapshot.

## Syntax
<a name="aws-resource-redshift-snapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshift-snapshot-syntax.json"></a>

```
{
  "Type" : "AWS::Redshift::Snapshot",
  "Properties" : {
      "[ClusterIdentifier](#cfn-redshift-snapshot-clusteridentifier)" : {{String}},
      "[ManualSnapshotRetentionPeriod](#cfn-redshift-snapshot-manualsnapshotretentionperiod)" : {{Integer}},
      "[SnapshotIdentifier](#cfn-redshift-snapshot-snapshotidentifier)" : {{String}},
      "[Tags](#cfn-redshift-snapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-redshift-snapshot-syntax.yaml"></a>

```
Type: AWS::Redshift::Snapshot
Properties:
  [ClusterIdentifier](#cfn-redshift-snapshot-clusteridentifier): {{String}}
  [ManualSnapshotRetentionPeriod](#cfn-redshift-snapshot-manualsnapshotretentionperiod): {{Integer}}
  [SnapshotIdentifier](#cfn-redshift-snapshot-snapshotidentifier): {{String}}
  [Tags](#cfn-redshift-snapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-redshift-snapshot-properties"></a>

`ClusterIdentifier`  <a name="cfn-redshift-snapshot-clusteridentifier"></a>
The identifier of the cluster for which the snapshot was taken.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManualSnapshotRetentionPeriod`  <a name="cfn-redshift-snapshot-manualsnapshotretentionperiod"></a>
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `3653`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotIdentifier`  <a name="cfn-redshift-snapshot-snapshotidentifier"></a>
The snapshot identifier that is provided in the request.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-redshift-snapshot-tags"></a>
The list of tags for the cluster snapshot.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshift-snapshot-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-redshift-snapshot-return-values"></a>

### Ref
<a name="aws-resource-redshift-snapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-redshift-snapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-redshift-snapshot-return-values-fn--getatt-fn--getatt"></a>

`AvailabilityZone`  <a name="AvailabilityZone-fn::getatt"></a>
The Availability Zone in which the cluster was created.

`ClusterCreateTime`  <a name="ClusterCreateTime-fn::getatt"></a>
The time (UTC) when the cluster was originally created.

`ClusterVersion`  <a name="ClusterVersion-fn::getatt"></a>
The version ID of the Amazon Redshift engine that is running on the cluster.

`DBName`  <a name="DBName-fn::getatt"></a>
The name of the database that was created when the cluster was created.

`Encrypted`  <a name="Encrypted-fn::getatt"></a>
If `true`, the data in the snapshot is encrypted at rest.

`EncryptedWithHSM`  <a name="EncryptedWithHSM-fn::getatt"></a>
A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. `true` indicates that the data is encrypted using HSM keys.

`EngineFullVersion`  <a name="EngineFullVersion-fn::getatt"></a>
The cluster version of the cluster used to create the snapshot. For example, 1.0.15503.

`EnhancedVpcRouting`  <a name="EnhancedVpcRouting-fn::getatt"></a>
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.
If this option is `true`, enhanced VPC routing is enabled.
Default: false

`KmsKeyId`  <a name="KmsKeyId-fn::getatt"></a>
The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.

`MaintenanceTrackName`  <a name="MaintenanceTrackName-fn::getatt"></a>
The name of the maintenance track for the snapshot.

`MasterUsername`  <a name="MasterUsername-fn::getatt"></a>
The admin user name for the cluster.

`NodeType`  <a name="NodeType-fn::getatt"></a>
The node type of the nodes in the cluster.

`NumberOfNodes`  <a name="NumberOfNodes-fn::getatt"></a>
The number of nodes in the cluster.

`OwnerAccount`  <a name="OwnerAccount-fn::getatt"></a>
For manual snapshots, the AWS account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.

`Port`  <a name="Port-fn::getatt"></a>
The port that the cluster is listening on.

`SnapshotArn`  <a name="SnapshotArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the snapshot.

`SnapshotCreateTime`  <a name="SnapshotCreateTime-fn::getatt"></a>
The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.

`SnapshotType`  <a name="SnapshotType-fn::getatt"></a>
The snapshot type. Snapshots created using CreateClusterSnapshot and CopyClusterSnapshot are of type "manual".

`Status`  <a name="Status-fn::getatt"></a>
The snapshot status. The value of the status depends on the API operation used:
+ CreateClusterSnapshot and CopyClusterSnapshot returns status as "creating".
+ DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
+ DeleteClusterSnapshot returns status as "deleted".

`VpcId`  <a name="VpcId-fn::getatt"></a>
The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.
