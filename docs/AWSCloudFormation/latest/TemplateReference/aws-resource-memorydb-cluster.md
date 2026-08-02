---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-memorydb-cluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::Cluster
<a name="aws-resource-memorydb-cluster"></a>

Specifies a cluster. All nodes in the cluster run the same protocol-compliant engine software.

## Syntax
<a name="aws-resource-memorydb-cluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-memorydb-cluster-syntax.json"></a>

```
{
  "Type" : "AWS::MemoryDB::Cluster",
  "Properties" : {
      "[ACLName](#cfn-memorydb-cluster-aclname)" : {{String}},
      "[AutoMinorVersionUpgrade](#cfn-memorydb-cluster-autominorversionupgrade)" : {{Boolean}},
      "[ClusterEndpoint](#cfn-memorydb-cluster-clusterendpoint)" : {{Endpoint}},
      "[ClusterName](#cfn-memorydb-cluster-clustername)" : {{String}},
      "[DataTiering](#cfn-memorydb-cluster-datatiering)" : {{String}},
      "[Description](#cfn-memorydb-cluster-description)" : {{String}},
      "[Engine](#cfn-memorydb-cluster-engine)" : {{String}},
      "[EngineVersion](#cfn-memorydb-cluster-engineversion)" : {{String}},
      "[FinalSnapshotName](#cfn-memorydb-cluster-finalsnapshotname)" : {{String}},
      "[IpDiscovery](#cfn-memorydb-cluster-ipdiscovery)" : {{String}},
      "[KmsKeyId](#cfn-memorydb-cluster-kmskeyid)" : {{String}},
      "[MaintenanceWindow](#cfn-memorydb-cluster-maintenancewindow)" : {{String}},
      "[MultiRegionClusterName](#cfn-memorydb-cluster-multiregionclustername)" : {{String}},
      "[NetworkType](#cfn-memorydb-cluster-networktype)" : {{String}},
      "[NodeType](#cfn-memorydb-cluster-nodetype)" : {{String}},
      "[NumReplicasPerShard](#cfn-memorydb-cluster-numreplicaspershard)" : {{Integer}},
      "[NumShards](#cfn-memorydb-cluster-numshards)" : {{Integer}},
      "[ParameterGroupName](#cfn-memorydb-cluster-parametergroupname)" : {{String}},
      "[Port](#cfn-memorydb-cluster-port)" : {{Integer}},
      "[SecurityGroupIds](#cfn-memorydb-cluster-securitygroupids)" : {{[ String, ... ]}},
      "[SnapshotArns](#cfn-memorydb-cluster-snapshotarns)" : {{[ String, ... ]}},
      "[SnapshotName](#cfn-memorydb-cluster-snapshotname)" : {{String}},
      "[SnapshotRetentionLimit](#cfn-memorydb-cluster-snapshotretentionlimit)" : {{Integer}},
      "[SnapshotWindow](#cfn-memorydb-cluster-snapshotwindow)" : {{String}},
      "[SnsTopicArn](#cfn-memorydb-cluster-snstopicarn)" : {{String}},
      "[SnsTopicStatus](#cfn-memorydb-cluster-snstopicstatus)" : {{String}},
      "[SubnetGroupName](#cfn-memorydb-cluster-subnetgroupname)" : {{String}},
      "[Tags](#cfn-memorydb-cluster-tags)" : {{[ Tag, ... ]}},
      "[TLSEnabled](#cfn-memorydb-cluster-tlsenabled)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-memorydb-cluster-syntax.yaml"></a>

```
Type: AWS::MemoryDB::Cluster
Properties:
  [ACLName](#cfn-memorydb-cluster-aclname): {{String}}
  [AutoMinorVersionUpgrade](#cfn-memorydb-cluster-autominorversionupgrade): {{Boolean}}
  [ClusterEndpoint](#cfn-memorydb-cluster-clusterendpoint): {{
    Endpoint}}
  [ClusterName](#cfn-memorydb-cluster-clustername): {{String}}
  [DataTiering](#cfn-memorydb-cluster-datatiering): {{String}}
  [Description](#cfn-memorydb-cluster-description): {{String}}
  [Engine](#cfn-memorydb-cluster-engine): {{String}}
  [EngineVersion](#cfn-memorydb-cluster-engineversion): {{String}}
  [FinalSnapshotName](#cfn-memorydb-cluster-finalsnapshotname): {{String}}
  [IpDiscovery](#cfn-memorydb-cluster-ipdiscovery): {{String}}
  [KmsKeyId](#cfn-memorydb-cluster-kmskeyid): {{String}}
  [MaintenanceWindow](#cfn-memorydb-cluster-maintenancewindow): {{String}}
  [MultiRegionClusterName](#cfn-memorydb-cluster-multiregionclustername): {{String}}
  [NetworkType](#cfn-memorydb-cluster-networktype): {{String}}
  [NodeType](#cfn-memorydb-cluster-nodetype): {{String}}
  [NumReplicasPerShard](#cfn-memorydb-cluster-numreplicaspershard): {{Integer}}
  [NumShards](#cfn-memorydb-cluster-numshards): {{Integer}}
  [ParameterGroupName](#cfn-memorydb-cluster-parametergroupname): {{String}}
  [Port](#cfn-memorydb-cluster-port): {{Integer}}
  [SecurityGroupIds](#cfn-memorydb-cluster-securitygroupids): {{
    - String}}
  [SnapshotArns](#cfn-memorydb-cluster-snapshotarns): {{
    - String}}
  [SnapshotName](#cfn-memorydb-cluster-snapshotname): {{String}}
  [SnapshotRetentionLimit](#cfn-memorydb-cluster-snapshotretentionlimit): {{Integer}}
  [SnapshotWindow](#cfn-memorydb-cluster-snapshotwindow): {{String}}
  [SnsTopicArn](#cfn-memorydb-cluster-snstopicarn): {{String}}
  [SnsTopicStatus](#cfn-memorydb-cluster-snstopicstatus): {{String}}
  [SubnetGroupName](#cfn-memorydb-cluster-subnetgroupname): {{String}}
  [Tags](#cfn-memorydb-cluster-tags): {{
    - Tag}}
  [TLSEnabled](#cfn-memorydb-cluster-tlsenabled): {{Boolean}}
```

## Properties
<a name="aws-resource-memorydb-cluster-properties"></a>

`ACLName`  <a name="cfn-memorydb-cluster-aclname"></a>
The name of the Access Control List to associate with the cluster.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z][a-zA-Z0-9\-]*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoMinorVersionUpgrade`  <a name="cfn-memorydb-cluster-autominorversionupgrade"></a>
When set to true, the cluster will automatically receive minor engine version upgrades after launch.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterEndpoint`  <a name="cfn-memorydb-cluster-clusterendpoint"></a>
The cluster's configuration endpoint.
*Required*: No
*Type*: [Endpoint](aws-properties-memorydb-cluster-endpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterName`  <a name="cfn-memorydb-cluster-clustername"></a>
The name of the cluster.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z][a-z0-9\-]*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataTiering`  <a name="cfn-memorydb-cluster-datatiering"></a>
Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html).
*Required*: No
*Type*: String
*Allowed values*: `true | false`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-memorydb-cluster-description"></a>
A description of the cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-memorydb-cluster-engine"></a>
The name of the engine used by the cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EngineVersion`  <a name="cfn-memorydb-cluster-engineversion"></a>
The Redis engine version used by the cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FinalSnapshotName`  <a name="cfn-memorydb-cluster-finalsnapshotname"></a>
The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpDiscovery`  <a name="cfn-memorydb-cluster-ipdiscovery"></a>
The mechanism that the cluster uses to discover IP addresses. Returns 'ipv4' when DNS endpoints resolve to IPv4 addresses, or 'ipv6' when DNS endpoints resolve to IPv6 addresses.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-memorydb-cluster-kmskeyid"></a>
The ID of the KMS key used to encrypt the cluster.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaintenanceWindow`  <a name="cfn-memorydb-cluster-maintenancewindow"></a>
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC). The minimum maintenance window is a 60 minute period.
*Pattern*: `ddd:hh24:mi-ddd:hh24:mi`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiRegionClusterName`  <a name="cfn-memorydb-cluster-multiregionclustername"></a>
The name of the multi-Region cluster that this cluster belongs to.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkType`  <a name="cfn-memorydb-cluster-networktype"></a>
The IP address type for the cluster. Returns 'ipv4' for IPv4 only, 'ipv6' for IPv6 only, or 'dual-stack' if the cluster supports both IPv4 and IPv6 addressing.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6 | dual_stack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NodeType`  <a name="cfn-memorydb-cluster-nodetype"></a>
The cluster's node type.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumReplicasPerShard`  <a name="cfn-memorydb-cluster-numreplicaspershard"></a>
The number of replicas to apply to each shard.
*Default value*: `1`
*Maximum value*: `5`
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumShards`  <a name="cfn-memorydb-cluster-numshards"></a>
The number of shards in the cluster.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterGroupName`  <a name="cfn-memorydb-cluster-parametergroupname"></a>
The name of the parameter group used by the cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-memorydb-cluster-port"></a>
The port used by the cluster.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-memorydb-cluster-securitygroupids"></a>
A list of security group names to associate with this cluster.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotArns`  <a name="cfn-memorydb-cluster-snapshotarns"></a>
A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster. The Amazon S3 object name in the ARN cannot contain any commas.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotName`  <a name="cfn-memorydb-cluster-snapshotname"></a>
The name of a snapshot from which to restore data into the new cluster. The snapshot status changes to restoring while the new cluster is being created.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotRetentionLimit`  <a name="cfn-memorydb-cluster-snapshotretentionlimit"></a>
The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotWindow`  <a name="cfn-memorydb-cluster-snapshotwindow"></a>
The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard. Example: 05:00-09:00 If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsTopicArn`  <a name="cfn-memorydb-cluster-snstopicarn"></a>
When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the ARN of the SNS topic, such as `arn:aws:memorydb:us-east-1:123456789012:mySNSTopic`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsTopicStatus`  <a name="cfn-memorydb-cluster-snstopicstatus"></a>
The SNS topic must be in Active status to receive notifications.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetGroupName`  <a name="cfn-memorydb-cluster-subnetgroupname"></a>
The name of the subnet group used by the cluster.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-memorydb-cluster-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-memorydb-cluster-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TLSEnabled`  <a name="cfn-memorydb-cluster-tlsenabled"></a>
A flag to indicate if In-transit encryption is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-memorydb-cluster-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-memorydb-cluster-return-values-fn--getatt"></a>

####
<a name="aws-resource-memorydb-cluster-return-values-fn--getatt-fn--getatt"></a>

`ARN`  <a name="ARN-fn::getatt"></a>
When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the ARN of the cluster, such as `arn:aws:memorydb:us-east-1:123456789012:cluster/my-cluster`

`ClusterEndpoint.Address`  <a name="ClusterEndpoint.Address-fn::getatt"></a>
The address of the cluster's configuration endpoint.

`ClusterEndpoint.Port`  <a name="ClusterEndpoint.Port-fn::getatt"></a>
The port used by the cluster configuration endpoint.

`ParameterGroupStatus`  <a name="ParameterGroupStatus-fn::getatt"></a>
The status of the parameter group used by the cluster, for example `active` or `applying`.

`Status`  <a name="Status-fn::getatt"></a>
The status of the cluster. For example, 'available', 'updating' or 'creating'.
