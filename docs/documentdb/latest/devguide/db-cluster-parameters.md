---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/db-cluster-parameters.html
---

# Amazon DocumentDB cluster settings
<a name="db-cluster-parameters"></a>

When you create or modify a cluster, it is important to understand which parameters are immutable and which are modifiable after the cluster has been created. The following table lists all the settings, or parameters, that are specific to a cluster. As specified in the table, some are modifiable, others are not.

**Note**
These settings should not be confused with Amazon DocumentDB cluster parameter groups and their parameters. For more information about cluster parameter groups, see [Managing Amazon DocumentDB cluster parameter groups](cluster_parameter_groups.md).

| Parameter | Modifiable | Notes |
| --- | --- | --- |
| DBClusterIdentifier | Yes | Naming constraints:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/db-cluster-parameters.html) |
| Engine | No | Must be docdb. |
| BackupRetentionPeriod | Yes | Must be between [1-35] days. |
| DBClusterParameterGroupName | Yes | Naming constraints:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/db-cluster-parameters.html) |
| DBSubnetGroupName | No | After a cluster has been created, you cannot modify the cluster's subnet. |
| EngineVersion | No | Value can be 5.0.0 (default), 4.0.0, or 3.6.0. |
| KmsKeyId | No | If you choose to encrypt your cluster, you cannot change the AWS KMS key that you used to encrypt your cluster. |
| MasterUsername | No | After a cluster has been created, you cannot modify the `MasterUsername`.<br />Naming constraints:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/db-cluster-parameters.html) |
| MasterUserPassword | Yes | Constraints:[See the AWS documentation website for more details](http://docs.aws.amazon.com/documentdb/latest/devguide/db-cluster-parameters.html) |
| Port | Yes | The port number applies to all instances in the cluster. |
| PreferredBackupWindow | Yes |  |
| PreferredMaintenanceWindow | Yes |  |
| StorageEncrypted | No | If you choose to encrypt your cluster, it cannot be unencrypted. |
| StorageType | Yes | The storage type for the DB cluster: Standard (`standard`) or I/O-Optimized (`iopt1`).<br />Default: `standard`<br />This parameter can be configured with `CreateDBCluster` and `ModifyDBCluster`.<br />For more information, see [Amazon DocumentDB cluster storage configurations](db-cluster-storage-configs.md). |
| Tags | Yes |  |
| VpcSecurityGroupIds | No | After a cluster has been created, you cannot modify the VPC that the cluster resides in. |
