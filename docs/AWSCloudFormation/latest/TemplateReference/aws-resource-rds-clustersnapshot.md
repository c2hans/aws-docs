---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-clustersnapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::ClusterSnapshot
<a name="aws-resource-rds-clustersnapshot"></a>

## Syntax
<a name="aws-resource-rds-clustersnapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-clustersnapshot-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::ClusterSnapshot",
  "Properties" : {
      "[DBClusterIdentifier](#cfn-rds-clustersnapshot-dbclusteridentifier)" : {{String}},
      "[DBClusterSnapshotIdentifier](#cfn-rds-clustersnapshot-dbclustersnapshotidentifier)" : {{String}},
      "[Tags](#cfn-rds-clustersnapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-clustersnapshot-syntax.yaml"></a>

```
Type: AWS::RDS::ClusterSnapshot
Properties:
  [DBClusterIdentifier](#cfn-rds-clustersnapshot-dbclusteridentifier): {{String}}
  [DBClusterSnapshotIdentifier](#cfn-rds-clustersnapshot-dbclustersnapshotidentifier): {{String}}
  [Tags](#cfn-rds-clustersnapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rds-clustersnapshot-properties"></a>

`DBClusterIdentifier`  <a name="cfn-rds-clustersnapshot-dbclusteridentifier"></a>
The identifier of the DB cluster to create a snapshot for. This parameter isn't case-sensitive.
Constraints:
+ Must match the identifier of an existing DBCluster.
Example: `my-cluster1`
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBClusterSnapshotIdentifier`  <a name="cfn-rds-clustersnapshot-dbclustersnapshotidentifier"></a>
The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.
Constraints:
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster1-snapshot1`
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-rds-clustersnapshot-tags"></a>
The tags to be assigned to the DB cluster snapshot.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-clustersnapshot-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rds-clustersnapshot-return-values"></a>

### Ref
<a name="aws-resource-rds-clustersnapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rds-clustersnapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-rds-clustersnapshot-return-values-fn--getatt-fn--getatt"></a>

`AllocatedStorage`  <a name="AllocatedStorage-fn::getatt"></a>
The allocated storage size of the DB cluster snapshot in gibibytes (GiB).

`AvailabilityZones`  <a name="AvailabilityZones-fn::getatt"></a>
The list of Availability Zones (AZs) where instances in the DB cluster snapshot can be restored.

`ClusterCreateTime`  <a name="ClusterCreateTime-fn::getatt"></a>
The time when the DB cluster was created, in Universal Coordinated Time (UTC).

`DbClusterResourceId`  <a name="DbClusterResourceId-fn::getatt"></a>
The resource ID of the DB cluster that this DB cluster snapshot was created from.

`DBClusterSnapshotArn`  <a name="DBClusterSnapshotArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the DB cluster snapshot.

`Engine`  <a name="Engine-fn::getatt"></a>
The name of the database engine for this DB cluster snapshot.

`EngineMode`  <a name="EngineMode-fn::getatt"></a>
The engine mode of the database engine for this DB cluster snapshot.

`EngineVersion`  <a name="EngineVersion-fn::getatt"></a>
The version of the database engine for this DB cluster snapshot.

`IAMDatabaseAuthenticationEnabled`  <a name="IAMDatabaseAuthenticationEnabled-fn::getatt"></a>
Indicates whether mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.

`KmsKeyId`  <a name="KmsKeyId-fn::getatt"></a>
If `StorageEncrypted` is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

`LicenseModel`  <a name="LicenseModel-fn::getatt"></a>
The license model information for this DB cluster snapshot.

`MasterUsername`  <a name="MasterUsername-fn::getatt"></a>
The master username for this DB cluster snapshot.

`Port`  <a name="Port-fn::getatt"></a>
The port that the DB cluster was listening on at the time of the snapshot.

`SnapshotCreateTime`  <a name="SnapshotCreateTime-fn::getatt"></a>
The time when the snapshot was taken, in Universal Coordinated Time (UTC).

`SnapshotType`  <a name="SnapshotType-fn::getatt"></a>
The type of the DB cluster snapshot.

`Status`  <a name="Status-fn::getatt"></a>
The status of this DB cluster snapshot. Valid statuses are the following:
+  `available`
+  `copying`
+  `creating`

`StorageEncrypted`  <a name="StorageEncrypted-fn::getatt"></a>
Indicates whether the DB cluster snapshot is encrypted.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The VPC ID associated with the DB cluster snapshot.
