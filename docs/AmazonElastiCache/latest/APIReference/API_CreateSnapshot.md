---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateSnapshot.html
---

# CreateSnapshot
<a name="API_CreateSnapshot"></a>

Creates a copy of an entire cluster or replication group at a specific moment in time.

**Note**
This operation is valid for Valkey or Redis OSS only.

## Request Parameters
<a name="API_CreateSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SnapshotName **
A name for the snapshot being created. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** CacheClusterId **
The identifier of an existing cluster. The snapshot is created from this cluster.
Type: String
Required: No

 ** KmsKeyId **
The ID of the KMS key used to encrypt the snapshot.
Type: String
Required: No

 ** ReplicationGroupId **
The identifier of an existing replication group. The snapshot is created from this replication group.
Type: String
Required: No

 **Tags.Tag.N**
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_CreateSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** Snapshot **
Represents a copy of an entire Valkey or Redis OSS cluster as of the time when the snapshot was taken.
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_CreateSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheClusterNotFound **
The requested cluster ID does not refer to an existing cluster.
HTTP Status Code: 404

 ** InvalidCacheClusterState **
The requested cluster is not in the `available` state.
HTTP Status Code: 400

 ** InvalidParameterCombination **
Two or more incompatible parameters were specified.
 ** message **
Two or more parameters that must not be used together were used together.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidReplicationGroupState **
The requested replication group is not in the `available` state.
HTTP Status Code: 400

 ** ReplicationGroupNotFoundFault **
The specified replication group does not exist.
HTTP Status Code: 404

 ** SnapshotAlreadyExistsFault **
You already have a snapshot with the given name.
HTTP Status Code: 400

 ** SnapshotFeatureNotSupportedFault **
You attempted one of the following operations:
+ Creating a snapshot of a Valkey or Redis OSS cluster running on a `cache.t1.micro` cache node.
+ Creating a snapshot of a cluster that is running Memcached rather than Valkey or Redis OSS.
Neither of these are supported by ElastiCache.
HTTP Status Code: 400

 ** SnapshotQuotaExceededFault **
The request cannot be processed because it would exceed the maximum number of snapshots.
HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **
The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.
HTTP Status Code: 400

## Examples
<a name="API_CreateSnapshot_Examples"></a>

### CreateSnapshot
<a name="API_CreateSnapshot_Example_1"></a>

This example illustrates one usage of CreateSnapshot.

#### Sample Request
<a name="API_CreateSnapshot_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=CreateSnapshot
   &CacheClusterId=my-redis-primary
   &SnapshotName=my-manual-snapshot
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_CreateSnapshot_Example_1_Response"></a>

```
<CreateSnapshotResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
   <CreateSnapshotResult>
      <Snapshot>
         <CacheClusterId>my-redis-primary</CacheClusterId>
         <Port>6379</Port>
         <CacheNodeType>cache.m1.small</CacheNodeType>
         <CacheParameterGroupName>default.redis2.8</CacheParameterGroupName>
         <Engine>redis</Engine>
         <PreferredAvailabilityZone>us-west-2c</PreferredAvailabilityZone>
         <CacheClusterCreateTime>2015-02-02T18:46:57.972Z</CacheClusterCreateTime>
         <EngineVersion>2.8.6</EngineVersion>
         <SnapshotSource>manual</SnapshotSource>
         <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
         <PreferredMaintenanceWindow>wed:09:00-wed:10:00</PreferredMaintenanceWindow>
         <SnapshotName>my-manual-snapshot</SnapshotName>
         <SnapshotRetentionLimit>5</SnapshotRetentionLimit>
         <NodeSnapshots>
            <NodeSnapshot>
               <CacheNodeCreateTime>2015-02-02T18:46:57.972Z</CacheNodeCreateTime>
               <CacheNodeId>0001</CacheNodeId>
               <CacheSize />
            </NodeSnapshot>
         </NodeSnapshots>
         <SnapshotStatus>creating</SnapshotStatus>
         <NumCacheNodes>1</NumCacheNodes>
         <SnapshotWindow>07:30-08:30</SnapshotWindow>
      </Snapshot>
   </CreateSnapshotResult>
   <ResponseMetadata>
      <RequestId>faf5a232-b9ce-11e3-8a16-7978bb24ffdf</RequestId>
   </ResponseMetadata>
</CreateSnapshotResponse>
```

## See Also
<a name="API_CreateSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/CreateSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/CreateSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CreateSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/CreateSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CreateSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/CreateSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/CreateSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/CreateSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/CreateSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CreateSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
