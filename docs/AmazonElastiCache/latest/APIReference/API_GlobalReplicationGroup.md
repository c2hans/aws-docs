---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_GlobalReplicationGroup.html
---

# GlobalReplicationGroup
<a name="API_GlobalReplicationGroup"></a>

Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different Amazon region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.
+ The **GlobalReplicationGroupIdSuffix** represents the name of the Global datastore, which is what you use to associate a secondary cluster.

## Contents
<a name="API_GlobalReplicationGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ARN **
The ARN (Amazon Resource Name) of the global replication group.
Type: String
Required: No

 ** AtRestEncryptionEnabled **
A flag that enables encryption at rest when set to `true`.
You cannot modify the value of `AtRestEncryptionEnabled` after the replication group is created. To enable encryption at rest on a replication group you must set `AtRestEncryptionEnabled` to `true` when you create the replication group.
 **Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6`, `4.x` or later.
Type: Boolean
Required: No

 ** AuthTokenEnabled **
A flag that enables using an `AuthToken` (password) when issuing Valkey or Redis OSS commands.
Default: `false`
Type: Boolean
Required: No

 ** CacheNodeType **
The cache node type of the Global datastore
Type: String
Required: No

 ** ClusterEnabled **
A flag that indicates whether the Global datastore is cluster enabled.
Type: Boolean
Required: No

 ** Engine **
The ElastiCache engine. For Valkey or Redis OSS only.
Type: String
Required: No

 ** EngineVersion **
The ElastiCache engine version.
Type: String
Required: No

 ** GlobalNodeGroups.GlobalNodeGroup.N **
Indicates the slot configuration and global identifier for each slice group.
Type: Array of [GlobalNodeGroup](API_GlobalNodeGroup.md) objects
Required: No

 ** GlobalReplicationGroupDescription **
The optional description of the Global datastore
Type: String
Required: No

 ** GlobalReplicationGroupId **
The name of the Global datastore
Type: String
Required: No

 ** Members.GlobalReplicationGroupMember.N **
The replication groups that comprise the Global datastore.
Type: Array of [GlobalReplicationGroupMember](API_GlobalReplicationGroupMember.md) objects
Required: No

 ** Status **
The status of the Global datastore
Type: String
Required: No

 ** TransitEncryptionEnabled **
A flag that enables in-transit encryption when set to true.
 **Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6`, `4.x` or later.
Type: Boolean
Required: No

## See Also
<a name="API_GlobalReplicationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/GlobalReplicationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/GlobalReplicationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/GlobalReplicationGroup)
