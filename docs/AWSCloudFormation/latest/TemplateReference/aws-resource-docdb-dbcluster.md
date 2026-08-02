---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-docdb-dbcluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DocDB::DBCluster
<a name="aws-resource-docdb-dbcluster"></a>

The `AWS::DocDB::DBCluster`Amazon DocumentDB (with MongoDB compatibility) resource describes a DBCluster. Amazon DocumentDB is a fully managed, MongoDB-compatible document database engine. For more information, see [DBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBCluster.html) in the *Amazon DocumentDB Developer Guide*.

## Syntax
<a name="aws-resource-docdb-dbcluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-docdb-dbcluster-syntax.json"></a>

```
{
  "Type" : "AWS::DocDB::DBCluster",
  "Properties" : {
      "[AvailabilityZones](#cfn-docdb-dbcluster-availabilityzones)" : {{[ String, ... ]}},
      "[BackupRetentionPeriod](#cfn-docdb-dbcluster-backupretentionperiod)" : {{Integer}},
      "[CopyTagsToSnapshot](#cfn-docdb-dbcluster-copytagstosnapshot)" : {{Boolean}},
      "[DBClusterIdentifier](#cfn-docdb-dbcluster-dbclusteridentifier)" : {{String}},
      "[DBClusterParameterGroupName](#cfn-docdb-dbcluster-dbclusterparametergroupname)" : {{String}},
      "[DBSubnetGroupName](#cfn-docdb-dbcluster-dbsubnetgroupname)" : {{String}},
      "[DeletionProtection](#cfn-docdb-dbcluster-deletionprotection)" : {{Boolean}},
      "[EnableCloudwatchLogsExports](#cfn-docdb-dbcluster-enablecloudwatchlogsexports)" : {{[ String, ... ]}},
      "[EngineVersion](#cfn-docdb-dbcluster-engineversion)" : {{String}},
      "[GlobalClusterIdentifier](#cfn-docdb-dbcluster-globalclusteridentifier)" : {{String}},
      "[KmsKeyId](#cfn-docdb-dbcluster-kmskeyid)" : {{String}},
      "[ManageMasterUserPassword](#cfn-docdb-dbcluster-managemasteruserpassword)" : {{Boolean}},
      "[MasterUsername](#cfn-docdb-dbcluster-masterusername)" : {{String}},
      "[MasterUserPassword](#cfn-docdb-dbcluster-masteruserpassword)" : {{String}},
      "[MasterUserSecretKmsKeyId](#cfn-docdb-dbcluster-masterusersecretkmskeyid)" : {{String}},
      "[NetworkType](#cfn-docdb-dbcluster-networktype)" : {{String}},
      "[Port](#cfn-docdb-dbcluster-port)" : {{Integer}},
      "[PreferredBackupWindow](#cfn-docdb-dbcluster-preferredbackupwindow)" : {{String}},
      "[PreferredMaintenanceWindow](#cfn-docdb-dbcluster-preferredmaintenancewindow)" : {{String}},
      "[RestoreToTime](#cfn-docdb-dbcluster-restoretotime)" : {{String}},
      "[RestoreType](#cfn-docdb-dbcluster-restoretype)" : {{String}},
      "[RotateMasterUserPassword](#cfn-docdb-dbcluster-rotatemasteruserpassword)" : {{Boolean}},
      "[ServerlessV2ScalingConfiguration](#cfn-docdb-dbcluster-serverlessv2scalingconfiguration)" : {{ServerlessV2ScalingConfiguration}},
      "[SnapshotIdentifier](#cfn-docdb-dbcluster-snapshotidentifier)" : {{String}},
      "[SourceDBClusterIdentifier](#cfn-docdb-dbcluster-sourcedbclusteridentifier)" : {{String}},
      "[StorageEncrypted](#cfn-docdb-dbcluster-storageencrypted)" : {{Boolean}},
      "[StorageType](#cfn-docdb-dbcluster-storagetype)" : {{String}},
      "[Tags](#cfn-docdb-dbcluster-tags)" : {{[ Tag, ... ]}},
      "[UseLatestRestorableTime](#cfn-docdb-dbcluster-uselatestrestorabletime)" : {{Boolean}},
      "[VpcSecurityGroupIds](#cfn-docdb-dbcluster-vpcsecuritygroupids)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-docdb-dbcluster-syntax.yaml"></a>

```
Type: AWS::DocDB::DBCluster
Properties:
  [AvailabilityZones](#cfn-docdb-dbcluster-availabilityzones): {{
    - String}}
  [BackupRetentionPeriod](#cfn-docdb-dbcluster-backupretentionperiod): {{Integer}}
  [CopyTagsToSnapshot](#cfn-docdb-dbcluster-copytagstosnapshot): {{Boolean}}
  [DBClusterIdentifier](#cfn-docdb-dbcluster-dbclusteridentifier): {{String}}
  [DBClusterParameterGroupName](#cfn-docdb-dbcluster-dbclusterparametergroupname): {{String}}
  [DBSubnetGroupName](#cfn-docdb-dbcluster-dbsubnetgroupname): {{String}}
  [DeletionProtection](#cfn-docdb-dbcluster-deletionprotection): {{Boolean}}
  [EnableCloudwatchLogsExports](#cfn-docdb-dbcluster-enablecloudwatchlogsexports): {{
    - String}}
  [EngineVersion](#cfn-docdb-dbcluster-engineversion): {{String}}
  [GlobalClusterIdentifier](#cfn-docdb-dbcluster-globalclusteridentifier): {{String}}
  [KmsKeyId](#cfn-docdb-dbcluster-kmskeyid): {{String}}
  [ManageMasterUserPassword](#cfn-docdb-dbcluster-managemasteruserpassword): {{Boolean}}
  [MasterUsername](#cfn-docdb-dbcluster-masterusername): {{String}}
  [MasterUserPassword](#cfn-docdb-dbcluster-masteruserpassword): {{String}}
  [MasterUserSecretKmsKeyId](#cfn-docdb-dbcluster-masterusersecretkmskeyid): {{String}}
  [NetworkType](#cfn-docdb-dbcluster-networktype): {{String}}
  [Port](#cfn-docdb-dbcluster-port): {{Integer}}
  [PreferredBackupWindow](#cfn-docdb-dbcluster-preferredbackupwindow): {{String}}
  [PreferredMaintenanceWindow](#cfn-docdb-dbcluster-preferredmaintenancewindow): {{String}}
  [RestoreToTime](#cfn-docdb-dbcluster-restoretotime): {{String}}
  [RestoreType](#cfn-docdb-dbcluster-restoretype): {{String}}
  [RotateMasterUserPassword](#cfn-docdb-dbcluster-rotatemasteruserpassword): {{Boolean}}
  [ServerlessV2ScalingConfiguration](#cfn-docdb-dbcluster-serverlessv2scalingconfiguration): {{
    ServerlessV2ScalingConfiguration}}
  [SnapshotIdentifier](#cfn-docdb-dbcluster-snapshotidentifier): {{String}}
  [SourceDBClusterIdentifier](#cfn-docdb-dbcluster-sourcedbclusteridentifier): {{String}}
  [StorageEncrypted](#cfn-docdb-dbcluster-storageencrypted): {{Boolean}}
  [StorageType](#cfn-docdb-dbcluster-storagetype): {{String}}
  [Tags](#cfn-docdb-dbcluster-tags): {{
    - Tag}}
  [UseLatestRestorableTime](#cfn-docdb-dbcluster-uselatestrestorabletime): {{Boolean}}
  [VpcSecurityGroupIds](#cfn-docdb-dbcluster-vpcsecuritygroupids): {{
    - String}}
```

## Properties
<a name="aws-resource-docdb-dbcluster-properties"></a>

`AvailabilityZones`  <a name="cfn-docdb-dbcluster-availabilityzones"></a>
A list of Amazon EC2 Availability Zones that instances in the cluster can be created in.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BackupRetentionPeriod`  <a name="cfn-docdb-dbcluster-backupretentionperiod"></a>
The number of days for which automated backups are retained. You must specify a minimum value of 1.
Default: 1
Constraints:
+ Must be a value from 1 to 35.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CopyTagsToSnapshot`  <a name="cfn-docdb-dbcluster-copytagstosnapshot"></a>
Set to `true` to copy all tags from the source cluster snapshot to the target cluster snapshot, and otherwise `false`. The default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBClusterIdentifier`  <a name="cfn-docdb-dbcluster-dbclusteridentifier"></a>
The cluster identifier. This parameter is stored as a lowercase string.
Constraints:
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBClusterParameterGroupName`  <a name="cfn-docdb-dbcluster-dbclusterparametergroupname"></a>
The name of the cluster parameter group to associate with this cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBSubnetGroupName`  <a name="cfn-docdb-dbcluster-dbsubnetgroupname"></a>
A subnet group to associate with this cluster.
Constraints: Must match the name of an existing `DBSubnetGroup`. Must not be default.
Example: `mySubnetgroup`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeletionProtection`  <a name="cfn-docdb-dbcluster-deletionprotection"></a>
Protects clusters from being accidentally deleted. If enabled, the cluster cannot be deleted unless it is modified and `DeletionProtection` is disabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableCloudwatchLogsExports`  <a name="cfn-docdb-dbcluster-enablecloudwatchlogsexports"></a>
The list of log types that need to be enabled for exporting to Amazon CloudWatch Logs. You can enable audit logs or profiler logs. For more information, see [Auditing Amazon DocumentDB Events](https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html) and [Profiling Amazon DocumentDB Operations](https://docs.aws.amazon.com/documentdb/latest/developerguide/profiling.html).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EngineVersion`  <a name="cfn-docdb-dbcluster-engineversion"></a>
The version number of the database engine to use. The `--engine-version` will default to the latest major engine version. For production workloads, we recommend explicitly declaring this parameter with the intended major engine version.
If you intend to trigger an in-place upgrade, please refer to [Amazon DocumentDB in-place major version upgrade](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-mvu.html). Note that for an in-place engine version upgrade, you need to remove other cluster properties changes (e.g. SecurityGroupId) from the CFN template.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalClusterIdentifier`  <a name="cfn-docdb-dbcluster-globalclusteridentifier"></a>
The cluster identifier of the new global cluster.
*Required*: No
*Type*: String
*Pattern*: `[A-Za-z][0-9A-Za-z-:._]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-docdb-dbcluster-kmskeyid"></a>
The AWS KMS key identifier for an encrypted cluster.
The AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are creating a cluster using the same AWS account that owns the AWS KMS encryption key that is used to encrypt the new cluster, you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.
If an encryption key is not specified in `KmsKeyId`:
+ If the `StorageEncrypted` parameter is `true`, Amazon DocumentDB uses your default encryption key.
AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Regions.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManageMasterUserPassword`  <a name="cfn-docdb-dbcluster-managemasteruserpassword"></a>
Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.
Constraint: You can't manage the master user password with Amazon Web Services Secrets Manager if `MasterUserPassword` is specified.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MasterUsername`  <a name="cfn-docdb-dbcluster-masterusername"></a>
The name of the master user for the cluster.
Constraints:
+ Must be from 1 to 63 letters or numbers.
+ The first character must be a letter.
+ Cannot be a reserved word for the chosen database engine.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MasterUserPassword`  <a name="cfn-docdb-dbcluster-masteruserpassword"></a>
The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@).
Constraints: Must contain from 8 to 100 characters.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MasterUserSecretKmsKeyId`  <a name="cfn-docdb-dbcluster-masterusersecretkmskeyid"></a>
The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager. This setting is valid only if the master user password is managed by Amazon DocumentDB in Amazon Web Services Secrets Manager for the DB cluster.
The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.
If you don't specify `MasterUserSecretKmsKeyId`, then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.
There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkType`  <a name="cfn-docdb-dbcluster-networktype"></a>
The network type of the cluster.
The network type is determined by the `DBSubnetGroup` specified for the cluster. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).
For more information, see [DocumentDB clusters in a VPC](https://docs.aws.amazon.com/documentdb/latest/devguide/vpc-clusters.html) in the Amazon DocumentDB Developer Guide.
Valid Values: `IPV4` \| `DUAL`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-docdb-dbcluster-port"></a>
Specifies the port that the database engine is listening on.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredBackupWindow`  <a name="cfn-docdb-dbcluster-preferredbackupwindow"></a>
The daily time range during which automated backups are created if automated backups are enabled using the `BackupRetentionPeriod` parameter.
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region.
Constraints:
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredMaintenanceWindow`  <a name="cfn-docdb-dbcluster-preferredmaintenancewindow"></a>
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
Format: `ddd:hh24:mi-ddd:hh24:mi`
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
Constraints: Minimum 30-minute window.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestoreToTime`  <a name="cfn-docdb-dbcluster-restoretotime"></a>
The date and time to restore the cluster to.
Valid values: A time in Universal Coordinated Time (UTC) format.
Constraints:
+ Must be before the latest restorable time for the instance.
+ Must be specified if the `UseLatestRestorableTime` parameter is not provided.
+ Cannot be specified if the `UseLatestRestorableTime` parameter is `true`.
+ Cannot be specified if the `RestoreType` parameter is `copy-on-write`.
Example: `2015-03-07T23:45:00Z`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestoreType`  <a name="cfn-docdb-dbcluster-restoretype"></a>
The type of restore to be performed. You can specify one of the following values:
+ `full-copy` - The new DB cluster is restored as a full copy of the source DB cluster.
+ `copy-on-write` - The new DB cluster is restored as a clone of the source DB cluster.
Constraints: You can't specify `copy-on-write` if the engine version of the source DB cluster is earlier than 1.11.
If you don't specify a `RestoreType` value, then the new DB cluster is restored as a full copy of the source DB cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RotateMasterUserPassword`  <a name="cfn-docdb-dbcluster-rotatemasteruserpassword"></a>
Specifies whether to rotate the secret managed by Amazon Web Services Secrets Manager for the master user password.
This setting is valid only if the master user password is managed by Amazon DocumentDB in Amazon Web Services Secrets Manager for the cluster. The secret value contains the updated password.
Constraint: You must apply the change immediately when rotating the master user password.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerlessV2ScalingConfiguration`  <a name="cfn-docdb-dbcluster-serverlessv2scalingconfiguration"></a>
Contains the scaling configuration of an Amazon DocumentDB Serverless cluster.
*Required*: No
*Type*: [ServerlessV2ScalingConfiguration](aws-properties-docdb-dbcluster-serverlessv2scalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotIdentifier`  <a name="cfn-docdb-dbcluster-snapshotidentifier"></a>
The identifier for the snapshot or cluster snapshot to restore from.
You can use either the name or the Amazon Resource Name (ARN) to specify a cluster snapshot. However, you can use only the ARN to specify a snapshot.
Constraints:
+ Must match the identifier of an existing snapshot.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceDBClusterIdentifier`  <a name="cfn-docdb-dbcluster-sourcedbclusteridentifier"></a>
The identifier of the source cluster from which to restore.
Constraints:
+ Must match the identifier of an existing `DBCluster`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageEncrypted`  <a name="cfn-docdb-dbcluster-storageencrypted"></a>
Specifies whether the cluster is encrypted.
If you specify `SourceDBClusterIdentifier` or `SnapshotIdentifier` and don’t specify `StorageEncrypted`, the encryption property is inherited from the source cluster or snapshot (unless `KMSKeyId` is specified, in which case the restored cluster will be encrypted with that KMS key). If the source is encrypted and `StorageEncrypted` is specified to be true, the restored cluster will be encrypted (if you want to use a different KMS key, specify the `KMSKeyId` property as well). If the source is unencrypted and `StorageEncrypted` is specified to be true, then the `KMSKeyId` property must be specified. If the source is encrypted, don’t specify `StorageEncrypted` to be false as opting out of encryption is not allowed.
*Required*: Conditional
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageType`  <a name="cfn-docdb-dbcluster-storagetype"></a>
The storage type to associate with the DB cluster.
For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the *Amazon DocumentDB Developer Guide*.
Valid values for storage type - `standard | iopt1`
Default value is `standard `
When you create an Amazon DocumentDB cluster with the storage type set to `iopt1`, the storage type is returned in the response. The storage type isn't returned when you set it to `standard`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-docdb-dbcluster-tags"></a>
The tags to be assigned to the cluster.
*Required*: No
*Type*: Array of [Tag](aws-properties-docdb-dbcluster-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseLatestRestorableTime`  <a name="cfn-docdb-dbcluster-uselatestrestorabletime"></a>
A value that is set to `true` to restore the cluster to the latest restorable backup time, and `false` otherwise.
Default: `false`
Constraints: Cannot be specified if the `RestoreToTime` parameter is provided.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcSecurityGroupIds`  <a name="cfn-docdb-dbcluster-vpcsecuritygroupids"></a>
A list of EC2 VPC security groups to associate with this cluster.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-docdb-dbcluster-return-values"></a>

### Ref
<a name="aws-resource-docdb-dbcluster-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the DBClusterIdentifier, such as `mycluster`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-docdb-dbcluster-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-docdb-dbcluster-return-values-fn--getatt-fn--getatt"></a>

`ClusterResourceId`  <a name="ClusterResourceId-fn::getatt"></a>
The resource id for the cluster; for example: `cluster-ABCD1234EFGH5678IJKL90MNOP`. The cluster ID uniquely identifies the cluster and is used in things like IAM authentication policies.

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The connection endpoint for the cluster, such as `sample-cluster.cluster-cozrlsfrcjoc.us-east-1.docdb.amazonaws.com`.

`Port`  <a name="Port-fn::getatt"></a>
The port number on which the cluster accepts connections. For example: `27017`.

`ReadEndpoint`  <a name="ReadEndpoint-fn::getatt"></a>
The reader endpoint for the cluster. For example: `sample-cluster.cluster-ro-cozrlsfrcjoc.us-east-1.docdb.amazonaws.com`.

## Examples
<a name="aws-resource-docdb-dbcluster--examples"></a>

###
<a name="aws-resource-docdb-dbcluster--examples--"></a>

#### JSON
<a name="aws-resource-docdb-dbcluster--examples----json"></a>

```
{
   "AWSTemplateFormatVersion" : "2010-09-09",
   "Resources" : {
      "myDBInstance" : {
         "Type" : "AWS::DocDB::DBCluster",
         "Properties" : {
            "BackupRetentionPeriod" : 8,
            "DBClusterIdentifier" : "sample-cluster",
            "DBClusterParameterGroupName" : "default.docdb3.6",
            "DBSubnetGroupName" : "default",
            "KmsKeyId" : "your-kms-key-id",
            "MasterUsername" : "your-master-username",
            "MasterUserPassword" : "your-master-user-password",
            "Port" : "27017",
            "PreferredBackupWindow" : "07:34-08:04",
            "PreferredMaintenanceWindow" : "sat:04:51-sat:05:21",
            "SnapshotIdentifier" : "sample-cluster-snapshot-id",
            "StorageEncrypted" : true,
            "Tags" : [ {"Key" : "String", "Value" : "String"} ]
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-docdb-dbcluster--examples----yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
   myDBInstance:
      Type: "AWS::DocDB::DBCluster"
      Properties:
         BackupRetentionPeriod : 8
         DBClusterIdentifier : "sample-cluster"
         DBClusterParameterGroupName : "default.docdb3.6"
         DBSubnetGroupName : "default"
         KmsKeyId : "your-kms-key-id"
         MasterUsername : "your-master-username"
         MasterUserPassword : "your-master-user-password"
         Port : "27017"
         PreferredBackupWindow : "07:34-08:04"
         PreferredMaintenanceWindow : "sat:04:51-sat:05:21"
         SnapshotIdentifier : "sample-cluster-snapshot-id"
         StorageEncrypted : true
         Tags:
            -
               Key: "String"
               Value: "String"
```

## See also
<a name="aws-resource-docdb-dbcluster--seealso"></a>
+  [DBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBCluster.html)
+  [CreateDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBCluster.html)
+  [DeleteDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DeleteDBCluster.html)
+  [DescribeDBClusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBClusters.html)
+  [ModifyDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyDBCluster.html)
