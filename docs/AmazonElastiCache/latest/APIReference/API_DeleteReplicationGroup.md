---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteReplicationGroup.html
---

# DeleteReplicationGroup
<a name="API_DeleteReplicationGroup"></a>

Deletes an existing replication group. By default, this operation deletes the entire replication group, including the primary/primaries and all of the read replicas. If the replication group has only one primary, you can optionally delete only the read replicas, while retaining the primary by setting `RetainPrimaryCluster=true`.

When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.

**Note**
 `CreateSnapshot` permission is required to create a final snapshot. Without this permission, the API call will fail with an `Access Denied` exception.
This operation is valid for Redis OSS only.

## Request Parameters
<a name="API_DeleteReplicationGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ReplicationGroupId **
The identifier for the cluster to be deleted. This parameter is not case sensitive.
Type: String
Required: Yes

 ** FinalSnapshotIdentifier **
The name of a final node group (shard) snapshot. ElastiCache creates the snapshot from the primary node in the cluster, rather than one of the replicas; this is to ensure that it captures the freshest data. After the final snapshot is taken, the replication group is immediately deleted.
Type: String
Required: No

 ** RetainPrimaryCluster **
If set to `true`, all of the read replicas are deleted, but the primary node is retained.
Type: Boolean
Required: No

## Response Elements
<a name="API_DeleteReplicationGroup_ResponseElements"></a>

The following element is returned by the service.

 ** ReplicationGroup **
Contains all of the attributes of a specific Valkey or Redis OSS replication group.
Type: [ReplicationGroup](API_ReplicationGroup.md) object

## Errors
<a name="API_DeleteReplicationGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## Examples
<a name="API_DeleteReplicationGroup_Examples"></a>

### DeleteReplicationGroup
<a name="API_DeleteReplicationGroup_Example_1"></a>

This example illustrates one usage of DeleteReplicationGroup.

#### Sample Request
<a name="API_DeleteReplicationGroup_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DeleteReplicationGroup &RetainPrimaryCluster=false
   &FinalSnapshotIdentifier=my-final-snapshot
   &ReplicationGroupId=my-repgroup
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DeleteReplicationGroup_Example_1_Response"></a>

```
<DeleteReplicationGroupResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
   <DeleteReplicationGroupResult>
      <ReplicationGroup>
         <SnapshottingClusterId>my-redis-primary</SnapshottingClusterId>
decrease-replica-count         <ReplicationGroupId>my-repgroup</ReplicationGroupId>
         <Status>deleting</Status>
         <PendingModifiedValues />
         <Description>My replication group</Description>
      </ReplicationGroup>
   </DeleteReplicationGroupResult>
   <ResponseMetadata>
      <RequestId>93eb37db-b9d7-11e3-8a16-7978bb24ffdf</RequestId>
   </ResponseMetadata>
</DeleteReplicationGroupResponse>
```

## See Also
<a name="API_DeleteReplicationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DeleteReplicationGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DeleteReplicationGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DeleteReplicationGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DeleteReplicationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DeleteReplicationGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DeleteReplicationGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DeleteReplicationGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DeleteReplicationGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DeleteReplicationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DeleteReplicationGroup)
